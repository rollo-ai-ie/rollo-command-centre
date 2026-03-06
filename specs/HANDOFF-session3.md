# ROLLO COMMAND CENTER — SESSION HANDOFF

**Date:** 5 March 2026 (Session 3)
**Build status:** PASSING — 20/20 pages, zero TypeScript errors
**Dev server:** `npm run dev` on port 3000

---

## 1. WHAT THIS PROJECT IS

Rollo is the operations command center for **24 Hour Plumber** (Stronge Homes Ltd). It is a full SaaS dashboard built in Next.js that sits alongside ServiceM8 (the current system of record). The owner is Trevor Stronge. Trevor has dyslexia — use short sentences, bullet points, plain language.

**Tech stack:** Next.js 14.2.35, TypeScript strict, Tailwind CSS v4, shadcn/ui, Lucide React icons (no emojis), dark theme only. No state library — everything is local `useState`. No database connected yet — all data comes from `data/sample-data.ts`.

---

## 2. WHAT HAS BEEN BUILT (COMPLETE)

### All 16 tabs — fully rendered with sample data

| Route | Page | Key Components |
|-------|------|----------------|
| `/control-room` | Command center | COSBABriefing, StatCards, EngineerStatusBoard, ApprovalQueue, KPIDashboard, BlackHoleTracker |
| `/jobs` | Job management | JobKanban, JobList, JobCalendar, JobDetailPanel (slide-over), JobCard (draggable) |
| `/dispatch` | Schedule + routing | DispatchGrid (drag-to-move, drag-to-resize, click-to-place), DispatchList, DispatchMap (placeholder), QueueBar |
| `/comms` | Unified inbox | CommsInbox with Done/Escalate/+Job buttons |
| `/customers` | CRM | CustomerTable, CustomerCards, CustomerDetailPanel (7-tab slide-over) |
| `/finance` | Invoices + quotes | FinanceOverview, InvoiceTable (with sub-tab filters), QuoteTable |
| `/agents` | 12 AI sub-agents | AgentGrid with toggle switches |
| `/fleet` | Van tracking | FleetOverview, VanDetailPanel (slide-over) |
| `/hr` | Hiring + certs | HROverview with Kanban pipeline |
| `/marketing` | Ads + weather | MarketingOverview with weather trigger approve/reject |
| `/plans` | Memberships | PlansOverview — Care/Priority/Protect tiers |
| `/guarantee` | On-time guarantee | GuaranteeOverview with claim approve/reject |
| `/security` | 8 hard rules | SecurityOverview |
| `/roadmap` | 90-day plan | RoadmapOverview with checkboxes |
| `/reports` | Charts placeholder | ReportsOverview |
| `/settings` | Config + killswitch | SettingsOverview with manual fallback toggle |

### Interactivity (all working)

- **ToastProvider** — bottom-right toast notifications (auto-dismiss 5s, 4 types)
- **JobDetailPanel** — slide-over with 3 tabs (Details, Billing, Activity). Checklist toggle/add/remove, materials/labour add/remove with live totals, payment recording, status dropdown, editable description/notes/PO number. Item codes with catalogue autocomplete. Job Metrics line (Job Time, Admin Time, Est. Profit).
- **NewJobModal** — centred modal with full form, customer autocomplete, generates job numbers
- **NewJobContext** — global context so TopBar and Comms can both trigger "+ New Job"
- **TopBar** — bell icon toggles notification dropdown, Guarantee routes to /guarantee, Engineer App shows info modal, "+ New Job" opens NewJobModal
- **Comms** — Done/Escalate/+Job buttons all work, row click expands detail
- **Control Room** — Approve/Reject in ApprovalQueue (removes item + toast), engineer status dropdown updates, stat cards clickable (route to relevant tabs), BlackHoleTracker "Mark Handled" button
- **Dispatch** — DispatchGrid: drag job blocks to move, drag edges to resize, click empty slot to place unscheduled job, click job block opens JobDetailPanel. QueueBar with 6 expandable queues
- **Finance** — Invoice Send/Mark Paid/View buttons, Quote Send/Accept/Reject buttons. Invoice sub-tab filter pills (All, Awaiting Approval, Awaiting Payment, Paid, Overdue) with badge counts. "Completed By" column shows engineer name.
- **Fleet** — Van cards/rows clickable, opens VanDetailPanel (editable mileage, CVRT/insurance/tax countdowns, AdBlue status)
- **Agents** — Toggle switches work, "View Log" opens action history modal
- **HR** — Candidate cards clickable, opens detail modal
- **Marketing** — Weather trigger Approve/Reject buttons update state + toast
- **Plans** — "+ Add Subscriber" opens modal with customer select + plan tier
- **Guarantee** — Approve/Reject buttons update state + toast
- **Settings** — Killswitch toggle works, integration toggles work
- **Customers** — Jobs tab in CustomerDetailPanel: clicking a job opens nested JobDetailPanel. Client badges (VIP, Repeat, New, Service Due) shown in both table and card views.

