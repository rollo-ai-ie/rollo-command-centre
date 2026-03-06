# ServiceM8 Premium Plus: Complete Feature & Add-on Reference

ServiceM8 is a cloud-based field service management platform built around **four fixed job statuses** (Quote, Work Order, Completed, Unsuccessful), a **Dispatch Board** serving as the central operational hub, and an **iOS mobile app** for field staff. Every feature below has been documented from official ServiceM8 help articles, developer docs, and verified partner resources to serve as a build specification reference for the Rollo Command Center.

---

## 1. Badges — visual job flags that drive workflow behavior

Badges are **virtual stickers** displayed prominently at the top of job cards that communicate job requirements from the office to field workers. They appear in full color when active and greyed out when inactive. Badges can be applied to individual jobs or to client records (where they propagate to all future jobs for that client). They are configured at Settings > Badges and can be pre-set in Job Templates for automatic application.

**Five badge categories exist**, each with distinct behavior:

- **Information Only** — Passive visual indicators (e.g., lead source, VIP client, special instructions). No triggered actions. Visible in reporting exports. Can be applied to both jobs and clients.
- **Form** — Linked to a specific ServiceM8 Form. When activated on a job, the associated form appears as a **checklist item** in the mobile app, ensuring field staff see and complete required paperwork. This is the primary mechanism for enforcing compliance documentation.
- **Follow Up** — Displayed in a distinctive **ribbon shape**. Activates when a job is completed. Creates recurring job reminders and triggers inbox notifications before follow-up dates. The badge must be ticked **before** job completion to fire correctly.
- **Automation** — Created via Settings > Automation > New Automation. Each automation badge triggers a scheduled email/SMS follow-up after job completion. Includes a **"Skip sending if..."** option that cancels the message if the client books before the automated send date.
- **Asset** — Auto-created when Asset Types are configured in the Asset Management add-on. Must be enabled on a job to access the Assets menu. Linked to QR code scanning and augmented reality features.

A special built-in **Burn List** badge flags problematic clients with an immediate warning alert when anyone creates a job for that client. Custom badges support configurable icons and colors (since ServiceM8 13, September 2024). Security roles control badge visibility per staff member.

---

## 2. Job Queues — parking jobs while waiting for action

Job Queues are virtual folders where jobs are held while waiting for something to happen before they can progress. They remove on-hold jobs from standard lists, reducing clutter on the Dispatch Board. Configured at Settings > Job Queues.

**Two queue types serve different purposes.** Regular Queues hold jobs waiting on **external actions** (parts arriving, client response, site readiness). Default examples include "Parts on Order," "Pending Quotes," and "Workshop." Assignable Queues hold jobs waiting on **internal actions** (staff needs to place an order, send a quote). These are assigned to a specific staff member who receives a notification, and the job appears in their "For My Review" list. Assignable queues display in a **different color** on the dashboard and mobile app.

**Every queued job has an expiry date**, set when placing the job in the queue. Each queue has a configurable Default Timeframe to save manual date entry. When a job's queue timer expires, it enters a **"Due for Review"/"Expired" state** — automatically flagged in the Queues view, appearing in both the Action Required and Unscheduled Jobs lists. On mobile, expired jobs show a **lighter background**. A **yellow dot** appears next to any queued job in lists, with hover details showing queue name and expiry.

Jobs enter queues by **dragging onto the queue icon** on the Dispatch Board (which prompts for duration). They can be moved between queues by dragging to a different queue. Jobs leave queues by right-clicking and selecting "Remove from queue," or automatically when the expiry date is reached — at which point they pop back onto the Unscheduled Jobs tab. Queue activity is tracked in the Job Diary under the "Bookings & Queues" filter.

---

## 3. Allocation Windows — flexible scheduling without fixed times

Allocation Windows are part of the **Job Allocations add-on** and provide booking timeframes rather than fixed appointment times. Instead of scheduling "Tuesday at 10:00 AM," a job is allocated with a window like "Morning" or "Anytime," giving field operations flexibility that enables route optimization.

