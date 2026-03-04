/**
 * Rollo SMS Server — port 8743
 * Twilio integration: outbound SMS, inbound reply webhook, guarantee logic
 * Keep this file private — contains API credentials
 */

const express = require('express');
const cors    = require('cors');
const fs      = require('fs');
const path    = require('path');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// ── CONFIG (fill in your Twilio credentials) ──────────────────
const CONFIG = {
  twilio: {
    accountSid: process.env.TWILIO_SID   || 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    authToken:  process.env.TWILIO_TOKEN || 'your_auth_token_here',
    fromNumber: process.env.TWILIO_FROM  || '+353XXXXXXXXX',  // your Irish Twilio number
  },
  guarantee: {
    capAmount:      100,    // €100 max payout
    windowMinutes:  120,    // 2-hour arrival window
    lateAlertMins:  15,     // alert office after 15 mins past window
    autoClaimMins:  30,     // log potential claim after 30 mins past window
    claimWindowHrs: 48,     // customer must claim within 48 hours
    maxClaimsPerYear: 1,    // per customer per 12 months
  },
  company: {
    name:  'Rollo Heating & Plumbing',
    phone: '01-XXX-XXXX',
    email: 'info@rolloheating.ie',
  },
};

// ── DATA STORE (JSON file — swap for DB later) ─────────────────
const DATA_FILE = path.join(__dirname, 'sms-data.json');
function readData() {
  try { return JSON.parse(fs.readFileSync(DATA_FILE, 'utf8')); }
  catch { return { smsLog: [], claims: [], smsQueue: [] }; }
}
function writeData(d) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(d, null, 2));
}

// ── SMS TEMPLATES ──────────────────────────────────────────────
const TEMPLATES = {
  booking_confirmation: (d) =>
    `Hi ${d.customerName}, your ${d.jobType} appointment with ${d.company} is confirmed for ${d.date} between ${d.windowStart}–${d.windowEnd}. Reply YES to confirm you'll be home, or call ${d.phone} to reschedule. Job ref: #${d.jobNumber}`,

  on_my_way: (d) =>
    `Hi ${d.customerName}, good news — ${d.engineerName} is on the way to you now and should arrive in approx. ${d.eta} mins. Job: #${d.jobNumber} 🚗`,

  running_late: (d) =>
    `Hi ${d.customerName}, we're sorry — ${d.engineerName} is running a little behind. New estimated arrival: ${d.newEta}. We apologise for the inconvenience. Call us: ${d.phone}`,

  cant_make_it: (d) =>
    `Hi ${d.customerName}, we're very sorry — we need to reschedule your appointment today (Job #${d.jobNumber}). Please call ${d.phone} or reply RESCHEDULE and we'll sort a new time. We apologise for the disruption.`,

  guarantee_triggered: (d) =>
    `Hi ${d.customerName}, we're sorry your engineer didn't arrive as scheduled. As per our On-Time Guarantee, you're entitled to a €${d.amount} credit. We'll be in touch within 24hrs to arrange this. Ref: #${d.jobNumber}`,

  job_complete: (d) =>
    `Hi ${d.customerName}, job #${d.jobNumber} is now complete ✅ Your invoice for €${d.amount} is on its way. Thank you for choosing ${d.company}! 🔧`,

  invoice_reminder: (d) =>
    `Hi ${d.customerName}, friendly reminder — invoice #${d.invoiceNum} for €${d.amount} from ${d.company} is now ${d.days} days overdue. Pay online or call ${d.phone}. Thank you.`,

  customer_confirmation_reply: (d) =>
    `Great, ${d.customerName}! Appointment confirmed for ${d.date}. We'll text you when ${d.engineerName} is on the way. ${d.company}`,

  reschedule_reply: (d) =>
    `Thanks ${d.customerName} — our office will call you within 2 hours to arrange a new time. Apologies for the inconvenience. ${d.company}`,
};