### ServiceM8-Inspired Improvements (ALL 10 COMPLETED)

**Session 2 (5 improvements):**
1. **Job Queue System** — 6 queue pills at top of DispatchGrid (Customer Requires, Jobs to Quote, Order Parts, Pending Quotes, Waiting on Client, Waiting on Parts). Each has badge count and expands to show items.
2. **Colour-coded Activity Timeline** — 8 entry types with unique dot colours and icons: note (amber), booking (red), photo (green), status_change (blue), payment (emerald), quote (indigo), enquiry (cyan), system (grey).
3. **PO Number field** — Editable monospaced input in Job Detail > Details tab.
4. **Dispatch Map View** — Third view option (Grid | List | Map). Shows placeholder Eircode coverage map with simulated county zones and engineer pins.
5. **"Same as job address" checkbox** — In Billing tab (confirmed working).

**Session 3 (5 improvements):**
6. **Item Codes to Billing** — Code column in materials table, "Search or add new item..." autocomplete dropdown that searches a 32-item catalogue by code or name, auto-fills code/name/price.
7. **Estimated Profit on Billing** — Job Metrics line below totals showing Job Time, Admin Time, Est. Profit in green.
8. **Invoice Sub-tab Filters** — Filter pills (All, Awaiting Approval, Awaiting Payment, Paid, Overdue) with badge counts above the invoice table.
9. **Completed By on Invoice Table** — New column with User icon showing which engineer completed the job.
10. **Client Badges** — VIP (gold star, lifetime spend >= 3000), Repeat (teal, 8+ jobs), New (blue, 1 job), Service Due (red, 60+ days since contact). Shown in CustomerTable and CustomerCards. Derived from existing data — no new fields needed.

### Bug Fixes (Session 3)

- **Hydration mismatch fix** — COSBABriefing was rendering `new Date()` on both server and client, causing time mismatches (e.g. "16:41" vs "16:42"). Fixed by deferring date/time rendering until after mount using `useState`/`useEffect`.

---

## 3. WHAT IS BROKEN

**Nothing is broken.** Build passes with zero errors. All 20 routes compile. Zero console errors.

Known limitations (not bugs):
- All data is local state from `sample-data.ts`. No persistence. Refresh resets everything.
- DispatchMap is a visual placeholder — no real Google Maps integration yet.
- Photos section in Job Detail is a placeholder grid (no upload functionality).
- PDF cert auto-extraction is not built yet (mentioned in spec).
- No Supabase, Stripe, or Twilio connections yet.
- Reports page has placeholder charts only.
- Calendar view in Jobs has no navigation arrows (only Month/Week/Day toggle and Today button).
- New Job dialog dropdowns (Division, Job Type, Area, Engineer) use native `<select>` — functional but could be upgraded to shadcn Select for consistency.

---

## 4. FILE MAP

### Core files

| File | Lines | Purpose |
|------|-------|---------|
| `lib/types.ts` | ~530 | All TypeScript interfaces and union types (includes CatalogueItem) |
| `lib/utils.ts` | 39 | formatCurrency, formatPhone, timeAgo, cn |
| `lib/constants.ts` | ~60 | Colour maps, division data |
| `data/sample-data.ts` | ~1400 | All mock data — engineers, jobs, customers, queues, itemCatalogue, etc. |
| `hooks/useViewPreference.ts` | 36 | Persist view mode per tab in localStorage |

### Layout

| File | Purpose |
|------|---------|
| `app/layout.tsx` | Root layout — wraps with ToastProvider + NewJobProvider |
| `components/layout/Sidebar.tsx` | Collapsible sidebar (desktop) / bottom tab bar (mobile) |
| `components/layout/TopBar.tsx` | Search + bell + Guarantee + Engineer App + New Job buttons |
| `components/layout/PageHeader.tsx` | Reusable page header with title + icon + action buttons |