**Four default windows exist with configurable priority levels** (1–5) that determine job list ordering: **Urgent** (Priority 1, top of list), **Morning**, **Afternoon**, and **Anytime** (Priority 5, bottom of list). Custom windows can be added with configurable names, start/end times, and priority levels at Settings > Allocation Windows.

Allocations differ from scheduled bookings in a critical way. **Scheduled bookings** occupy specific time blocks on the Staff Schedule calendar. **Allocations** appear in a staff member's job list ordered by priority without occupying a fixed slot, which is essential for **Auto Routing** — ServiceM8's route optimization engine. Three optimization levels exist: Low (reorder allocations only), Medium (reschedule fixed bookings + reorder), and High (convert all to allocations for maximum optimization).

When creating an allocation from the Dashboard, dragging a job onto a staff member's icon produces a popup with fields for **Booking Window**, **Estimated Duration**, **Start Date**, **Booking Expiry**, **Message**, and **Notification method**. The Urgent window triggers an immediate notification with the job added to the top of the staff member's schedule. Allocated jobs can optionally appear on Staff Schedules (configurable in Settings > Preferences). If not completed by expiry, the allocation disappears and the job appears in Action Required with a red dot.

---

## 4. Customer Feedback — automated review collection with Google redirect

The Feedback add-on collects **star ratings** (out of 5) and **short written reviews** (limited to **160 characters**) from customers after job completion. Configuration lives at Settings > Feedback, where you paste Google and/or Facebook review URLs. Customers rating **4+ stars** are automatically redirected to a thank-you page inviting them to leave a public Google or Facebook review.

**Two collection methods exist.** The `{feedback}` merge field generates a unique, job-specific feedback link for use in email/SMS templates — responses are stored in the relevant job's diary. A separate general feedback link (constant per account) can be placed on websites, invoices, or email signatures, but feedback from this link is anonymous and not job-linked.

Automated feedback requests are configured via the Automation add-on, triggered **after invoice payment**. A **30-day cooldown period** prevents repeat requests to regular clients with multiple jobs per month. The cooldown applies only to internal ServiceM8 feedback, not external Google/Facebook reviews. Duplicate prevention ensures automated requests are only sent if the customer hasn't already provided feedback for that specific job. The email is sent from the staff member who produced the invoice.

---

## 5. Forms — the compliance and documentation engine

Forms are ServiceM8's most critical documentation feature, enabling electronic completion of paperwork, reports, certificates, and checklists in the field. **Completed forms automatically generate professional PDFs** saved to the job diary. Forms are entirely separate from quotes and invoices.

### Form creation and builder

**Two creation methods exist.** The **auto-generated template** method (introduced September 2024) uses the form editor at Settings > Forms > Add Form — you add questions, and ServiceM8 automatically generates the PDF layout. The **custom Word template** method uses Microsoft Word (.docx) files with MergeField codes matching each question's Template Field Code, allowing complete control over branding, layout, logos, headers/footers, and tables.

The Form Editor provides configuration for each form: **Form Name**, **Badge Name** (every form gets an associated badge), **Badge Requirement** (Optional, Mandatory on Check-In, or Mandatory on Check-Out), and **Form Template** selection. For each question, you configure the **Question label**, **Template Field Code**, **Additional Details** (explanatory text shown in the app), **Mandatory** checkbox, **Question Type**, and **Conditions** (skip logic).

### Eight available field types

Forms support **Text** (short alphanumeric), **Text (Multi-Line)** (detailed responses), **Number** (digits, decimals, negatives), **Date** (calendar picker), **Multiple Choice** (select one — radio-button style), **Multiple Choice (Multi-Answer)** (select many — checkbox style), **Signature** (digital capture, up to 20 per form), and **Photo** (JPEG/PNG capture).

### Conditional logic via "Skip Question IF"

Forms support conditional branching with operators: **Equal to**, **Greater than**, **Less than**, **Contains**, **Does not contain**. Conditions can use **ALL** (all conditions must be met) or **ANY** (any condition triggers skip) logic across multiple questions. This effectively shows/hides questions based on previous answers — for example, if "Completed task?" = "YES," skip "Reason for not completing."

### How forms attach to jobs and enforce compliance