// ── TWILIO CLIENT (lazy init — only when keys are set) ─────────
let twilioClient = null;
function getTwilio() {
  if (twilioClient) return twilioClient;
  const { accountSid, authToken } = CONFIG.twilio;
  if (accountSid.startsWith('AC') && !accountSid.includes('xxx')) {
    const twilio = require('twilio');
    twilioClient = twilio(accountSid, authToken);
  }
  return twilioClient;
}

// ── SEND SMS ───────────────────────────────────────────────────
async function sendSMS(to, body, jobId = null, template = null) {
  const data = readData();
  const logEntry = {
    id: 'sms_' + Date.now(),
    to, body, jobId, template,
    sentAt: new Date().toISOString(),
    status: 'queued',
    sid: null,
  };

  const client = getTwilio();
  if (client) {
    try {
      const msg = await client.messages.create({
        body,
        from: CONFIG.twilio.fromNumber,
        to,
      });
      logEntry.status = 'sent';
      logEntry.sid = msg.sid;
      console.log(`✅ SMS sent to ${to}: ${body.substring(0, 50)}...`);
    } catch (err) {
      logEntry.status = 'failed';
      logEntry.error = err.message;
      console.error(`❌ SMS failed to ${to}:`, err.message);
    }
  } else {
    // Demo mode — log but don't send
    logEntry.status = 'demo';
    console.log(`📱 [DEMO] SMS to ${to}: ${body}`);
  }

  data.smsLog.unshift(logEntry);
  writeData(data);
  return logEntry;
}

// ═══════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════

// Health check
app.get('/status', (req, res) => {
  const client = getTwilio();
  res.json({
    ok: true,
    mode: client ? 'live' : 'demo',
    from: CONFIG.twilio.fromNumber,
    guarantee: CONFIG.guarantee,
    company: CONFIG.company,
  });
});

// ── Send templated SMS ─────────────────────────────────────────
app.post('/sms/send', async (req, res) => {
  const { template, data, to, body } = req.body;
  let messageBody = body;

  if (template && TEMPLATES[template] && data) {
    messageBody = TEMPLATES[template]({ ...data, ...CONFIG.company, phone: CONFIG.company.phone });
  }

  if (!to || !messageBody) {
    return res.status(400).json({ error: 'Missing to or message body' });
  }

  const result = await sendSMS(to, messageBody, data?.jobId || null, template);
  res.json({ ok: true, result });
});

// ── On My Way trigger ──────────────────────────────────────────
app.post('/sms/on-my-way', async (req, res) => {
  const { jobNumber, customerName, customerPhone, engineerName, eta, jobId } = req.body;
  if (!customerPhone) return res.status(400).json({ error: 'No phone number' });

  const body = TEMPLATES.on_my_way({
    customerName, engineerName,
    eta: eta || 20,
    jobNumber,
    company: CONFIG.company.name,
  });

  const result = await sendSMS(customerPhone, body, jobId, 'on_my_way');

  // Log the on-my-way time for late detection
  const data = readData();
  const existingIdx = data.claims.findIndex(c => c.jobId === jobId && c.type === 'omw');
  if (existingIdx < 0) {
    data.claims.push({ type: 'omw', jobId, jobNumber, sentAt: new Date().toISOString() });
    writeData(data);
  }

  res.json({ ok: true, result });
});

// ── Running late ───────────────────────────────────────────────
app.post('/sms/running-late', async (req, res) => {
  const { jobNumber, customerName, customerPhone, engineerName, newEta, jobId } = req.body;
  const body = TEMPLATES.running_late({
    customerName, engineerName,
    newEta: newEta || 'TBC',
    phone: CONFIG.company.phone,
    jobNumber,
  });
  const result = await sendSMS(customerPhone, body, jobId, 'running_late');
  res.json({ ok: true, result });
});