### Shared components

| File | Purpose |
|------|---------|
| `components/shared/ToastProvider.tsx` | Toast notification context + bottom-right toast stack |
| `components/shared/NewJobContext.tsx` | Global context for "+ New Job" modal |
| `components/shared/StatCard.tsx` | Reusable stat card with accent bar |
| `components/shared/ViewToggle.tsx` | Switch between view modes |

### Big components (the ones you will touch most)

| File | Lines | Purpose |
|------|-------|---------|
| `components/dispatch/DispatchGrid.tsx` | ~1208 | Full schedule grid with drag-and-drop + QueueBar |
| `components/jobs/JobDetailPanel.tsx` | ~1150 | ServiceM8-style job card slide-over (Details/Billing/Activity) with item codes + catalogue |
| `components/jobs/NewJobModal.tsx` | ~500 | Create new job form modal |
| `components/customers/CustomerDetailPanel.tsx` | ~600 | 7-tab customer slide-over panel |
| `components/customers/CustomerTable.tsx` | ~350 | CRM table with client badges |
| `components/customers/CustomerCards.tsx` | ~250 | CRM card grid with client badges |
| `components/finance/InvoiceTable.tsx` | ~300 | Invoice table with sub-tab filter pills + Completed By |
| `components/fleet/VanDetailPanel.tsx` | ~500 | Van detail slide-over |
| `components/dispatch/DispatchMap.tsx` | 164 | Eircode map placeholder |
| `components/control-room/COSBABriefing.tsx` | 115 | Daily briefing (hydration-safe) |

### All page files (16 tabs + root)

All at `app/[tab]/page.tsx`. Each imports its tab-specific components and manages local state.

---

## 5. KEY ARCHITECTURE PATTERNS

- **Slide-over panels** — Right-side panels for detail views (JobDetailPanel, CustomerDetailPanel, VanDetailPanel). Pattern: fixed z-50, backdrop with blur, translate-x animation, body scroll lock, internal tabs.
- **Callbacks flow upward** — Children call prop functions, pages own the state.
- **Two React contexts at layout level** — `NewJobContext` (opens new job modal from anywhere) + `ToastContext` (shows toast notifications from anywhere).
- **View persistence** — `useViewPreference` hook saves view mode (kanban/list/calendar) per tab in localStorage.
- **Irish data only** — Euro, Irish phone format (083/085/086/087), Eircode postcodes, Irish names and areas.
- **No emojis** — Lucide React icons everywhere. This is a hard rule.
- **Dark theme only** — bg `#09090B`, surface `#111114`, elevated `#18181B`.
- **@dnd-kit** — Used for drag-and-drop in DispatchGrid and JobKanban.
- **Client badges are derived** — VIP/Repeat/New/Service Due badges are computed from existing customer data (lifetimeSpend, jobCount, lastContact). No new data fields required.
- **Hydration safety** — Any component rendering `new Date()` must defer to client-side only using `mounted` state pattern.

---

## 6. SCREENSHOT DOCUMENTATION

**Folder:** `~/Desktop/Rollo Command Centre - Jobs Pictures/`
**Count:** 75 PNG screenshots
**Created:** 5 March 2026

Covers every interactive element on the Jobs tab:
- 01-02: Kanban view (full + scrolled right)
- 03-47: 9 job detail panels (Details, Billing, Activity tabs each)
- 48-50: List view (full, scrolled, job detail open)
- 51-55: List view sorted by each column
- 56-59: Calendar view (Month, Week, Day, Today)
- 60-61: Dispatch page (from Jobs button)
- 62-65: New Job dialog (empty, fields filled, fully filled, dropdowns set)
- 66-69: Search bar (focused, "Colm Murphy", "boiler", job number)
- 70-73: Mobile 375px (Kanban, List, Calendar, New Job)
- 74-75: Tablet 768px (Kanban, List)

These screenshots are for review in Claude Chat to identify missing features or issues.

---

## 7. REFERENCE DOCUMENTS