Every form has a **corresponding badge** automatically created. Badges are applied to jobs manually, via Job Templates (ensuring all jobs of a certain type require specific forms), or via Client Cards (propagating to all future jobs for that client). When a form badge is active, the form appears as a **checklist item** in the mobile app.

**Mandatory forms** block job progress: set to "Mandatory on Check-In" to require completion before starting work, or "Mandatory on Check-Out" to require completion before the job can be completed. This is the primary mechanism for enforcing Gas Safety Certificates, risk assessments, JSA/SWMS, electrical certificates, inspection reports, and site audits.

### Mobile completion workflow

Field staff complete forms on iPhone/iPad via the ServiceM8 iOS app. Forms appear as checklist items when badges are active. Staff work through a **step-by-step question sequence** — picking from lists, taking photos, collecting signatures, typing responses, entering dates/numbers. Forms can be **paused and resumed** if interrupted. Job data (customer name, address, contact details) auto-populates via merge fields, eliminating re-entry.

### PDF generation and job diary integration

Completed forms produce a **professional PDF** auto-saved to the job diary. PDFs can be emailed to clients (individually or attached to invoices), printed, or stored as permanent documentation. In the job diary, completed forms appear as clickable PDF items with a dropdown offering **Edit Form**, **Version History**, and email options. Editing a form removes signatures, re-populates merge fields with current data, and generates a new version while maintaining full version history. Forms can also be sent for **remote digital signature** — customers receive an email with a "Review and Sign" button.

### Form Store and reusability

The **Form Store** marketplace offers **250+ ready-made forms** filterable by category, industry, or keyword — covering electrical, plumbing, HVAC, cleaning, locksmith, pool, pest control, and more. Forms are one-time purchases usable unlimited times, available on all plans. Form templates are fully reusable across unlimited jobs and can be exported/imported as `.sm8f` files.

---

## 6. Assets — equipment tracking with QR codes and service history

Asset Management enables tracking of client-site equipment (boilers, cylinders, fire extinguishers, HVAC units) with full service history. **Asset Types** are configured at Settings > Assets with custom fields (free text, number, date, multiple choice) defining what data is tracked per asset category.

Assets are identified via **physical QR Code labels** (~25mm × 30mm, durable PET polyester with UV-resistant ink) ordered from ServiceM8. Assets can **only be created in the iOS app** — field staff scan a QR label, select the Asset Type, enter details, take a photo, and position the asset on a bird's-eye **site map**. Subsequent visits require only scanning the QR code to instantly pull up the asset record. An **Augmented Reality** view lets staff scan one asset's QR code to see and locate all other tagged assets on site through the camera.

**Forms completed against individual assets** build a complete service history timeline. Each question shows **history of past values** for that asset, enabling trend tracking. Completed asset forms are listed in both the asset's history and the job diary. **Service Reports** are auto-generated as PDFs when jobs with asset forms are completed. **Asset Registers** — PDF reports listing all assets for a customer — can be generated from the online dashboard.

A **Customer Portal** allows clients to scan an asset's QR code with their own smartphone to view asset details, report issues, or request service. **Form Follow-Up Automation** can trigger inbox messages based on inspection form responses (e.g., flagging assets needing replacement), with an "On Job Completion" mode to consolidate multiple follow-ups into a single message.

---

## 7. Automation — triggered communications across the job lifecycle

The Automation add-on (free from Starter plan) automates routine communications. All automations are configured at Settings > Automation with setup wizards. **Seven automation types** cover the full job lifecycle:

**Booking Confirmation** sends immediately when a booking is created (email, SMS, or both). **Booking Reminder** sends a configurable number of hours before a scheduled booking — requires the "Booking Reminder" badge to be active on the job. **Quote Follow Up** automatically chases clients who haven't accepted a quote. **Payment Follow Up** chases outstanding invoices with configurable timing and frequency, and can send **pre-payment reminders** before the due date — messages auto-cancel if paid before the scheduled send. **Feedback Request** fires after invoice payment. **Badge Follow Up Automation** (user-created) triggers custom follow-ups after job completion (e.g., annual service reminders) with the "Skip sending if..." option. **Form Response Automation** sends inbox messages based on form question responses, which can be converted to new jobs.