// ── Can't make it (guarantee trigger candidate) ────────────────
app.post('/sms/cant-make-it', async (req, res) => {
  const { jobNumber, customerName, customerPhone, jobId, confirmedByCustomer } = req.body;
  const body = TEMPLATES.cant_make_it({
    customerName, jobNumber, phone: CONFIG.company.phone,
  });
  const result = await sendSMS(customerPhone, body, jobId, 'cant_make_it');

  // Log potential claim if customer had confirmed
  if (confirmedByCustomer) {
    const data = readData();
    data.claims.push({
      id: 'claim_' + Date.now(),
      type: 'potential',
      jobId, jobNumber, customerName, customerPhone,
      capAmount: CONFIG.guarantee.capAmount,
      triggeredAt: new Date().toISOString(),
      status: 'pending_review',  // office must approve/reject
      resolution: null,
    });
    writeData(data);
  }

  res.json({ ok: true, result });
});

// ── Job complete SMS ───────────────────────────────────────────
app.post('/sms/job-complete', async (req, res) => {
  const { jobNumber, customerName, customerPhone, amount, jobId } = req.body;
  const body = TEMPLATES.job_complete({
    customerName, jobNumber,
    amount: parseFloat(amount).toFixed(2),
    company: CONFIG.company.name,
  });
  const result = await sendSMS(customerPhone, body, jobId, 'job_complete');
  res.json({ ok: true, result });
});

// ── Booking confirmation ───────────────────────────────────────
app.post('/sms/booking-confirm', async (req, res) => {
  const { jobNumber, customerName, customerPhone, jobType, date, windowStart, windowEnd, jobId } = req.body;
  const body = TEMPLATES.booking_confirmation({
    customerName, jobType, date,
    windowStart: windowStart || '09:00',
    windowEnd: windowEnd || '11:00',
    phone: CONFIG.company.phone,
    jobNumber, company: CONFIG.company.name,
  });
  const result = await sendSMS(customerPhone, body, jobId, 'booking_confirmation');

  // Mark job as "awaiting confirmation"
  const data = readData();
  data.claims.push({
    type: 'awaiting_confirm', jobId, jobNumber,
    sentAt: new Date().toISOString(), confirmed: false,
  });
  writeData(data);

  res.json({ ok: true, result });
});

// ── Inbound SMS webhook (Twilio calls this URL) ────────────────
// Set this as your Twilio phone number webhook:
// http://YOUR_SERVER:8743/sms/inbound
app.post('/sms/inbound', async (req, res) => {
  const from  = req.body.From  || '';
  const body  = (req.body.Body || '').trim().toUpperCase();
  const data  = readData();

  console.log(`📩 Inbound SMS from ${from}: "${body}"`);

  let replyBody = null;
  let action    = 'received';

  if (body === 'YES' || body === 'CONFIRM') {
    // Mark job as confirmed by customer
    const pending = data.claims.find(c => c.type === 'awaiting_confirm' && !c.confirmed);
    if (pending) {
      pending.confirmed = true;
      pending.confirmedAt = new Date().toISOString();
      pending.confirmedFrom = from;
      // Activate guarantee for this job
      data.claims.push({
        type: 'guarantee_active', jobId: pending.jobId,
        jobNumber: pending.jobNumber, confirmedAt: new Date().toISOString(),
        customerPhone: from, capAmount: CONFIG.guarantee.capAmount,
      });
      action = 'confirmed';
      replyBody = TEMPLATES.customer_confirmation_reply({
        customerName: 'there',
        date: 'your scheduled date',
        engineerName: 'your engineer',
        company: CONFIG.company.name,
      });
    } else {
      replyBody = `Thanks! We'll see you on your appointment day. ${CONFIG.company.name}`;
    }
  } else if (body === 'NO' || body === 'CANCEL' || body === 'RESCHEDULE') {
    action = 'reschedule_requested';
    replyBody = TEMPLATES.reschedule_reply({
      customerName: 'there',
      company: CONFIG.company.name,
    });
    // Log reschedule request
    data.smsLog.unshift({
      id: 'inbound_' + Date.now(), from, body: req.body.Body,
      action, receivedAt: new Date().toISOString(),
    });
  } else if (body === 'LATE?' || body === 'WHEN' || body === 'ETA') {
    action = 'eta_query';
    replyBody = `Our engineer is on the way. We'll send an update shortly. Call us if urgent: ${CONFIG.company.phone}`;
  } else if (body === 'STOP' || body === 'UNSUBSCRIBE') {
    action = 'unsubscribed';
    replyBody = `You've been unsubscribed from ${CONFIG.company.name} messages. Call ${CONFIG.company.phone} to manage your appointment.`;
  } else {
    action = 'unknown';
    replyBody = `Thanks for your message. To speak to us, call ${CONFIG.company.phone} or visit our office. ${CONFIG.company.name}`;
  }

  // Log inbound
  data.smsLog.unshift({
    id: 'inbound_' + Date.now(), direction: 'inbound',
    from, body: req.body.Body, action,
    receivedAt: new Date().toISOString(),
  });
  writeData(data);

  // Reply using TwiML
  const twiml = replyBody
    ? `<?xml version="1.0" encoding="UTF-8"?><Response><Message>${replyBody}</Message></Response>`
    : `<?xml version="1.0" encoding="UTF-8"?><Response></Response>`;

  res.set('Content-Type', 'text/xml');
  res.send(twiml);
});