| File | What it contains |
|------|-----------------|
| `CLAUDE.md` | Build rules, tech stack, architecture, non-negotiable rules |
| `docs/ROLLO-SPEC.md` | Full 17-section specification — tab-by-tab UI spec, design system, data models, business rules |
| `docs/SERVICEM8-ANALYSIS.md` | ServiceM8 UI analysis with 13 prioritised improvements (10 done, 3 LOW remaining) |
| `docs/GITHUB-REPO-RESEARCH.md` | Research on 20 GitHub repos for accelerating the build |
| `~/Desktop/24hp-coverage-map.html` | Source HTML for the Eircode coverage map (to be integrated into DispatchMap) |

---

## 8. WHAT TO DO NEXT (PRIORITY ORDER)

### From ServiceM8 analysis — 3 remaining (all LOW priority)

| # | Improvement | Priority | Notes |
|---|------------|----------|-------|
| 11 | Materials & Services catalogue page | LOW | Full searchable catalogue of items with codes. Data exists in `itemCatalogue` (32 items in sample-data.ts). Needs a UI page or sub-tab. |
| 12 | Job Templates in Settings | LOW | Templates for common job types (boiler service, gas cert, etc.) to pre-fill new job forms. |
| 13 | SMS/Email Templates in Settings | LOW | Template management for Comms tab messages. |

### Trevor's review process (IN PROGRESS)

Trevor is reviewing each tab systematically using Claude Chat + screenshot folders:
- **Jobs tab** — 75 screenshots captured, ready for review
- **Dispatch tab** — next in queue
- **Comms tab** — after Dispatch
- Continue through all 16 tabs in sidebar order

For each remaining tab, create a screenshot folder on Desktop:
```
~/Desktop/Rollo Command Centre - [Tab Name] Pictures/
```

### From the spec — features not yet built

| Feature | Where | Notes |
|---------|-------|-------|
| Real Eircode coverage map | DispatchMap.tsx | Parse `~/Desktop/24hp-coverage-map.html`, integrate Google Maps API |
| PDF cert auto-extraction | HR > Certs tab | Upload PDF, parse with pdf-parse, auto-extract cert holder/number/expiry |
| Photo upload in Job Detail | JobDetailPanel DetailsTab | Currently a placeholder grid — needs file picker + preview |
| Supabase connection | Everywhere | Replace sample data with real database |
| Stripe integration | Finance | Pay-by-link, Text-to-Pay, pre-auth deposits |
| Twilio SMS | Comms | DPC-compliant marketing SMS (NOT through ServiceM8) |
| Charts in Reports | ReportsOverview | Recharts for daily/weekly/monthly reporting |
| Calendar navigation | Jobs Calendar | Add prev/next arrows for navigating between months/weeks |

### Quick wins Trevor might ask for

- Make specific buttons do something new (he tests on his phone)
- Add more sample data for specific scenarios
- Adjust colours or spacing on specific cards
- Add a new field to a form or table

---

## 9. HOW TO START A NEW SESSION

```bash
cd ~/Desktop/rollo-command-center
npm run dev          # Start dev server on port 3000
npm run build        # Verify zero errors (do this after every change)
```

Read these files first:
1. `HANDOFF.md` (this file) — current state
2. `CLAUDE.md` — build rules and non-negotiable constraints
3. `docs/SERVICEM8-ANALYSIS.md` — if continuing SM8 improvements
4. `docs/ROLLO-SPEC.md` — if building new features (read the relevant tab section)

If the dev server shows a stale cache error:
```bash
rm -rf .next
npm run dev
```

To create screenshot folders for other tabs (reusable Playwright pattern):
```bash
# Install if needed: npm install --save-dev playwright
# See previous scripts pattern in git history or ask Claude Code to generate
```

---

## 10. IMPORTANT CONTEXT

- **ServiceM8 is still the system of record.** Rollo sits alongside it. Never break the existing SM8 workflow.
- **Trevor has dyslexia.** Short sentences. Bullet points. Plain language. No jargon.
- **This is a live business.** 7 engineers, 12,500+ customers, 5 counties. Every feature maps to a real daily workflow.
- **Quality bar:** If a screen would not look credible as a real SaaS product demo, it is not finished.
- **The 8 Hard Rules are sacred.** See `/security` tab and `docs/ROLLO-SPEC.md` section 14.
- **No git repo initialised.** Files are just on the Desktop. No version control.
- **Playwright is installed** as a dev dependency for automated screenshots.

---

*Handoff updated 5 March 2026 — Rollo Command Center v1.1 (Session 3)*