Each automation type except Badge Follow Up comes pre-created. Badge Follow Up Automations are user-created via "New Automation" and each generates a unique badge. All automations are viewable per-job in the Job Diary and monitored from Settings > Automation.

---

## 8. Job Categories — color-coded job classification for filtering and reporting

Job Categories provide an additional classification layer beyond the four fixed statuses. **Four default categories** exist: After-Hours, Standard, VIP, and Warranty. Unlimited custom categories can be created at Settings > Job Categories, each with a **customizable color** displayed on the Dispatch Board schedule and in job lists.

Categories are assigned via the job card dropdown and are **optional** per job. They drive three key reports: **Revenue By Category** (monthly), **Completed Jobs By Category** (monthly), and **Materials Usage Report** (segmented by category). Categories also power custom Job Filters on the Dispatch Board and can be pre-set in Job Templates.

---

## 9. Job Templates — pre-configured job cards for consistent operations

Job Templates are preset configurations that auto-fill new job cards when creating common job types. When activated, the "New Job" button becomes a **dropdown menu** listing all templates. Templates can pre-fill: **Client Name**, **Job Description**, **Checklist items** (lines starting with hyphens become clickable checklist items; including "photo" auto-launches the camera), **Job Notes**, **Billable Items** (materials & services with optional zero-quantity for later finalization), **Labour Rate**, **Work Completed description**, **Badges** (all five types), and **Job Category**.

Templates are central to **Recurring Jobs** — all recurring jobs are based on either a Job Template or a Service. When recurring jobs are auto-created, they inherit the template's descriptions, checklists, badges, forms, and billing items.

---

## 10. Knowledge Articles — an internal wiki for field staff

The Knowledge add-on creates a library of **articles, videos, and PDFs** accessible via the iOS app and online dashboard. Articles support rich formatting (bold, italic, lists, images, tables, hyperlinks). Videos can be recorded directly in the app with start/stop capability — ServiceM8 combines footage segments into a single video.

The key differentiator is a **Smart Tagging system**. Knowledge items tagged with specific Client Names, Item Names/Numbers, or Service Names are **automatically surfaced** inside relevant job cards — proactively presenting information to staff rather than requiring them to search. Phone numbers, job numbers, emails, and URLs within articles are **tappable and actionable**. New knowledge items are posted to the **Activity Feed** for team-wide visibility.

---

## 11. Materials & Services catalogue — pricing, bundles, and markup billing

The Materials & Services catalogue at Settings > Materials & Services stores parts, labour, and services with **Item Number** (code), **Name/Description**, **Price** (sell), **Purchase Cost**, and **Tax settings**. Items are imported via CSV bulk upload, accounting integration (Xero/QuickBooks/MYOB with bidirectional sync), automated supplier import, or manual entry.

On job cards, staff search by item code or keyword in the Quotes & Invoicing tab. **Barcode scanning** in the iOS app matches product barcodes to catalogue items. Costs and prices can be edited per-job without affecting the master catalogue. Items unused for **12 months** are auto-archived (unless total items are under 500), remaining accessible via a link at the bottom of search results.

The **Bundles add-on** combines multiple items into preset packages with a single client-facing description and fixed price — constituent items are hidden from client documents. The **Markup Billing add-on** adds Cost and Markup columns showing real-time markup percentage. The **Job Costing add-on** displays estimated profit/loss per job based on purchase costs vs. sell prices, tracking materials profit, labour profit, and administration time.

---

## 12. Services — systemized pricing, scheduling, and online booking

The Services add-on is **distinct from Materials & Services**. It defines how a business prices and schedules each service type it offers, serving two functions: powering **advanced online booking** forms and providing an **internal pricing/scheduling system** for staff.

Each Service is configured with: **Service Type** (Field, Workshop, or Urgent), **Booking Form Questions** (multiple choice, numeric, text, photo — with conditional branching), **Pricing** (Fixed or Variable based on customer answers), **Scheduling** (which staff can perform it, booking type — Schedule a Quote, Schedule a Service, or No Schedule/enquiry only), **Travel Distance Surcharge**, **Service Radius**, **Minimum/Maximum criteria**, **Scheduling Discount**, and **Deposit/Pre-payment requirements** (via Stripe).