// ── Guarantee claims management ────────────────────────────────
app.get('/guarantee/claims', (req, res) => {
  const data = readData();
  const claims = data.claims.filter(c => c.type === 'potential' || c.type === 'approved' || c.type === 'rejected');
  res.json({ ok: true, claims, config: CONFIG.guarantee });
});

app.post('/guarantee/resolve', (req, res) => {
  const { claimId, resolution, notes } = req.body; // resolution: 'approved' | 'rejected'
  const data = readData();
  const claim = data.claims.find(c => c.id === claimId);
  if (!claim) return res.status(404).json({ error: 'Claim not found' });

  claim.status = resolution;
  claim.resolution = resolution;
  claim.resolutionNotes = notes;
  claim.resolvedAt = new Date().toISOString();

  if (resolution === 'approved') {
    claim.compensationAmount = Math.min(CONFIG.guarantee.capAmount, claim.requestedAmount || CONFIG.guarantee.capAmount);
    // Send guarantee SMS to customer
    sendSMS(claim.customerPhone, TEMPLATES.guarantee_triggered({
      customerName: claim.customerName,
      amount: claim.compensationAmount,
      jobNumber: claim.jobNumber,
      company: CONFIG.company.name,
    }), claim.jobId, 'guarantee_triggered');
  }

  writeData(data);
  res.json({ ok: true, claim });
});

// ── SMS log ────────────────────────────────────────────────────
app.get('/sms/log', (req, res) => {
  const data = readData();
  res.json({ ok: true, log: data.smsLog.slice(0, 100) });
});

// ── Config update (for setting Twilio credentials via UI) ──────
app.post('/config', (req, res) => {
  const { sid, token, from, companyPhone } = req.body;
  if (sid)  CONFIG.twilio.accountSid  = sid;
  if (token) CONFIG.twilio.authToken  = token;
  if (from)  CONFIG.twilio.fromNumber = from;
  if (companyPhone) CONFIG.company.phone = companyPhone;
  twilioClient = null; // reset client
  res.json({ ok: true, mode: getTwilio() ? 'live' : 'demo' });
});

// ── Start ──────────────────────────────────────────────────────
const PORT = 8743;
app.listen(PORT, () => {
  console.log(`\n⚔️  Rollo SMS Server running on http://localhost:${PORT}`);
  console.log(`   Mode: ${getTwilio() ? '🟢 LIVE (Twilio connected)' : '🟡 DEMO (add Twilio credentials to go live)'}`);
  console.log(`   Inbound webhook URL: http://YOUR_DOMAIN:${PORT}/sms/inbound`);
  console.log(`   Status: http://localhost:${PORT}/status\n`);
});