When a Service is applied to a job, it pre-fills pricing, scheduling duration, materials, job description, category, and badges automatically. For online booking, ServiceM8 hosts the booking pages — customers fill out the form, receive a live quote, browse available times (accounting for existing bookings, travel time, and staff leave), and book directly. Jobs are auto-created in ServiceM8 with all details pre-filled.

---

## 13. Network Request Templates and Network Contacts — subcontractor management

**Network Contacts** maintains a list of trusted subcontractors. The Network add-on is free — subcontractors don't need access to your ServiceM8 account. Network Requests are sent from a job card by clicking "Share," which opens a request window with auto-populated job/contact details, a unique reference number (becomes the PO Number in the subcontractor's account), and **Job Requirements** (Task, Photo, Document, Form).

Subcontractors **with** a ServiceM8 account receive requests in their Inbox and convert to a job with one click. Subcontractors **without** an account receive an email with a browser link to view details and complete requirements. The primary business maintains **real-time visibility** as contractors accept, complete requirements, upload files, and mark jobs complete.

**Network Request Templates** (Settings > Network Request Templates) pre-configure standard sets of Job Requirements for repeated work types, functioning like Job Templates for subcontractor requests. Document requirements support **expiry dates** so subcontractors can reuse documents (e.g., insurance certificates) across requests until expiry.

---

## 14. Online Booking and Enquiry — two tiers of customer-facing intake

**Self Serve Online Booking** (via the Services add-on) provides full-featured booking forms per service type. Customers get live quotes, browse available times, book directly, and receive automatic confirmation. Forms are hosted by ServiceM8 — businesses embed HTML button snippets on their websites. Supports Google/Facebook tracking IDs for conversion analytics.

**Simple Online Enquiry** provides a basic form collecting customer name, contact details, job address, description, and optional photo/document attachments. Enquiries arrive in the ServiceM8 **Inbox** for manual review — they are **not** automatically converted to jobs. Clicking "Convert to Job" pre-fills the job card with all submitted information. An automatic "Service Enquiry Confirmation" email is sent to the customer.

---

## 15. Document Templates — Word-based merge field templates for PDFs

Document Templates use Microsoft Word (.docx) files with **MergeField** codes to generate PDF quotes, invoices, and work orders. Three template types exist: Invoice, Quote, and Work Order. Templates are managed at Settings > Document Templates with three options: use a pre-designed library template, modify an existing template, or create from scratch.

Merge fields reference ServiceM8 data using codes like `job.amount_paid`, `job.balance_due`, `job.total`, `job.description`, plus customer/contact details, staff details, materials line items, and up to **10 custom fields** per account for jobs and clients. Fields are inserted in Word via Insert > Quick Parts > Field > MergeField. A downloadable Word document with all available fields pre-formatted is provided by ServiceM8.

---

## 16. Email and SMS Templates — reusable messaging with merge fields

**Email Templates** (Settings > Email Templates) provide pre-formatted messages with dynamic merge fields in curly braces. Key merge fields include `{job.contact_first}`, `{job.next_booking_time}`, `{document}` (generates unique online link for quote/invoice viewing/payment), `{feedback}` (unique feedback link), and `{quote_accept_link}`. Templates support HTML formatting via Source view and AI-powered text drafting.

**Special named templates** override system defaults: "On-Site Service Confirmation," "Workshop Service Confirmation," "Service Enquiry Confirmation," "SMS Invoice," and "Navigate To Job." **Two-Way Email** means customer replies to ServiceM8-sent emails automatically sync to the Job Diary.

**SMS Templates** (Settings > SMS Templates) work similarly with the same merge fields. Every outgoing SMS automatically includes a **"Reply here" link** that opens a branded web messaging portal. Replies are saved to the job diary and trigger push notifications. Since ServiceM8 14, **photo and file attachments** can be shared via SMS. **Branded SMS** (Premium/Premium Plus) shows the business name as sender instead of "ServiceM8."

---

## 17. Proposals — interactive online quotes with customer choice

Proposals (introduced March 2024) create rich, interactive online quote experiences that **co-exist with standard quotes** — for each job, you choose which to use. The WYSIWYG builder supports **photo galleries**, **multiple choice sections** (customers choose quality/color/scope with dynamic price adjustment), **optional extras**, flexible sections, subtotals, and an **AI Smart Writing Helper** (Auto-Write, Improve, Shorten, Lengthen).

Proposals are sent via email or SMS using the `{document}` merge field, which generates a unique client link. Clients view proposals as **interactive web pages**, make selections, and click "Accept" — which automatically changes job status to **Work Order**, logs a diary note, and applies selected materials/services to the Billing tab. The diary tracks **how many times** and **when** clients viewed the proposal. Unaccepted proposals are **"live"** — edits update the client's view in real time without resending. Manual acceptance is available via the diary dropdown > "Apply to Job."

---

## 18. Suppliers — pricing import and invoice matching

Supplier management focuses on **automated pricing updates** and **invoice tracking against jobs**. The **Automated Supplier Import** generates a unique email address per supplier — when suppliers send updated CSV price files to this address, ServiceM8 auto-imports them, creating new items, updating existing ones, and deleting removed items. A configurable **markup percentage** per supplier is applied on import.

**Supplier Invoice Import** provides a special email address for receiving supplier invoices. Staff provide the **ServiceM8 Job Number as the Purchase Order reference** when purchasing. Invoices sent to the email are automatically matched to the correct job. Unmatched invoices appear in the Inbox. Billing options include "Apply Total to Job," "Apply Line Items to Job," or "Apply Bundle to Job."

---

## 19. Security Roles — granular permission control per staff member

Security Roles control access and functionality per staff member, assigned at Account > Settings > Staff > Edit > Security Role. **Five default roles** range from full to minimal access:

**Default Business Owner** has unrestricted access including editing check-in times. **Default Finance** can access all jobs and invoice/quote but cannot access reports or remove jobs. **Default Staff** can access all jobs but cannot see Quote & Invoice PDFs or perform billing. **Default Contractor** sees only their own jobs/schedule with no access to clients, settings, or diary. **Default Strict Contractor** disables the Job Diary and Billing areas entirely — required to hide pricing from contractors.

**Custom roles** can be created at Settings > Security Roles with granular control over: Show New Job Button, access to unassigned jobs, restrict to specific job categories, show/hide all staff schedules, client signoff, quote/invoice buttons, all Settings sections, app search, calendar, job filters, Tasks access, and Inbox access. Each job card button (Schedule, Queue, Email, SMS, Forms, Allocate) can be shown/hidden per role.

---

## 20. Email Inbox — email-to-job conversion with threading

The Email Inbox provides a unique email address per account. Emails sent to this address arrive in the ServiceM8 Inbox, ready to be **converted to jobs** (all information and attachments auto-populate the job card) or **attached to existing jobs**. An **auto-fill feature** recognizes Field Codes in incoming emails (keywords followed by colons) for automatic population. **Work Order Scanning** automatically extracts key details from PDF work order attachments (common from property managers).

Two-Way Email threading means customer replies to ServiceM8-sent emails appear in the relevant Job Diary. Staff replies to forwarded customer emails are added to the Diary and forwarded to the customer.

---

## 21. API capabilities — REST endpoints, webhooks, and OAuth

The ServiceM8 REST API operates at `https://api.servicem8.com/api_1.0/` with plain JSON over HTTP. **Two authentication methods** exist: **API Keys** (for private/single-account integration, generated at Settings > API Keys, passed via `X-API-Key` header) and **OAuth 2.0** (for public applications, with authorization code grant, 1-hour access tokens, and refresh token support).

**Rate limits are 180 requests/minute and 20,000 requests/day** per add-on per account. The API provides full CRUD operations on **30+ endpoints** including Jobs (`/job.json`), Companies/Clients (`/company.json`), Materials (`/material.json`), Job Materials (`/jobmaterial.json`), Job Activities/Bookings (`/jobactivity.json`), Staff (`/staff.json`), Forms (`/form.json`), Form Fields (`/formfield.json`), Form Responses (`/formresponse.json`), Assets (`/asset.json`), Badges (`/badge.json`), Categories (`/category.json`), Queues, Attachments, Notes, Tasks, Feedback, Knowledge Articles, Email/SMS Templates, and more.

**Key API naming conventions**: Clients = Company, Line items = JobMaterial, Scheduled Bookings = JobActivity (where `activity_was_scheduled == 1`), Check-in time = JobActivity (where `activity_was_scheduled == 0`), Quotes/Invoices/Photos in diary = Attachment.

**Two webhook types exist.** Object Webhooks subscribe to field-level changes on specific object types (Job, JobActivity, JobPayment, Note, Task, Material, Company, Attachment, Form Response) — callbacks receive the UUID and changed fields but not full data (requiring a follow-up GET). Event Webhooks subscribe to business events like `job.created` or `job.completed`. The **Add-on SDK** supports serverless (AWS Lambda) and web-hosted add-ons with action events (button clicks in Job/Client Cards) and webhook events.

---

## 22. External Calendars — one-way sync in both directions

**Two separate add-ons handle calendar integration.** The External Calendars add-on exports ServiceM8 scheduled bookings to Google Calendar, Apple iCal, or Outlook via an **iCal URL per staff member** — this is **one-way, read-only** in the external calendar with periodic sync (not real-time, delays can occur). The Calendar Import add-on imports **busy/available times** from external calendars (Google, Office 365, iCal-compatible) and displays them as "Busy" blocks on the ServiceM8 Dispatch Board — also one-way, periodic sync. **Zapier integration** provides near-real-time bidirectional workflows between ServiceM8 and Google Calendar.

---

## 23. The Dispatch Board — central operational command

The Dispatch Board is the operational center where office staff spend **90% of their time**. The **Staff Schedules** view displays a **Gantt-style horizontal timeline** per staff member with scheduled bookings as blocks. Views switch between **Day, Week, 2 Weeks, and Month** formats with navigation arrows and a "Today" button.

**Drag-and-drop scheduling** works by dragging jobs from the left-hand Jobs list onto a staff member's timeline. Drag block edges to adjust duration. Double-click to edit. Multi-staff bookings are supported — after initial scheduling, add more staff and drag to move all attached bookings simultaneously. ServiceM8 learns **"Suggested Teams"** based on frequent booking patterns. Hold SHIFT to move only one staff member's booking.

The **Dispatch Map** shows all jobs and staff locations in real time (when staff are clocked on with GPS). A **green navigation line** connects staff to their target job while navigating. The map is crucial for **urgent dispatch** — finding the nearest clocked-on staff member to a job site. **Track My Arrival** sends clients a live map portal link via SMS so they can watch the technician approaching in real time.

**Standard job list filters** include All Jobs, Completed Jobs (visible for 48 hours), In Progress, and Unscheduled. Custom filters can be created. **Status dots** provide visual coding: **blue** = scheduled and unread, **red** = staff needs to review (job not completed after appointment), **yellow** = job in queue or expired from queue.

---

## 24. Recurring Jobs — automatic job creation on schedule

**Two mechanisms exist.** Simple Recurring Jobs auto-recreate a job when completed, scheduling to the same staff at the same time. The more advanced **Recurring Jobs & Reminders** are created from the Dispatch Board's "New Recurring Job" button, requiring a Job Template or Service as the basis.

Future recurring bookings start as **inactive/TBC** (shown yellow), auto-activating a configurable timeframe before the recurrence date (default 1 week, max 12 weeks). On activation, a new job card is created with a unique number. **Three recurring types**: Auto-scheduled (fixed time), Auto-allocated (flexible booking window), and Reminder (arrives in Inbox for manual confirmation). The **Recurring Jobs Auto-Routing add-on** optimizes routes for recurring Services jobs.

---

## 25. Job card header buttons and the checkout workflow

### Job card toolbar buttons

**Schedule** opens the Add Booking window with smart booking suggestions that dynamically account for staff schedules, leave, and travel time. Two modes: schedule directly or generate a **Booking Link** for clients to choose their own time. **Queue** places the job on hold with an expiry timeframe. **Email** opens composition with auto-filled client address, template selection, merge field population, and document attachment capability. **SMS** opens messaging with template selection, attachment support, and automatic Two-Way SMS reply links. **Form** dropdown shows available forms linked via badges — checklist items for mandatory/optional completion. **Service** applies a Service to the job, stepping through the configured question set to determine pricing and scheduling. **Proposal** opens the WYSIWYG proposal builder. **More** dropdown includes Print Work Order/Invoice/Quote and access to additional actions. On mobile, the **Job Actions bar** is customizable — staff choose which actions appear via Edit Actions.

### Checkout and completion workflow

The mobile **Checkout Wizard** flow is: Check Out > Job Complete > optional diary notes > Activity Feed sharing. The wizard uses **Smart Labour timer** for time tracking and can collect a **client signature**. Job status changes to Completed.

The online dashboard's **Billing Workflow dropdown** (top-right of Billing tab) provides: **Complete** (changes status to Completed), **Auto Invoice** (AI analyzes job card, diary, photos, and similar past jobs to draft Work Completed description and materials list — requires ~100+ completed jobs for best results), **Email Invoice** (generates PDF with pre-drafted email), **SMS Invoice** (sends via text), **Customise Invoice** (change invoice date/settings), **Add Payment**, **Partial/Progress Invoice** (creates job clones like #123A, #123B with auto-deducted amounts), and **Save to Diary** (save without sending).

### Invoice approval workflow

Completed jobs land in the **Invoicing page > Awaiting Approval** tab. Office staff review pricing, add missing materials, verify amounts, then **Approve** — which syncs the invoice to the connected accounting package (Xero/MYOB/QuickBooks). Multiple jobs can be batch-approved. After approval, jobs move to **Awaiting Payment** (for issuing invoices and tracking balances, with batch email capability) and then to **Paid** (shown for two weeks before archiving).

### Payment collection

Options include **Stripe** (enter card number, Scan & Pay with Apple Pay/Google Pay, Tap to Pay on iPhone), **external EFTPOS** (record manually), **Cash/Cheque/EFT**, **online card payment** (client pays via emailed link), and **ServiceM8 Pay** (automated deposits on quote acceptance, automatic recurring payments).

---

## Job status workflow — the four immutable states

ServiceM8 enforces exactly **four non-customizable statuses**: **Quote** (needs quoting or awaiting quote approval), **Work Order** (client has approved, work can proceed), **Completed** (all work finished, ready for invoicing), and **Unsuccessful** (cancelled/rejected). The standard flow runs: Job Created → Quote → send quote → queue as "Waiting on Client" → client accepts → Work Order → schedule/allocate → technician navigates (ETA sent) → check in → complete work/forms → check out → Completed → Awaiting Approval → Approve → Awaiting Payment → Paid → Archived.

Status changes drive automations: Quote sent triggers Quote Follow Up; booking creation triggers Booking Confirmation and Booking Reminder; Work Order → Completed triggers invoicing workflow; invoice payment triggers Feedback Request; overdue payment triggers Payment Follow Up; job completion with badge triggers Badge Follow Up; "Navigate to Job" triggers ETA notification and Track My Arrival.

Queues and Job Categories serve as the recommended mechanisms for adding workflow granularity beyond these four statuses — queues for process stages ("waiting for parts," "pending approval") and categories for job classification ("emergency," "maintenance," "warranty").

---

## Conclusion: architectural patterns for Rollo Command Center

ServiceM8's architecture reveals several key patterns essential for faithful reproduction. The **badge system** is the universal connector — badges link forms to jobs, trigger automations, gate asset access, and create recurring job reminders. **Job Queues with expiry dates** serve as the extensible workflow engine compensating for the fixed four-status model. The **Dispatch Board** functions as a unified command center combining Gantt scheduling, real-time GPS tracking, queue management, and drag-and-drop allocation. The **Forms engine** is the compliance backbone with mandatory enforcement, conditional logic, PDF generation, and version history. The **API surface** exposes 30+ REST endpoints with both field-level and event-level webhooks, providing comprehensive programmatic access to every data entity. Understanding these interconnections — particularly how badges, templates, automations, and the checkout workflow chain together — is critical for building a specification that captures ServiceM8's full operational depth.