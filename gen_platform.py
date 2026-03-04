#!/usr/bin/env python3
"""Generate platform-v2.html - complete enhanced version"""

import os

OUT = '/Users/openclaw/.openclaw/workspace/rollo-platform/platform-v2.html'

# ── HTML is built as list of strings then joined ──────────────────────────────
parts = []
def w(*args):
    parts.append(''.join(str(a) for a in args))

# ─── HEAD + CSS ───────────────────────────────────────────────────────────────
w("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rollo Business OS v2</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,'SF Pro Display','Helvetica Neue',Arial,sans-serif;background:#F2F2F7;color:#000;font-size:14px;display:flex;min-height:100vh;overflow-x:hidden}
:root{--primary:#007AFF;--success:#34C759;--warning:#FF9500;--danger:#FF3B30;--purple:#AF52DE}
#fallback-banner{display:none;position:fixed;top:0;left:0;right:0;z-index:9999;background:#FF3B30;color:#fff;text-align:center;padding:10px;font-weight:600;font-size:14px}
body.fallback-mode #fallback-banner{display:block}
body.fallback-mode #sidebar,body.fallback-mode #main{margin-top:40px}
/* SIDEBAR */
#sidebar{width:220px;min-width:220px;background:#fff;border-right:1px solid #E5E5EA;display:flex;flex-direction:column;position:fixed;top:0;left:0;bottom:0;z-index:100;overflow-y:auto}
.sidebar-logo{padding:20px 16px 12px;border-bottom:1px solid #E5E5EA}
.sidebar-logo-name{font-size:18px;font-weight:700;color:#000;letter-spacing:-0.5px}
.sidebar-logo-sub{font-size:11px;color:#6C6C70;margin-top:1px}
.sidebar-nav{flex:1;padding:8px}
.nav-item{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:8px;cursor:pointer;font-size:14px;font-weight:400;color:#000;transition:background 0.15s;margin-bottom:1px;user-select:none}
.nav-item:hover{background:#F2F2F7}
.nav-item.active{background:#007AFF;color:#fff}
.nav-item svg{width:16px;height:16px;stroke:#6C6C70;fill:none;stroke-width:1.8;flex-shrink:0}
.nav-item.active svg{stroke:#fff}
.sidebar-footer{padding:12px 16px;border-top:1px solid #E5E5EA;font-size:11px;color:#AEAEB2}
/* MAIN */
#main{margin-left:220px;flex:1;display:flex;flex-direction:column;min-height:100vh}
#topbar{background:#fff;border-bottom:1px solid #E5E5EA;padding:12px 24px;display:flex;align-items:center;gap:12px;position:sticky;top:0;z-index:90}
#page-title{font-size:17px;font-weight:600;color:#000;white-space:nowrap}
#search-box{flex:1;max-width:360px;margin:0 auto;position:relative}
#search-box input{width:100%;padding:7px 12px 7px 32px;border:1px solid #E5E5EA;border-radius:8px;font-size:14px;background:#F2F2F7;outline:none;font-family:inherit}
#search-box svg{position:absolute;left:8px;top:50%;transform:translateY(-50%);width:16px;height:16px;stroke:#AEAEB2;fill:none;stroke-width:2}
#topbar-actions{display:flex;align-items:center;gap:8px;margin-left:auto}
.content{padding:24px;flex:1}
.section{display:none}
.section.active{display:block}
/* CARDS */
.card{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:20px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.card-sm{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:14px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.card-title{font-size:15px;font-weight:600;color:#000;margin-bottom:12px}
/* GRID */
.grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.grid-auto{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
/* STATS */
.stat-card{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:16px 18px;box-shadow:0 1px 3px rgba(0,0,0,.08);position:relative;cursor:pointer;transition:box-shadow .15s}
.stat-card:hover{box-shadow:0 3px 8px rgba(0,0,0,.12)}
.stat-card .stat-icon{position:absolute;top:14px;right:14px;width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center}
.stat-card .stat-icon svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2}
.stat-card .stat-num{font-size:28px;font-weight:700;color:#000;line-height:1;margin-top:4px}
.stat-card .stat-label{font-size:12px;color:#6C6C70;margin-top:4px}
.stat-card .stat-trend{font-size:11px;margin-top:6px}
.trend-up{color:#34C759}.trend-down{color:#FF3B30}.trend-flat{color:#AEAEB2}
/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:8px;font-size:14px;font-weight:500;cursor:pointer;border:none;font-family:inherit;transition:opacity .15s;white-space:nowrap}
.btn:hover{opacity:.85}
.btn svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2}
.btn-primary{background:#007AFF;color:#fff}
.btn-secondary{background:#fff;color:#007AFF;border:1px solid #007AFF}
.btn-danger{background:#FF3B30;color:#fff}
.btn-success{background:#34C759;color:#fff}
.btn-ghost{background:transparent;color:#007AFF;padding:6px 10px}
.btn-sm{padding:5px 10px;font-size:12px}
/* TABS */
.tabs{display:flex;gap:4px;margin-bottom:16px;background:#F2F2F7;border-radius:10px;padding:3px;width:fit-content}
.tab{padding:6px 14px;border-radius:7px;font-size:13px;font-weight:500;cursor:pointer;color:#6C6C70;transition:all .15s;white-space:nowrap}
.tab.active{background:#fff;color:#000;box-shadow:0 1px 3px rgba(0,0,0,.1)}
/* TABLES */
.table-wrap{overflow-x:auto;border-radius:12px;border:1px solid #E5E5EA}
table{width:100%;border-collapse:collapse;background:#fff}
thead th{padding:10px 14px;text-align:left;font-size:12px;font-weight:600;color:#6C6C70;border-bottom:1px solid #E5E5EA;background:#F9F9FB;white-space:nowrap;cursor:pointer}
tbody td{padding:10px 14px;font-size:13px;border-bottom:1px solid #F2F2F7;vertical-align:middle}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:#F9F9FB}
/* BADGES */
.badge{display:inline-flex;align-items:center;padding:3px 8px;border-radius:20px;font-size:11px;font-weight:600;white-space:nowrap}
.badge-blue{background:#EBF4FF;color:#007AFF}
.badge-green{background:#E8FAF0;color:#34C759}
.badge-orange{background:#FFF4E5;color:#FF9500}
.badge-red{background:#FFEBEB;color:#FF3B30}
.badge-purple{background:#F5EEFF;color:#AF52DE}
.badge-grey{background:#F2F2F7;color:#6C6C70}
/* STATUS PILLS */
.status-pill{display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:600}
.status-pill::before{content:'';width:6px;height:6px;border-radius:50%;flex-shrink:0}
.pill-green{background:#E8FAF0;color:#34C759}.pill-green::before{background:#34C759}
.pill-orange{background:#FFF4E5;color:#FF9500}.pill-orange::before{background:#FF9500}
.pill-red{background:#FFEBEB;color:#FF3B30}.pill-red::before{background:#FF3B30}
.pill-blue{background:#EBF4FF;color:#007AFF}.pill-blue::before{background:#007AFF}
.pill-grey{background:#F2F2F7;color:#6C6C70}.pill-grey::before{background:#AEAEB2}
/* AVATARS */
.eng-avatar{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;flex-shrink:0}
.eng-avatar-sm{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff;flex-shrink:0}
/* MODALS */
#modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:200;align-items:center;justify-content:center}
#modal-overlay.show{display:flex}
.modal{background:#fff;border-radius:16px;padding:24px;max-width:640px;width:92%;max-height:90vh;overflow-y:auto;position:relative}
.modal-title{font-size:17px;font-weight:600;margin-bottom:20px}
.modal-close{position:absolute;top:16px;right:16px;background:none;border:none;font-size:22px;cursor:pointer;color:#6C6C70;line-height:1;padding:4px}
/* SLIDE-OVER */
#slideover-backdrop{display:none;position:fixed;inset:0;background:rgba(0,0,0,.3);z-index:149;backdrop-filter:blur(2px)}
#slideover-backdrop.show{display:block}
#slideover{position:fixed;top:0;right:-1200px;width:480px;height:100vh;background:#fff;box-shadow:-4px 0 24px rgba(0,0,0,.12);z-index:150;transition:right .3s ease;display:flex;flex-direction:column}
#slideover.open{right:0}
#slideover.wide{width:980px;max-width:96vw}
.slideover-header{padding:14px 20px;border-bottom:1px solid #E5E5EA;display:flex;align-items:center;justify-content:space-between;background:#F9F9FB;flex-shrink:0}
.slideover-title{font-size:17px;font-weight:600;flex:1;min-width:0}
.slideover-body{flex:1;overflow-y:auto;padding:20px}
.slideover-body.no-pad{padding:0;overflow:hidden;display:flex;flex-direction:column}
.slideover-close{background:none;border:none;cursor:pointer;padding:6px;border-radius:8px;color:#6C6C70;flex-shrink:0}
.slideover-close:hover{background:#F2F2F7}
.slideover-close svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2}
/* TOAST */
#toast-container{position:fixed;bottom:24px;right:24px;z-index:1000;display:flex;flex-direction:column;gap:8px;pointer-events:none}
.toast{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:12px 16px;font-size:13px;box-shadow:0 4px 16px rgba(0,0,0,.12);display:flex;align-items:center;gap:10px;min-width:280px;pointer-events:all;animation:slideIn .3s ease}
.toast.success .toast-dot{background:#34C759}
.toast.error .toast-dot{background:#FF3B30}
.toast.info .toast-dot{background:#007AFF}
.toast.warning .toast-dot{background:#FF9500}
.toast-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
@keyframes slideIn{from{transform:translateX(100%);opacity:0}to{transform:translateX(0);opacity:1}}
@keyframes fadeOut{from{opacity:1}to{opacity:0}}
/* FORMS */
.form-group{margin-bottom:14px}
.form-label{display:block;font-size:11px;font-weight:600;color:#6C6C70;margin-bottom:5px;text-transform:uppercase;letter-spacing:.3px}
.form-control{width:100%;padding:8px 12px;border:1px solid #E5E5EA;border-radius:8px;font-size:14px;font-family:inherit;outline:none;transition:border-color .15s}
.form-control:focus{border-color:#007AFF;box-shadow:0 0 0 3px rgba(0,122,255,.12)}
select.form-control{background:#fff;cursor:pointer}
textarea.form-control{resize:vertical}
/* TOGGLE */
.toggle{position:relative;display:inline-block;width:44px;height:26px}
.toggle input{display:none}
.toggle-slider{position:absolute;inset:0;background:#E5E5EA;border-radius:13px;cursor:pointer;transition:.2s}
.toggle-slider::before{content:'';position:absolute;width:22px;height:22px;left:2px;top:2px;background:#fff;border-radius:50%;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.toggle input:checked+.toggle-slider{background:#34C759}
.toggle input:checked+.toggle-slider::before{transform:translateX(18px)}
/* CONTROL ROOM */
.cosba-card{background:#fff;border:1px solid #E5E5EA;border-left:4px solid #007AFF;border-radius:12px;padding:20px;margin-bottom:20px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.eng-status-card{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:14px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.approval-queue{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.approval-item{padding:12px 0;border-bottom:1px solid #F2F2F7;display:flex;align-items:center;justify-content:space-between;gap:10px}
.approval-item:last-child{border-bottom:none}
.activity-item{display:flex;align-items:flex-start;gap:12px;padding:10px 0;border-bottom:1px solid #F2F2F7}
.activity-item:last-child{border-bottom:none}
.activity-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:4px}
.bh-item{display:flex;align-items:center;gap:12px;padding:10px;border-radius:8px;background:#F9F9FB;margin-bottom:8px;border:1px solid #E5E5EA}
.bh-item.urgent{border-left:3px solid #FF3B30}
.bh-item.breached{background:#FFEBEB;border-left:3px solid #FF3B30;animation:pulse-red 1.5s infinite}
@keyframes pulse-red{0%,100%{background:#FFEBEB}50%{background:#FFD5D5}}
.escalation-card{padding:12px;border-radius:8px;border:1px solid #E5E5EA;margin-bottom:8px;display:flex;gap:12px;align-items:center}
/* JOBS */
.kanban-board{display:flex;gap:14px;overflow-x:auto;padding-bottom:8px;min-height:500px}
.kanban-col{min-width:220px;flex-shrink:0;background:#F2F2F7;border-radius:12px;padding:12px}
.kanban-col-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.kanban-col-title{font-size:13px;font-weight:600;color:#000}
.kanban-count{background:#E5E5EA;color:#6C6C70;border-radius:12px;padding:2px 8px;font-size:11px;font-weight:600}
.job-card{background:#fff;border:1px solid #E5E5EA;border-radius:10px;padding:12px;margin-bottom:8px;cursor:pointer;transition:box-shadow .15s;user-select:none}
.job-card:hover{box-shadow:0 3px 10px rgba(0,0,0,.1)}
.kanban-col.drag-over{background:#EBF4FF;border:2px dashed #007AFF}
.job-card-num{font-size:11px;color:#AEAEB2;margin-bottom:4px}
.job-card-customer{font-size:13px;font-weight:600;margin-bottom:3px}
.job-card-type{font-size:11px;color:#6C6C70;margin-bottom:8px}
.job-card-footer{display:flex;align-items:center;justify-content:space-between}
/* DISPATCH - ServiceM8 style */
.dispatch-sm-wrap{display:flex;height:700px;border-radius:12px;overflow:hidden;border:1px solid #E5E5EA}
.dq-panel{width:188px;flex-shrink:0;background:#1C1C1E;display:flex;flex-direction:column;overflow-y:auto}
.dq-title{font-size:10px;font-weight:700;color:#636366;padding:14px 12px 6px;text-transform:uppercase;letter-spacing:.5px}
.dq-item{display:flex;align-items:center;padding:9px 10px;margin:2px 6px;border-radius:7px;cursor:pointer;transition:background .15s}
.dq-item:hover{background:rgba(255,255,255,.08)}
.dq-item.active{background:#007AFF}
.dq-emoji{font-size:14px;flex-shrink:0;width:22px}
.dq-label{font-size:12px;color:#fff;flex:1;margin-left:6px}
.dq-count{font-size:10px;font-weight:700;background:rgba(255,255,255,.2);color:#fff;border-radius:10px;padding:1px 7px}
.dm-panel{flex:1;display:flex;flex-direction:column;overflow:hidden;background:#fff}
.dm-tab-bar{display:flex;border-bottom:1px solid #E5E5EA;background:#F9F9FB;flex-shrink:0}
.dm-tab{padding:10px 14px;font-size:12px;font-weight:500;cursor:pointer;color:#6C6C70;border-bottom:2px solid transparent;transition:all .15s;white-space:nowrap}
.dm-tab.active{color:#007AFF;border-bottom-color:#007AFF;background:#fff}
.dm-eng-row{display:flex;border-bottom:1px solid #E5E5EA;position:sticky;top:0;z-index:10;background:#fff;flex-shrink:0}
.dm-time-hdr{width:52px;flex-shrink:0;border-right:1px solid #E5E5EA;background:#FAFAFA}
.dm-eng-hdr{flex:1;min-width:80px;padding:8px 4px;text-align:center;border-right:1px solid #E5E5EA;font-size:10px}
.dm-eng-av{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;color:#fff;margin:0 auto 3px}
.dm-grid{flex:1;overflow-y:auto}
.dm-row{display:flex}
.dm-time-cell{width:52px;flex-shrink:0;height:52px;border-right:1px solid #E5E5EA;border-bottom:1px solid #F2F2F7;display:flex;align-items:flex-start;justify-content:flex-end;padding:3px 6px 0;font-size:10px;color:#AEAEB2;background:#FAFAFA}
.dm-slot{flex:1;min-width:80px;height:52px;border-right:1px solid #F2F2F7;border-bottom:1px solid #F2F2F7;position:relative;cursor:pointer;transition:background .1s}
.dm-slot:hover{background:#F0F8FF}
.dm-slot.drag-over-cell{background:#EBF4FF;border:1px dashed #007AFF}
.dm-job-block{position:absolute;left:2px;right:2px;border-radius:5px;padding:3px 5px;font-size:9px;font-weight:600;color:#fff;overflow:hidden;cursor:pointer;z-index:5;box-shadow:0 1px 3px rgba(0,0,0,.15)}
.dm-job-block:hover{filter:brightness(.9)}
.dm-job-num{font-size:8px;opacity:.85}
.dm-job-cust{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dm-job-type{font-size:7px;opacity:.8;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dr-panel{width:220px;flex-shrink:0;background:#F9F9FB;border-left:1px solid #E5E5EA;display:flex;flex-direction:column}
.dr-search{padding:8px;border-bottom:1px solid #E5E5EA;flex-shrink:0}
.dr-search input{width:100%;padding:6px 10px;border:1px solid #E5E5EA;border-radius:8px;font-size:12px;background:#fff;outline:none;font-family:inherit}
.dr-list{flex:1;overflow-y:auto;padding:6px}
.dr-group-lbl{font-size:9px;font-weight:700;color:#AEAEB2;text-transform:uppercase;letter-spacing:.5px;padding:6px 4px 3px}
.dr-item{background:#fff;border:1px solid #E5E5EA;border-radius:7px;padding:7px;margin-bottom:5px;cursor:pointer;display:flex;align-items:flex-start;gap:6px}
.dr-item:hover{box-shadow:0 2px 6px rgba(0,0,0,.08)}
/* JOB PANEL ServiceM8 style */
.jp-icon-nav{width:44px;background:#1C1C1E;display:flex;flex-direction:column;align-items:center;padding:12px 0;gap:6px;flex-shrink:0}
.jp-icon-tab{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#636366;transition:all .15s}
.jp-icon-tab:hover{background:rgba(255,255,255,.08)}
.jp-icon-tab.active{background:#007AFF;color:#fff}
.jp-icon-tab svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.8}
.jp-action-bar{display:flex;gap:3px;padding:8px 10px;border-bottom:1px solid #E5E5EA;background:#F9F9FB;flex-wrap:wrap;flex-shrink:0}
.jp-btn{display:inline-flex;align-items:center;gap:4px;padding:5px 9px;border-radius:6px;font-size:11px;font-weight:500;cursor:pointer;border:1px solid #E5E5EA;background:#fff;color:#000;transition:background .1s;font-family:inherit;white-space:nowrap}
.jp-btn:hover{background:#F2F2F7}
.jp-btn svg{width:12px;height:12px;stroke:currentColor;fill:none;stroke-width:2}
.jp-two-col{display:flex;flex:1;overflow:hidden}
.jp-form-col{flex:0 0 55%;border-right:1px solid #E5E5EA;overflow-y:auto;padding:14px}
.jp-diary-col{flex:1;background:#F9F9FB;overflow-y:auto;padding:14px}
.diary-note-row{display:flex;gap:6px;margin-bottom:14px}
.diary-note-row input{flex:1;padding:7px 10px;border:1px solid #E5E5EA;border-radius:8px;font-size:12px;background:#fff;outline:none;font-family:inherit}
.diary-entry{display:flex;gap:10px;padding:10px 0;border-bottom:1px solid #E5E5EA}
.diary-entry:last-child{border-bottom:none}
.diary-icon-box{width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:14px}
.diary-body-wrap{flex:1}
.diary-title{font-size:12px;font-weight:600;color:#000}
.diary-meta{font-size:10px;color:#AEAEB2;margin-top:1px}
.diary-bubble{font-size:11px;color:#3C3C43;margin-top:5px;background:#fff;border-radius:6px;padding:6px 8px;border:1px solid #E5E5EA}
/* Checklist */
.cl-item{display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #F5F5F5}
.cl-circle{width:20px;height:20px;border-radius:50%;border:2px solid #D1D1D6;cursor:pointer;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all .15s}
.cl-circle.done{background:#34C759;border-color:#34C759}
.cl-circle.done::after{content:'\\2713';font-size:10px;color:#fff;font-weight:700}
.cl-text{flex:1;font-size:13px}
.cl-text.done{text-decoration:line-through;color:#AEAEB2}
.cl-del{background:none;border:none;cursor:pointer;color:#AEAEB2;font-size:16px;padding:0 4px;line-height:1}
.cl-del:hover{color:#FF3B30}
/* Indicators */
.ind-badge{display:inline-flex;align-items:center;padding:4px 10px;border-radius:20px;font-size:11px;font-weight:600;cursor:pointer;border:1px solid #E5E5EA;background:#F2F2F7;color:#6C6C70;transition:all .15s;user-select:none;margin:2px}
.ind-badge.on{color:#fff;border-color:transparent}
.ind-badge.on.b-gas{background:#34C759}
.ind-badge.on.b-cert{background:#007AFF}
.ind-badge.on.b-warr{background:#FF9500}
.ind-badge.on.b-rep{background:#AF52DE}
.ind-badge.on.b-fol{background:#FF3B30}
.ind-badge.on.b-per{background:#0891b2}
/* Billing */
.billing-wrap{flex:1;overflow-y:auto;padding:14px}
.bi-table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #E5E5EA;border-radius:8px;overflow:hidden;margin-bottom:14px;font-size:12px}
.bi-table th{padding:7px 8px;font-size:10px;font-weight:600;color:#6C6C70;background:#F9F9FB;border-bottom:1px solid #E5E5EA;text-align:left;white-space:nowrap}
.bi-table td{padding:6px 8px;border-bottom:1px solid #F5F5F5;vertical-align:middle}
.bi-table tr:last-child td{border-bottom:none}
.bi-table input[type=text],.bi-table input[type=number]{border:none;outline:none;font-family:inherit;font-size:12px;width:100%;background:transparent;padding:2px 4px}
.bi-table input:focus{background:#EBF4FF;border-radius:4px}
.complete-btn-grp{display:inline-flex;align-items:stretch}
.complete-btn{background:#34C759;color:#fff;border:none;padding:7px 14px;border-radius:8px 0 0 8px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit}
.complete-btn-drop{background:#2ab04d;color:#fff;border:none;border-left:1px solid rgba(255,255,255,.3);padding:7px 10px;border-radius:0 8px 8px 0;cursor:pointer;font-size:12px}
/* Fleet */
.van-card{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.van-status-bar{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap}
.van-tag{font-size:10px;padding:2px 8px;border-radius:20px;font-weight:500}
.van-ok{background:#E8FAF0;color:#34C759}
.van-amber{background:#FFF4E5;color:#FF9500}
.van-red{background:#FFEBEB;color:#FF3B30}
.van-actions{display:flex;flex-wrap:wrap;gap:4px;margin-top:10px;padding-top:10px;border-top:1px solid #F2F2F7}
.van-actions .btn{font-size:10px;padding:4px 8px}
/* Agents */
.agent-card{background:#fff;border:1px solid #E5E5EA;border-radius:12px;padding:18px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.agent-code{font-size:11px;font-weight:700;color:#007AFF;background:#EBF4FF;padding:2px 8px;border-radius:6px;display:inline-block;margin-bottom:8px}
.agent-name{font-size:14px;font-weight:600;margin-bottom:6px}
.agent-desc{font-size:12px;color:#6C6C70;margin-bottom:10px;line-height:1.5}
.agent-ladder-bar{height:4px;background:#E5E5EA;border-radius:2px;margin-top:3px;overflow:hidden}
.agent-ladder-fill{height:100%;background:#007AFF;border-radius:2px;transition:width .3s}
/* HR */
.cert-expiry-badge{padding:3px 8px;border-radius:20px;font-size:11px;font-weight:600}
.cert-ok{background:#E8FAF0;color:#34C759}
.cert-amber{background:#FFF4E5;color:#FF9500}
.cert-red{background:#FFEBEB;color:#FF3B30}
/* Plans */
.plan-card{background:#fff;border:2px solid #E5E5EA;border-radius:16px;padding:24px;text-align:center;position:relative;transition:border-color .2s}
.plan-card.featured{border-color:#007AFF}
.plan-badge{position:absolute;top:-10px;left:50%;transform:translateX(-50%);background:#007AFF;color:#fff;padding:3px 12px;border-radius:20px;font-size:11px;font-weight:700}
.plan-price{font-size:36px;font-weight:700;margin:12px 0 4px}
.plan-period{font-size:12px;color:#6C6C70}
.plan-features{text-align:left;margin:16px 0}
.plan-feature{display:flex;align-items:center;gap:8px;padding:5px 0;font-size:13px}
.plan-feature svg{width:14px;height:14px;stroke:#34C759;fill:none;stroke-width:2.5;flex-shrink:0}
/* Guarantee */
.claim-item{background:#fff;border:1px solid #E5E5EA;border-radius:10px;padding:14px;margin-bottom:10px;display:flex;align-items:center;gap:14px;justify-content:space-between}
/* Roadmap */
.roadmap-phase{background:#F9F9FB;border:1px solid #E5E5EA;border-radius:12px;padding:14px}
.roadmap-item{padding:8px 0;border-bottom:1px solid #F2F2F7;display:flex;align-items:center;justify-content:space-between;gap:8px;font-size:13px}
.roadmap-item:last-child{border-bottom:none}
/* Security */
.hard-rule-card{background:#fff;border:1px solid #E5E5EA;border-radius:10px;padding:14px;display:flex;align-items:center;gap:14px}
.rule-num{width:28px;height:28px;border-radius:50%;background:#007AFF;color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
/* KPI */
.kpi-card{background:#fff;border:1px solid #E5E5EA;border-radius:10px;padding:14px;font-size:13px}
.kpi-value{font-size:22px;font-weight:700;margin:4px 0}
.kpi-trends{display:flex;gap:10px;font-size:11px;margin-top:6px}
.kpi-filter-btn{padding:5px 12px;border-radius:20px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid #E5E5EA;background:#fff;color:#6C6C70;transition:all .15s}
.kpi-filter-btn.active{background:#007AFF;color:#fff;border-color:#007AFF}
/* Misc */
.row{display:flex;gap:14px}
.mb-16{margin-bottom:16px}
.mb-20{margin-bottom:20px}
.mt-16{margin-top:16px}
.text-secondary{color:#6C6C70}
.text-sm{font-size:12px}
.font-600{font-weight:600}
.divider{height:1px;background:#E5E5EA;margin:16px 0}
.flex{display:flex}
.flex-center{display:flex;align-items:center}
.flex-between{display:flex;align-items:center;justify-content:space-between}
.gap-8{gap:8px}
.gap-12{gap:12px}
.w-full{width:100%}
.section-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}
.section-title{font-size:17px;font-weight:600}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%}
canvas{display:block;max-width:100%}
</style>
</head>
<body>
""")

# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
w("""<div id="fallback-banner">MANUAL FALLBACK MODE ACTIVE — All AI automation suspended.</div>
<nav id="sidebar">
  <div class="sidebar-logo">
    <div class="sidebar-logo-name">Rollo</div>
    <div class="sidebar-logo-sub">Business OS</div>
  </div>
  <div class="sidebar-nav">""")

nav_items = [
  ('control-room','Control Room','<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>'),
  ('jobs','Jobs','<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/>'),
  ('customers','Customers','<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'),
  ('dispatch','Dispatch','<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>'),
  ('comms','Comms','<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
  ('finance','Finance','<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="9" y1="11" x2="15" y2="11"/>'),
  ('agents','Agents','<rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="9" cy="10" r="1.5"/><circle cx="15" cy="10" r="1.5"/><path d="M9 15s1 1.5 3 1.5 3-1.5 3-1.5"/>'),
  ('hr','HR','<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>'),
  ('fleet','Fleet','<rect x="1" y="3" width="15" height="13" rx="1"/><path d="M16 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>'),
  ('marketing','Marketing','<path d="M22 8V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h9"/><path d="M2 10h20"/>'),
  ('plans','Plans','<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>'),
  ('guarantee','Guarantee','<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),
  ('roadmap','Roadmap','<line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/>'),
  ('security','Security','<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>'),
  ('reports','Reports','<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>'),
  ('settings','Settings','<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>'),
]

for i, (sec, label, svg) in enumerate(nav_items):
    active = ' active' if i == 0 else ''
    w(f'\n    <div class="nav-item{active}" onclick="showSection(\'{sec}\',this)" data-section="{sec}"><svg viewBox="0 0 24 24">{svg}</svg>{label}</div>')

w("""
  </div>
  <div class="sidebar-footer">v2.0 &middot; Rollo Business OS</div>
</nav>

<main id="main">
  <div id="topbar">
    <div id="page-title">Control Room</div>
    <div id="search-box">
      <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" placeholder="Search jobs, customers..." oninput="globalSearch(this.value)">
    </div>
    <div id="topbar-actions">
      <button class="btn btn-secondary btn-sm" onclick="showNewJobModal()">
        <svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>New Job
      </button>
      <button class="btn btn-primary btn-sm" onclick="showToast('Syncing...','info')">
        <svg viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>Sync
      </button>
    </div>
  </div>
  <div class="content">
""")

# ─── CONTROL ROOM SECTION ─────────────────────────────────────────────────────
w("""
<section class="section active" id="s-control-room">
  <div class="cosba-card mb-20">
    <div class="flex-between mb-16">
      <div>
        <div style="font-size:11px;font-weight:700;color:#007AFF;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px">COSBA Daily Briefing</div>
        <div style="font-size:15px;font-weight:600">Good morning &mdash; Wednesday 4 March 2026</div>
      </div>
      <span class="badge badge-blue">Live</span>
    </div>
    <div style="font-size:13px;color:#3C3C43;line-height:1.7">
      You have <strong>10 jobs scheduled today</strong> across 8 engineers. Trevor is on an emergency no-heat in Malahide at 07:30. Paula has a boiler service in Swords at 08:00. <strong>2 quotes overdue for follow-up</strong> &mdash; Q4421 (Portmarnock) and Q4418 (Clontarf). Darren&rsquo;s CVRT due in <strong>18 days</strong>. Outstanding invoices total <strong>&euro;1,240</strong>.
    </div>
  </div>
  <div class="grid-4 mb-20">
    <div class="stat-card"><div class="stat-icon" style="background:#007AFF"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div><div class="stat-num">6</div><div class="stat-label">New Leads</div><div class="stat-trend trend-up">+2 from yesterday</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#FF3B30"><svg viewBox="0 0 24 24"><line x1="1" y1="1" x2="23" y2="23"/><path d="M16.72 11.06A10.94 10.94 0 0 1 19 12.55"/></svg></div><div class="stat-num">2</div><div class="stat-label">Missed Calls</div><div class="stat-trend trend-down">Needs follow-up</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#FF9500"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div><div class="stat-num">2</div><div class="stat-label">Unquoted Jobs</div><div class="stat-trend trend-flat">Same as yesterday</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#AF52DE"><svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div><div class="stat-num">1</div><div class="stat-label">Open Quotes</div><div class="stat-trend trend-flat">Awaiting customer</div></div>
  </div>
  <div class="grid-4 mb-20">
    <div class="stat-card"><div class="stat-icon" style="background:#34C759"><svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/></svg></div><div class="stat-num" id="kpi-jobs-today">10</div><div class="stat-label">Jobs Today</div><div class="stat-trend trend-up">4 completed</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#FF9500"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div><div class="stat-num">1</div><div class="stat-label">Not Invoiced</div><div class="stat-trend trend-down">Action needed</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#FF3B30"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div><div class="stat-num">&euro;1,240</div><div class="stat-label">Unpaid Invoices</div><div class="stat-trend trend-down">3 invoices pending</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#FF3B30"><svg viewBox="0 0 24 24"><polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div><div class="stat-num">2</div><div class="stat-label">Urgent Alerts</div><div class="stat-trend trend-down">Immediate action</div></div>
  </div>
  <div class="card mb-20">
    <div class="card-title">Engineer Status</div>
    <div id="engineer-status-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px"></div>
  </div>
  <div class="row mb-20">
    <div style="flex:1">
      <div class="card mb-20">
        <div class="flex-between mb-16"><div class="card-title" style="margin-bottom:0">Black Hole Tracker</div><span class="badge badge-red">2 Urgent</span></div>
        <div id="bh-tracker"></div>
      </div>
      <div class="card">
        <div class="card-title">Activity Feed</div>
        <div id="activity-feed"></div>
      </div>
    </div>
    <div style="width:340px;flex-shrink:0">
      <div class="approval-queue mb-20">
        <div class="flex-between mb-16"><div class="card-title" style="margin-bottom:0">Approval Queue</div><span class="badge badge-orange" id="approval-count-badge">3 Pending</span></div>
        <div id="approval-queue"></div>
      </div>
      <div class="card">
        <div class="card-title">Escalation Matrix</div>
        <div class="escalation-card" style="border-left:4px solid #FF3B30"><div style="width:28px;height:28px;background:#FF3B30;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;flex-shrink:0">L1</div><div><div style="font-size:13px;font-weight:600">Gas Emergency</div><div style="font-size:11px;color:#6C6C70">999 + Bord G&aacute;is 1850 20 50 50 &mdash; 5 min</div></div></div>
        <div class="escalation-card" style="border-left:4px solid #FF9500"><div style="width:28px;height:28px;background:#FF9500;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;flex-shrink:0">L2</div><div><div style="font-size:13px;font-weight:600">Active Flooding</div><div style="font-size:11px;color:#6C6C70">Nearest engineer dispatched &mdash; isolate mains</div></div></div>
        <div class="escalation-card" style="border-left:4px solid #007AFF"><div style="width:28px;height:28px;background:#007AFF;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;flex-shrink:0">L3</div><div><div style="font-size:13px;font-weight:600">No Heating (Winter)</div><div style="font-size:11px;color:#6C6C70">Priority booking, same-day if possible</div></div></div>
        <div class="escalation-card" style="border-left:4px solid #34C759"><div style="width:28px;height:28px;background:#34C759;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;flex-shrink:0">L4</div><div><div style="font-size:13px;font-weight:600">Standard Urgent</div><div style="font-size:11px;color:#6C6C70">Next available slot &mdash; callback within 2 hrs</div></div></div>
      </div>
    </div>
  </div>
  <div class="card mb-20">
    <div class="flex-between mb-16">
      <div class="card-title" style="margin-bottom:0">15-KPI Dominance Dashboard</div>
      <div style="display:flex;gap:6px;flex-wrap:wrap">
        <button class="kpi-filter-btn active" onclick="filterKPI('all',this)">All</button>
        <button class="kpi-filter-btn" onclick="filterKPI('speed',this)">Speed</button>
        <button class="kpi-filter-btn" onclick="filterKPI('conversion',this)">Conversion</button>
        <button class="kpi-filter-btn" onclick="filterKPI('margin',this)">Margin</button>
        <button class="kpi-filter-btn" onclick="filterKPI('ops',this)">Ops</button>
        <button class="kpi-filter-btn" onclick="filterKPI('revenue',this)">Revenue</button>
        <button class="kpi-filter-btn" onclick="filterKPI('marketing',this)">Marketing</button>
      </div>
    </div>
    <div id="kpi-grid" style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px"></div>
  </div>
</section>
""")

# ─── JOBS SECTION ─────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-jobs">
  <div class="section-header mb-16">
    <div class="tabs" style="margin-bottom:0">
      <div class="tab active" onclick="switchJobView('kanban',this)">Kanban</div>
      <div class="tab" onclick="switchJobView('list',this)">List</div>
      <div class="tab" onclick="switchJobView('map',this)">Map</div>
    </div>
    <div class="flex gap-8">
      <input type="text" class="form-control btn-sm" placeholder="Search jobs..." style="width:200px" oninput="filterJobList(this.value)">
      <button class="btn btn-secondary btn-sm" onclick="showToast('Filter applied','info')">
        <svg viewBox="0 0 24 24"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>Filter
      </button>
      <button class="btn btn-primary btn-sm" onclick="showNewJobModal()">
        <svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>New Job
      </button>
    </div>
  </div>
  <div id="job-view-kanban"><div class="kanban-board" id="kanban-board"></div></div>
  <div id="job-view-list" style="display:none">
    <div class="table-wrap">
      <table id="jobs-table">
        <thead><tr><th>#</th><th>Customer</th><th>Address</th><th>Type</th><th>Engineer</th><th>Status</th><th>Value</th><th>Date</th><th>Actions</th></tr></thead>
        <tbody id="jobs-table-body"></tbody>
      </table>
    </div>
  </div>
  <div id="job-view-map" style="display:none">
    <div class="card mb-16" style="min-height:300px;display:flex;align-items:center;justify-content:center;background:#EBF4FF;border:2px dashed #007AFF">
      <div style="text-align:center;color:#6C6C70"><svg width="48" height="48" viewBox="0 0 24 24" style="stroke:#007AFF;fill:none;stroke-width:1.5;margin-bottom:10px"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg><div style="font-size:14px;font-weight:600;color:#007AFF">Map View</div><div style="font-size:12px;margin-top:4px">Google Maps integration via API key in Settings</div></div>
    </div>
    <div id="map-job-list"></div>
  </div>
</section>
""")

# ─── CUSTOMERS SECTION ────────────────────────────────────────────────────────
w("""
<section class="section" id="s-customers">
  <div class="section-header">
    <input type="text" class="form-control" placeholder="Search customers..." style="width:280px" oninput="filterCustomers(this.value)">
    <button class="btn btn-primary btn-sm" onclick="showAddCustomerModal()">
      <svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>Add Customer
    </button>
  </div>
  <div class="table-wrap">
    <table>
      <thead><tr><th>Name</th><th>Phone</th><th>Email</th><th>Area</th><th>Last Job</th><th>Total Spend</th><th>Membership</th><th>Actions</th></tr></thead>
      <tbody id="customers-table-body"></tbody>
    </table>
  </div>
</section>
""")

# ─── DISPATCH SECTION ─────────────────────────────────────────────────────────
w("""
<section class="section" id="s-dispatch">
  <div class="section-header mb-16">
    <div class="tabs" style="margin-bottom:0">
      <div class="tab active" onclick="switchDispatchView('day',this)">Day</div>
      <div class="tab" onclick="switchDispatchView('week',this)">Week</div>
      <div class="tab" onclick="switchDispatchView('month',this)">Month</div>
      <div class="tab" onclick="switchDispatchView('coverage',this)">Coverage Map</div>
    </div>
    <div class="flex gap-8" id="dispatch-date-nav">
      <button class="btn btn-secondary btn-sm" onclick="changeDispatchDate(-1)"><svg viewBox="0 0 24 24" width="14" height="14" style="stroke:currentColor;fill:none;stroke-width:2"><polyline points="15 18 9 12 15 6"/></svg></button>
      <button class="btn btn-secondary btn-sm" onclick="goToToday()">Today</button>
      <span id="dispatch-date-label" style="font-size:14px;font-weight:600;min-width:140px;text-align:center">Wed 4 Mar</span>
      <button class="btn btn-secondary btn-sm" onclick="changeDispatchDate(1)"><svg viewBox="0 0 24 24" width="14" height="14" style="stroke:currentColor;fill:none;stroke-width:2"><polyline points="9 18 15 12 9 6"/></svg></button>
    </div>
  </div>
  <div id="dispatch-view-day"></div>
  <div id="dispatch-view-week" style="display:none"><div class="card" style="padding:16px"><div id="week-grid" style="display:grid;grid-template-columns:repeat(7,1fr);gap:8px"></div></div></div>
  <div id="dispatch-view-month" style="display:none"><div class="card" style="padding:16px"><div id="month-grid" style="display:grid;grid-template-columns:repeat(7,1fr);gap:4px"></div></div></div>
  <div id="dispatch-view-coverage" style="display:none">
    <div class="card mb-16"><div class="card-title">Eircode Coverage Zones</div>
      <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px">
        <div style="background:#EBF4FF;border:2px solid #007AFF;border-radius:10px;padding:14px;text-align:center"><div style="font-size:18px;font-weight:700;color:#007AFF">D01&ndash;D24</div><div style="font-size:12px;color:#6C6C70;margin-top:4px">Dublin City</div><div style="font-size:11px;color:#34C759;font-weight:600;margin-top:4px">Primary Zone</div></div>
        <div style="background:#E8FAF0;border:2px solid #34C759;border-radius:10px;padding:14px;text-align:center"><div style="font-size:18px;font-weight:700;color:#34C759">K / A / Co</div><div style="font-size:12px;color:#6C6C70;margin-top:4px">Meath / Kildare</div><div style="font-size:11px;color:#34C759;font-weight:600;margin-top:4px">Secondary Zone</div></div>
        <div style="background:#FFF4E5;border:2px solid #FF9500;border-radius:10px;padding:14px;text-align:center"><div style="font-size:18px;font-weight:700;color:#FF9500">A / Co</div><div style="font-size:12px;color:#6C6C70;margin-top:4px">Louth / Wicklow</div><div style="font-size:11px;color:#FF9500;font-weight:600;margin-top:4px">Extended Zone</div></div>
        <div style="background:#F9F9FB;border:2px solid #E5E5EA;border-radius:10px;padding:14px;text-align:center"><div style="font-size:18px;font-weight:700;color:#AEAEB2">Other</div><div style="font-size:12px;color:#6C6C70;margin-top:4px">On Request</div><div style="font-size:11px;color:#AEAEB2;font-weight:600;margin-top:4px">Quote Required</div></div>
        <div style="background:#F5EEFF;border:2px solid #AF52DE;border-radius:10px;padding:14px;text-align:center"><div style="font-size:18px;font-weight:700;color:#AF52DE">B2B</div><div style="font-size:12px;color:#6C6C70;margin-top:4px">Nationwide</div><div style="font-size:11px;color:#AF52DE;font-weight:600;margin-top:4px">SLA Contract</div></div>
      </div>
    </div>
    <div class="card"><div class="card-title">Engineer Territory</div><div id="territory-table"></div></div>
  </div>
</section>
""")

# ─── COMMS ────────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-comms">
  <div class="section-header mb-16">
    <div class="tabs" style="margin-bottom:0">
      <div class="tab active" onclick="switchTab(this,'comms-all','comms-tab')">All</div>
      <div class="tab" onclick="switchTab(this,'comms-phone','comms-tab')">Phone</div>
      <div class="tab" onclick="switchTab(this,'comms-email','comms-tab')">Email</div>
      <div class="tab" onclick="switchTab(this,'comms-whatsapp','comms-tab')">WhatsApp</div>
      <div class="tab" onclick="switchTab(this,'comms-web','comms-tab')">Web</div>
    </div>
    <button class="btn btn-primary btn-sm" onclick="showComposeModal()">
      <svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>Compose
    </button>
  </div>
  <div id="comms-all" class="comms-tab">
    <div class="table-wrap"><table><thead><tr><th>Channel</th><th>From</th><th>Preview</th><th>Time</th><th>Status</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td><span class="badge badge-blue">Phone</span></td><td>086 123 4567</td><td>Missed call &mdash; no message left</td><td>09:14</td><td><span class="badge badge-red">Missed</span></td><td><button class="btn btn-primary btn-sm" onclick="showToast('Calling back...','success')">Call Back</button></td></tr>
      <tr><td><span class="badge badge-green">WhatsApp</span></td><td>Mary O'Brien</td><td>Hi, my boiler is making a strange noise...</td><td>09:31</td><td><span class="badge badge-orange">Unread</span></td><td><button class="btn btn-secondary btn-sm" onclick="showToast('WhatsApp opened','info')">Reply</button></td></tr>
      <tr><td><span class="badge badge-purple">Email</span></td><td>info@landlordco.ie</td><td>Boiler service needed at 4 units in Clontarf</td><td>08:52</td><td><span class="badge badge-orange">Unread</span></td><td><button class="btn btn-secondary btn-sm" onclick="showToast('Email client opened','info')">Reply</button></td></tr>
      <tr><td><span class="badge badge-blue">Web</span></td><td>Website Form</td><td>Emergency: no heat &mdash; family with infant</td><td>10:02</td><td><span class="badge badge-red">Urgent</span></td><td><button class="btn btn-primary btn-sm" onclick="showNewJobModal()">Create Job</button></td></tr>
      <tr><td><span class="badge badge-blue">Phone</span></td><td>01 234 5678</td><td>Query about gas cert pricing</td><td>10:18</td><td><span class="badge badge-grey">Read</span></td><td><button class="btn btn-secondary btn-sm" onclick="showToast('Logged','success')">Log</button></td></tr>
    </tbody></table></div>
  </div>
  <div id="comms-phone" class="comms-tab" style="display:none"><div class="card" style="padding:40px;text-align:center;color:#6C6C70">Phone call log &mdash; Nuacom integration required</div></div>
  <div id="comms-email" class="comms-tab" style="display:none"><div class="card" style="padding:40px;text-align:center;color:#6C6C70">Email integration &mdash; Connect via Settings &gt; Integrations</div></div>
  <div id="comms-whatsapp" class="comms-tab" style="display:none"><div class="card" style="padding:40px;text-align:center;color:#6C6C70">WhatsApp Business API &mdash; Twilio integration required</div></div>
  <div id="comms-web" class="comms-tab" style="display:none"><div class="card" style="padding:40px;text-align:center;color:#6C6C70">Web contact form submissions appear here</div></div>
</section>
""")

# ─── FINANCE ──────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-finance">
  <div class="grid-4 mb-20">
    <div class="stat-card"><div class="stat-icon" style="background:#34C759"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div><div class="stat-num">&euro;18,240</div><div class="stat-label">Revenue This Month</div><div class="stat-trend trend-up">+12% vs Feb</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#FF9500"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><div class="stat-num">&euro;1,240</div><div class="stat-label">Outstanding</div><div class="stat-trend trend-flat">3 invoices</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#FF3B30"><svg viewBox="0 0 24 24"><polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/></svg></div><div class="stat-num">&euro;640</div><div class="stat-label">Overdue</div><div class="stat-trend trend-down">Chase required</div></div>
    <div class="stat-card"><div class="stat-icon" style="background:#007AFF"><svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div><div class="stat-num">&euro;16,800</div><div class="stat-label">Collected</div><div class="stat-trend trend-up">On target</div></div>
  </div>
  <div class="tabs mb-16">
    <div class="tab active" onclick="switchTab(this,'fin-invoices','fin-tab')">Invoices</div>
    <div class="tab" onclick="switchTab(this,'fin-quotes','fin-tab')">Quotes</div>
    <div class="tab" onclick="switchTab(this,'fin-payments','fin-tab')">Payments</div>
    <div class="tab" onclick="switchTab(this,'fin-notinvoiced','fin-tab')">Not Invoiced</div>
    <div class="tab" onclick="switchTab(this,'fin-deadquote','fin-tab')">Dead-Quote Revival</div>
    <div class="tab" onclick="switchTab(this,'fin-b2b','fin-tab')">B2B Desk</div>
    <div class="tab" onclick="switchTab(this,'fin-overdue','fin-tab')">Overdue Chase</div>
  </div>
  <div id="fin-invoices" class="fin-tab">
    <div class="flex-between mb-16">
      <div style="font-size:14px;font-weight:600">All Invoices</div>
      <button class="btn btn-primary btn-sm" onclick="showCreateInvoiceModal()"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>Create Invoice</button>
    </div>
    <div class="table-wrap"><table><thead><tr><th>#</th><th>Customer</th><th>Job</th><th>Amount</th><th>Issued</th><th>Due</th><th>Status</th><th>Actions</th></tr></thead><tbody id="invoices-body"></tbody></table></div>
  </div>
  <div id="fin-quotes" class="fin-tab" style="display:none">
    <div class="table-wrap"><table><thead><tr><th>#</th><th>Customer</th><th>Type</th><th>Amount</th><th>Sent</th><th>Status</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td>Q4421</td><td>Ciaran Murphy, Portmarnock</td><td>Boiler Replacement</td><td>&euro;2,800</td><td>28 Feb</td><td><span class="badge badge-orange">Pending</span></td><td><button class="btn btn-secondary btn-sm" onclick="showToast('Follow-up sent','success')">Follow Up</button></td></tr>
      <tr><td>Q4418</td><td>Anne Kelly, Clontarf</td><td>Full Heating System</td><td>&euro;4,200</td><td>25 Feb</td><td><span class="badge badge-orange">Pending</span></td><td><button class="btn btn-secondary btn-sm" onclick="showToast('Follow-up sent','success')">Follow Up</button></td></tr>
    </tbody></table></div>
  </div>
  <div id="fin-payments" class="fin-tab" style="display:none">
    <div class="table-wrap"><table><thead><tr><th>Date</th><th>Customer</th><th>Invoice</th><th>Amount</th><th>Method</th><th>Ref</th></tr></thead>
    <tbody><tr><td>03 Mar</td><td>John Byrne</td><td>INV-0091</td><td>&euro;280</td><td>Card</td><td>ch_3xyz</td></tr><tr><td>02 Mar</td><td>Mary O'Brien</td><td>INV-0089</td><td>&euro;160</td><td>Bank Transfer</td><td>IBANTX</td></tr><tr><td>01 Mar</td><td>Derek Walsh</td><td>INV-0087</td><td>&euro;420</td><td>Cash</td><td>&mdash;</td></tr></tbody>
    </table></div>
  </div>
  <div id="fin-notinvoiced" class="fin-tab" style="display:none">
    <div class="table-wrap"><table><thead><tr><th>Job #</th><th>Customer</th><th>Date Completed</th><th>Type</th><th>Est. Value</th><th>Action</th></tr></thead>
    <tbody><tr><td>#19445</td><td>Paul Doyle</td><td>01 Mar</td><td>Boiler Service</td><td>&euro;120</td><td><button class="btn btn-primary btn-sm" onclick="showCreateInvoiceModal()">Invoice Now</button></td></tr></tbody>
    </table></div>
  </div>
  <div id="fin-deadquote" class="fin-tab" style="display:none">
    <div class="card"><div class="card-title">Dead-Quote Revival Pipeline</div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">
        <div style="background:#F2F2F7;border-radius:10px;padding:12px"><div style="font-size:11px;font-weight:700;color:#FF9500;margin-bottom:8px">48HR FOLLOW-UP</div><div style="background:#fff;border:1px solid #E5E5EA;border-radius:8px;padding:10px;font-size:12px"><div style="font-weight:600">Q4421 &mdash; Portmarnock</div><div style="color:#6C6C70">&euro;2,800 &middot; Boiler Replacement</div><button class="btn btn-secondary btn-sm" style="margin-top:8px;width:100%" onclick="showToast('SMS sent','success')">Send SMS</button></div></div>
        <div style="background:#F2F2F7;border-radius:10px;padding:12px"><div style="font-size:11px;font-weight:700;color:#FF9500;margin-bottom:8px">7-DAY PERSONALISED</div><div style="background:#fff;border:1px solid #E5E5EA;border-radius:8px;padding:10px;font-size:12px"><div style="font-weight:600">Q4418 &mdash; Clontarf</div><div style="color:#6C6C70">&euro;4,200 &middot; Heating System</div><button class="btn btn-secondary btn-sm" style="margin-top:8px;width:100%" onclick="showToast('Email sent','success')">Send Email</button></div></div>
        <div style="background:#F2F2F7;border-radius:10px;padding:12px"><div style="font-size:11px;font-weight:700;color:#FF3B30;margin-bottom:8px">14-DAY LAST CHANCE</div><div style="color:#AEAEB2;font-size:12px;text-align:center;padding:20px 0">No quotes</div></div>
        <div style="background:#F2F2F7;border-radius:10px;padding:12px"><div style="font-size:11px;font-weight:700;color:#AEAEB2;margin-bottom:8px">30-DAY COLD PIPELINE</div><div style="color:#AEAEB2;font-size:12px;text-align:center;padding:20px 0">No quotes</div></div>
      </div>
    </div>
  </div>
  <div id="fin-b2b" class="fin-tab" style="display:none">
    <div class="card"><div class="card-title">B2B Portfolio Desk</div>
      <div class="table-wrap" style="border:none"><table><thead><tr><th>Agency</th><th>Contact</th><th>Properties</th><th>Open Jobs</th><th>SLA Status</th><th>Outstanding</th></tr></thead>
      <tbody><tr><td>Daft Property Mgmt</td><td>Sarah Collins</td><td>14</td><td>2</td><td><span class="badge badge-green">Within 4hr</span></td><td>&euro;480</td></tr><tr><td>Dublin Rentals Ltd</td><td>Mark Hennessy</td><td>8</td><td>1</td><td><span class="badge badge-orange">Approaching</span></td><td>&euro;120</td></tr></tbody>
      </table></div>
    </div>
  </div>
  <div id="fin-overdue" class="fin-tab" style="display:none">
    <div class="card"><div class="card-title">Overdue Chase Workflow</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">
        <div style="background:#FFF4E5;border:1px solid #FF9500;border-radius:10px;padding:14px"><div style="font-size:12px;font-weight:700;color:#FF9500;margin-bottom:8px">DAY 7 &mdash; FIRST CHASE</div><div style="font-size:13px;font-weight:600">INV-0085 &middot; &euro;320</div><div style="font-size:11px;color:#6C6C70">Brian Murphy &middot; Drumcondra</div><button class="btn btn-secondary btn-sm" style="margin-top:8px" onclick="showToast('Chase sent','success')">Send Chase</button></div>
        <div style="background:#FFEBEB;border:1px solid #FF3B30;border-radius:10px;padding:14px"><div style="font-size:12px;font-weight:700;color:#FF3B30;margin-bottom:8px">DAY 14 &mdash; PHONE CALL</div><div style="font-size:13px;font-weight:600">INV-0082 &middot; &euro;640</div><div style="font-size:11px;color:#6C6C70">Alan Doyle &middot; Raheny</div><button class="btn btn-danger btn-sm" style="margin-top:8px" onclick="showToast('Call logged','success')">Log Call</button></div>
        <div style="background:#FFEBEB;border:1px solid #FF3B30;border-radius:10px;padding:14px"><div style="font-size:12px;font-weight:700;color:#FF3B30;margin-bottom:8px">DAY 30 &mdash; FINAL DEMAND</div><div style="color:#AEAEB2;font-size:12px;margin-top:8px">No invoices at this stage</div></div>
      </div>
    </div>
  </div>
</section>
""")

# ─── AGENTS ───────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-agents">
  <div class="section-header mb-16">
    <div style="font-size:15px;font-weight:600">AI Agent Control Centre</div>
    <button class="btn btn-secondary btn-sm" onclick="showToast('All agent statuses refreshed','success')">
      <svg viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>Refresh All
    </button>
  </div>
  <div id="agents-grid" class="grid-3"></div>
</section>
""")

# ─── HR ───────────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-hr">
  <div class="tabs mb-16">
    <div class="tab active" onclick="switchTab(this,'hr-profiles','hr-tab')">Engineer Profiles</div>
    <div class="tab" onclick="switchTab(this,'hr-hiring','hr-tab')">Hiring Kanban</div>
    <div class="tab" onclick="switchTab(this,'hr-certs','hr-tab')">Certifications</div>
    <div class="tab" onclick="switchTab(this,'hr-onboarding','hr-tab')">Onboarding</div>
  </div>
  <div id="hr-profiles" class="hr-tab"><div id="hr-profiles-grid" class="grid-4" style="grid-template-columns:repeat(4,1fr)"></div></div>
  <div id="hr-hiring" class="hr-tab" style="display:none">
    <div class="flex-between mb-16">
      <div style="font-size:14px;font-weight:600">Hiring Pipeline</div>
      <button class="btn btn-primary btn-sm" onclick="showAddCandidateModal()"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>Add Candidate</button>
    </div>
    <div class="kanban-board">
      <div class="kanban-col" ondragover="event.preventDefault()" ondrop="dropCandidate(event,'sourced')"><div class="kanban-col-header"><span class="kanban-col-title">Sourced</span><span class="kanban-count">2</span></div><div id="hk-sourced"><div class="job-card" draggable="true" ondragstart="dragCandidate(event,'Shane Brennan')"><div class="job-card-customer">Shane Brennan</div><div class="job-card-type">Gas Engineer &middot; 5yrs exp</div></div><div class="job-card" draggable="true" ondragstart="dragCandidate(event,'Conor Reilly')"><div class="job-card-customer">Conor Reilly</div><div class="job-card-type">Plumber &middot; 3yrs exp</div></div></div></div>
      <div class="kanban-col" ondragover="event.preventDefault()" ondrop="dropCandidate(event,'applied')"><div class="kanban-col-header"><span class="kanban-col-title">Applied</span><span class="kanban-count">1</span></div><div id="hk-applied"><div class="job-card" draggable="true" ondragstart="dragCandidate(event,'Luke Farrell')"><div class="job-card-customer">Luke Farrell</div><div class="job-card-type">Apprentice &middot; City &amp; Guilds</div></div></div></div>
      <div class="kanban-col" ondragover="event.preventDefault()" ondrop="dropCandidate(event,'cvreview')"><div class="kanban-col-header"><span class="kanban-col-title">CV Review</span><span class="kanban-count">0</span></div><div id="hk-cvreview"></div></div>
      <div class="kanban-col" ondragover="event.preventDefault()" ondrop="dropCandidate(event,'phone')"><div class="kanban-col-header"><span class="kanban-col-title">Phone Screen</span><span class="kanban-count">0</span></div><div id="hk-phone"></div></div>
      <div class="kanban-col" ondragover="event.preventDefault()" ondrop="dropCandidate(event,'interview')"><div class="kanban-col-header"><span class="kanban-col-title">Interview</span><span class="kanban-count">0</span></div><div id="hk-interview"></div></div>
      <div class="kanban-col" ondragover="event.preventDefault()" ondrop="dropCandidate(event,'trial')"><div class="kanban-col-header"><span class="kanban-col-title">Trial Day</span><span class="kanban-count">0</span></div><div id="hk-trial"></div></div>
      <div class="kanban-col" ondragover="event.preventDefault()" ondrop="dropCandidate(event,'offer')"><div class="kanban-col-header"><span class="kanban-col-title">Offer</span><span class="kanban-count">0</span></div><div id="hk-offer"></div></div>
    </div>
  </div>
  <div id="hr-certs" class="hr-tab" style="display:none">
    <div class="card"><div class="card-title">Certifications &amp; Compliance</div>
      <div class="table-wrap" style="border:none"><table><thead><tr><th>Engineer</th><th>RGI</th><th>Safe Pass</th><th>Insurance</th><th>Gas Cert</th><th>CVRT</th></tr></thead><tbody id="certs-table-body"></tbody></table></div>
    </div>
  </div>
  <div id="hr-onboarding" class="hr-tab" style="display:none">
    <div class="card"><div class="card-title">Onboarding Checklist &mdash; New Start</div><div id="onboarding-checklist"></div></div>
  </div>
</section>
""")

# ─── FLEET ────────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-fleet">
  <div class="section-header mb-20">
    <div style="font-size:15px;font-weight:600">Fleet Management</div>
    <div class="flex gap-8">
      <button class="btn btn-secondary btn-sm" onclick="showToast('Fleet report generated','success')">Export Report</button>
      <button class="btn btn-primary btn-sm" onclick="showAddVanModal()">
        <svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>Add New Van
      </button>
    </div>
  </div>
  <div id="fleet-grid" class="grid-4"></div>
</section>
""")

# ─── MARKETING ────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-marketing">
  <div class="tabs mb-16">
    <div class="tab active" onclick="switchTab(this,'mkt-overview','mkt-tab')">Overview</div>
    <div class="tab" onclick="switchTab(this,'mkt-google','mkt-tab')">Google Ads</div>
    <div class="tab" onclick="switchTab(this,'mkt-weather','mkt-tab')">Weather Trigger</div>
    <div class="tab" onclick="switchTab(this,'mkt-tiktok','mkt-tab')">TikTok Trust</div>
    <div class="tab" onclick="switchTab(this,'mkt-seasonal','mkt-tab')">Seasonal</div>
  </div>
  <div id="mkt-overview" class="mkt-tab">
    <div class="grid-4 mb-20">
      <div class="stat-card"><div class="stat-icon" style="background:#007AFF"><svg viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></div><div class="stat-num">48,200</div><div class="stat-label">Impressions</div><div class="stat-trend trend-up">+18% this week</div></div>
      <div class="stat-card"><div class="stat-icon" style="background:#34C759"><svg viewBox="0 0 24 24"><path d="M15 3h6v6"/><path d="M10 14 21 3"/></svg></div><div class="stat-num">1,240</div><div class="stat-label">Clicks</div><div class="stat-trend trend-up">CTR 2.6%</div></div>
      <div class="stat-card"><div class="stat-icon" style="background:#FF9500"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div><div class="stat-num">&euro;380</div><div class="stat-label">Ad Spend</div><div class="stat-trend trend-flat">Budget on track</div></div>
      <div class="stat-card"><div class="stat-icon" style="background:#AF52DE"><svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div><div class="stat-num">28</div><div class="stat-label">Conversions</div><div class="stat-trend trend-up">CPA &euro;13.57</div></div>
    </div>
    <div class="card"><div class="card-title">Campaign Performance</div>
      <div class="table-wrap" style="border:none"><table><thead><tr><th>Campaign</th><th>Impressions</th><th>Clicks</th><th>CTR</th><th>Cost</th><th>Conv.</th><th>Status</th></tr></thead>
      <tbody><tr><td>Emergency Boiler Repair Dublin</td><td>22,400</td><td>680</td><td>3.04%</td><td>&euro;184</td><td>14</td><td><span class="badge badge-green">Active</span></td></tr><tr><td>Boiler Service Dublin 2026</td><td>18,600</td><td>420</td><td>2.26%</td><td>&euro;120</td><td>9</td><td><span class="badge badge-green">Active</span></td></tr></tbody>
      </table></div>
    </div>
  </div>
  <div id="mkt-google" class="mkt-tab" style="display:none"><div class="card"><div class="card-title">Google Ads Dashboard</div><div style="color:#6C6C70;font-size:13px">Connect Google Ads API in Settings to pull live data.</div></div></div>
  <div id="mkt-weather" class="mkt-tab" style="display:none">
    <div style="background:linear-gradient(135deg,#007AFF,#5AC8FA);border-radius:12px;padding:20px;color:#fff;margin-bottom:16px">
      <div style="font-size:13px;font-weight:600;opacity:.8;margin-bottom:6px">Met Eireann &mdash; Dublin</div>
      <div style="display:flex;align-items:flex-end;gap:16px"><div style="font-size:48px;font-weight:700">4&deg;C</div><div><div style="font-size:16px;font-weight:600">Cold &amp; Overcast</div><div style="font-size:13px;opacity:.8;margin-top:2px">Emergency heating keywords: AUTO-SCALED</div></div></div>
    </div>
    <div class="card"><div class="card-title">Weather-Triggered Advertising</div>
      <div class="form-group"><label class="form-label">Emergency Heating Trigger Threshold</label><div style="display:flex;gap:8px;align-items:center"><input type="range" min="-5" max="10" value="2" id="temp-threshold" oninput="updateTempThreshold(this.value)" style="flex:1"><span id="temp-threshold-val" style="font-size:16px;font-weight:700;min-width:40px">2&deg;C</span></div></div>
      <div class="flex-between" style="background:#E8FAF0;border:1px solid #34C759;border-radius:10px;padding:14px"><div><div style="font-size:13px;font-weight:600;color:#34C759">AUTO-SCALE ACTIVE</div><div style="font-size:12px;color:#3C3C43;margin-top:2px">Current temp below threshold &mdash; emergency keywords bid boost: +150%</div></div><label class="toggle"><input type="checkbox" checked onchange="showToast('Weather trigger '+(this.checked?'enabled':'disabled'),'success')"><div class="toggle-slider"></div></label></div>
    </div>
  </div>
  <div id="mkt-tiktok" class="mkt-tab" style="display:none">
    <div class="card mb-16"><div class="card-title">TikTok Trust Engine</div><div class="grid-4"><div class="stat-card"><div class="stat-num">14</div><div class="stat-label">Videos Posted</div></div><div class="stat-card"><div class="stat-num">42.1K</div><div class="stat-label">Total Views</div></div><div class="stat-card"><div class="stat-num">1,840</div><div class="stat-label">Followers</div></div><div class="stat-card"><div class="stat-num">6.2%</div><div class="stat-label">Engagement Rate</div></div></div></div>
    <div class="card"><div class="card-title">Content Calendar</div><div class="table-wrap" style="border:none"><table><thead><tr><th>Date</th><th>Content</th><th>Type</th><th>Status</th></tr></thead><tbody><tr><td>04 Mar</td><td>Behind the scenes: boiler service in Malahide</td><td>Educational</td><td><span class="badge badge-orange">Scheduled</span></td></tr><tr><td>06 Mar</td><td>Top 5 signs your boiler needs replacing</td><td>Tips</td><td><span class="badge badge-grey">Draft</span></td></tr></tbody></table></div></div>
  </div>
  <div id="mkt-seasonal" class="mkt-tab" style="display:none">
    <div class="card"><div class="card-title">Seasonal Campaign Tracker</div><div class="table-wrap" style="border:none"><table><thead><tr><th>Campaign</th><th>Period</th><th>Channel</th><th>Budget</th><th>Status</th></tr></thead><tbody><tr><td>Winter Emergency Push</td><td>Nov&ndash;Mar</td><td>Google / Meta</td><td>&euro;1,200/mo</td><td><span class="badge badge-green">Active</span></td></tr><tr><td>Spring Boiler Service</td><td>Apr&ndash;May</td><td>Google / TikTok</td><td>&euro;600/mo</td><td><span class="badge badge-grey">Planned</span></td></tr></tbody></table></div></div>
  </div>
</section>
""")

# ─── PLANS ────────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-plans">
  <div class="grid-4 mb-20" style="grid-template-columns:repeat(3,1fr)">
    <div class="plan-card"><div style="font-size:14px;font-weight:600;color:#6C6C70">Care Plan</div><div class="plan-price">&euro;12.99</div><div class="plan-period">per month</div><div style="margin:16px 0;height:1px;background:#E5E5EA"></div><div class="plan-features"><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Annual boiler service</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Priority booking</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>10% discount on labour</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Digital gas cert</div></div><button class="btn btn-secondary w-full" onclick="showToast('Plan selected','success')">Manage Plan</button></div>
    <div class="plan-card featured"><div class="plan-badge">Most Popular</div><div style="font-size:14px;font-weight:600;color:#007AFF">Priority Plan</div><div class="plan-price" style="color:#007AFF">&euro;19.99</div><div class="plan-period">per month</div><div style="margin:16px 0;height:1px;background:#E5E5EA"></div><div class="plan-features"><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Everything in Care</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Same-day emergency response</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>15% discount on labour</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Free 2nd gas cert</div></div><button class="btn btn-primary w-full" onclick="showToast('Plan selected','success')">Manage Plan</button></div>
    <div class="plan-card"><div style="font-size:14px;font-weight:600;color:#AF52DE">Protect Plan</div><div class="plan-price" style="color:#AF52DE">&euro;29.99</div><div class="plan-period">per month</div><div style="margin:16px 0;height:1px;background:#E5E5EA"></div><div class="plan-features"><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Everything in Priority</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Full heating system cover</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>20% discount on all labour</div><div class="plan-feature"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>VIP helpline access</div></div><button class="btn btn-secondary w-full" style="border-color:#AF52DE;color:#AF52DE" onclick="showToast('Plan selected','success')">Manage Plan</button></div>
  </div>
  <div class="grid-3">
    <div class="card"><div class="card-title">Plan Stats</div><div style="font-size:28px;font-weight:700;margin-bottom:4px">84</div><div style="font-size:13px;color:#6C6C70">Total Subscribers</div><div class="divider"></div><div class="flex-between"><div><div style="font-size:20px;font-weight:700">&euro;1,420</div><div style="font-size:12px;color:#6C6C70">MRR</div></div><div><div style="font-size:20px;font-weight:700;color:#34C759">+6</div><div style="font-size:12px;color:#6C6C70">This Month</div></div></div></div>
    <div class="card"><div class="card-title">Plan Breakdown</div><div class="flex-between mb-16"><span class="text-sm">Care (&euro;12.99)</span><span style="font-weight:600">42 members</span></div><div style="height:6px;background:#E5E5EA;border-radius:3px;margin-bottom:16px"><div style="height:100%;width:50%;background:#34C759;border-radius:3px"></div></div><div class="flex-between mb-16"><span class="text-sm">Priority (&euro;19.99)</span><span style="font-weight:600">28 members</span></div><div style="height:6px;background:#E5E5EA;border-radius:3px;margin-bottom:16px"><div style="height:100%;width:33%;background:#007AFF;border-radius:3px"></div></div><div class="flex-between mb-16"><span class="text-sm">Protect (&euro;29.99)</span><span style="font-weight:600">14 members</span></div><div style="height:6px;background:#E5E5EA;border-radius:3px"><div style="height:100%;width:17%;background:#AF52DE;border-radius:3px"></div></div></div>
    <div class="card"><div class="card-title">Loyalty Voucher Table</div><div class="table-wrap" style="border:none"><table><thead><tr><th>Spend Threshold</th><th>Voucher Value</th></tr></thead><tbody><tr><td>&euro;500</td><td>&euro;25 credit</td></tr><tr><td>&euro;800</td><td>&euro;50 credit</td></tr><tr><td>&euro;1,000</td><td>&euro;80 credit</td></tr><tr><td>&euro;1,500</td><td>&euro;120 credit</td></tr><tr><td>&euro;2,000+</td><td>&euro;200 credit</td></tr></tbody></table></div></div>
  </div>
</section>
""")

# ─── GUARANTEE ────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-guarantee">
  <div class="tabs mb-16">
    <div class="tab active" onclick="switchTab(this,'guar-claims','guar-tab')">Claims Queue</div>
    <div class="tab" onclick="switchTab(this,'guar-new','guar-tab')">New Claim</div>
    <div class="tab" onclick="switchTab(this,'guar-stats','guar-tab')">Stats</div>
    <div class="tab" onclick="switchTab(this,'guar-sms','guar-tab')">SMS Log</div>
    <div class="tab" onclick="switchTab(this,'guar-tc','guar-tab')">T&amp;Cs</div>
  </div>
  <div id="guar-claims" class="guar-tab">
    <div class="card mb-16"><div class="flex-between mb-16"><div class="card-title" style="margin-bottom:0">Guarantee Claims</div><span class="badge badge-orange">2 Pending</span></div>
      <div class="claim-item"><div style="flex:1"><div style="font-size:13px;font-weight:600">CLM-0014 &mdash; Mary O'Shea, Finglas</div><div style="font-size:12px;color:#6C6C70;margin-top:3px">Boiler fault returned within 48hrs &middot; Phase 1 &middot; &euro;100 credit</div></div><span class="badge badge-orange">Pending</span><button class="btn btn-success btn-sm" onclick="this.previousSibling.className='badge badge-green';this.previousSibling.textContent='Approved';showToast('Claim CLM-0014 approved','success')">Approve</button><button class="btn btn-danger btn-sm" onclick="this.closest('.claim-item').remove();showToast('Claim rejected','error')">Reject</button></div>
      <div class="claim-item"><div style="flex:1"><div style="font-size:13px;font-weight:600">CLM-0013 &mdash; Paul Lawlor, Blanchardstown</div><div style="font-size:12px;color:#6C6C70;margin-top:3px">No hot water 3 days after repair &middot; Phase 2 &middot; Full refund</div></div><span class="badge badge-orange">Pending</span><button class="btn btn-success btn-sm" onclick="this.closest('.claim-item').remove();showToast('Claim CLM-0013 approved','success')">Approve</button><button class="btn btn-danger btn-sm" onclick="this.closest('.claim-item').remove();showToast('Claim rejected','error')">Reject</button></div>
    </div>
  </div>
  <div id="guar-new" class="guar-tab" style="display:none">
    <div class="card" style="max-width:560px"><div class="card-title">Submit New Guarantee Claim</div>
      <div class="form-group"><label class="form-label">Customer Name</label><input type="text" class="form-control" placeholder="Full name"></div>
      <div class="form-group"><label class="form-label">Job Reference</label><input type="text" class="form-control" placeholder="#19440"></div>
      <div class="form-group"><label class="form-label">Phase</label><select class="form-control"><option>Phase 1 &mdash; Fixed credit (&euro;100)</option><option>Phase 2 &mdash; Full refund + lost-pay</option></select></div>
      <div class="form-group"><label class="form-label">Issue Description</label><textarea class="form-control" rows="3"></textarea></div>
      <button class="btn btn-primary" onclick="showToast('Claim submitted','success')">Submit Claim</button>
    </div>
  </div>
  <div id="guar-stats" class="guar-tab" style="display:none"><div class="grid-4"><div class="stat-card"><div class="stat-num">14</div><div class="stat-label">Total Claims</div></div><div class="stat-card"><div class="stat-num">11</div><div class="stat-label">Approved</div><div class="stat-trend trend-up">78.5% rate</div></div><div class="stat-card"><div class="stat-num">2</div><div class="stat-label">Pending</div></div><div class="stat-card"><div class="stat-num">&euro;1,480</div><div class="stat-label">Total Paid Out</div></div></div></div>
  <div id="guar-sms" class="guar-tab" style="display:none"><div class="card"><div class="card-title">SMS Communication Log</div><div class="table-wrap" style="border:none"><table><thead><tr><th>Date</th><th>Claim</th><th>To</th><th>Message</th><th>Status</th></tr></thead><tbody><tr><td>03 Mar 10:14</td><td>CLM-0012</td><td>087 *** ****</td><td>Hi Joan, your claim has been approved. &euro;100 credit added.</td><td><span class="badge badge-green">Delivered</span></td></tr></tbody></table></div></div></div>
  <div id="guar-tc" class="guar-tab" style="display:none"><div class="card" style="max-width:700px;line-height:1.8;font-size:13px"><div class="card-title">Guarantee Terms &amp; Conditions</div><p><strong>Phase 1:</strong> If the same fault recurs within 30 days, the customer receives a &euro;100 service credit.</p><p style="margin-top:12px"><strong>Phase 2:</strong> If the fault recurs a second time within 90 days, the customer is entitled to a full refund plus compensation for demonstrable lost pay, up to &euro;200.</p><p style="margin-top:12px"><strong>RGI Gas Work:</strong> All gas-related guarantee decisions must be reviewed by an RGI-registered engineer before approval. No AI automation of gas guarantee decisions.</p></div></div>
</section>
""")

# ─── ROADMAP ──────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-roadmap">
  <div class="section-header mb-20"><div style="font-size:15px;font-weight:600">Product Roadmap &mdash; 90 Day Plan</div><span class="badge badge-blue">Phase 1 Active</span></div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px">
    <div class="roadmap-phase"><div style="font-size:11px;font-weight:700;color:#007AFF;margin-bottom:8px">PHASE 1 &mdash; COMMS</div><div class="roadmap-item"><span>Nuacom call integration</span><span class="badge badge-green">Done</span></div><div class="roadmap-item"><span>WhatsApp Business API</span><span class="badge badge-orange">In Progress</span></div><div class="roadmap-item"><span>Email inbox sync</span><span class="badge badge-grey">Planned</span></div><div class="roadmap-item"><span>Black Hole Tracker</span><span class="badge badge-green">Done</span></div></div>
    <div class="roadmap-phase"><div style="font-size:11px;font-weight:700;color:#34C759;margin-bottom:8px">PHASE 2 &mdash; FIELD</div><div class="roadmap-item"><span>Engineer mobile app</span><span class="badge badge-orange">In Progress</span></div><div class="roadmap-item"><span>GPS tracking</span><span class="badge badge-grey">Planned</span></div><div class="roadmap-item"><span>Digital job sheets</span><span class="badge badge-grey">Planned</span></div><div class="roadmap-item"><span>Photo uploads</span><span class="badge badge-grey">Planned</span></div></div>
    <div class="roadmap-phase"><div style="font-size:11px;font-weight:700;color:#FF9500;margin-bottom:8px">PHASE 3 &mdash; GROWTH</div><div class="roadmap-item"><span>Online booking portal</span><span class="badge badge-grey">Planned</span></div><div class="roadmap-item"><span>Review automation</span><span class="badge badge-grey">Planned</span></div><div class="roadmap-item"><span>Finance dashboard</span><span class="badge badge-green">Done</span></div></div>
    <div class="roadmap-phase"><div style="font-size:11px;font-weight:700;color:#AF52DE;margin-bottom:8px">PHASE 4 &mdash; SCALE</div><div class="roadmap-item"><span>Multi-location support</span><span class="badge badge-grey">Future</span></div><div class="roadmap-item"><span>Franchise module</span><span class="badge badge-grey">Future</span></div><div class="roadmap-item"><span>White-label platform</span><span class="badge badge-grey">Future</span></div></div>
  </div>
</section>
""")

# ─── SECURITY ─────────────────────────────────────────────────────────────────
w("""
<section class="section" id="s-security">
  <div class="tabs mb-16">
    <div class="tab active" onclick="switchTab(this,'sec-rules','sec-tab')">Hard Rules</div>
    <div class="tab" onclick="switchTab(this,'sec-envs','sec-tab')">Environments</div>
    <div class="tab" onclick="switchTab(this,'sec-dpc','sec-tab')">DPC/GDPR</div>
    <div class="tab" onclick="switchTab(this,'sec-log','sec-tab')">Access Log</div>
  </div>
  <div id="sec-rules" class="sec-tab">
    <div class="card-title mb-16">8 Hard Rules &mdash; Non-Negotiable Constraints</div>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px">
      <div class="hard-rule-card"><div class="rule-num">1</div><div style="flex:1"><div style="font-size:13px;font-weight:600">No AI Gas Decisions</div><div style="font-size:12px;color:#6C6C70;margin-top:3px">All gas safety decisions require a human RGI engineer.</div></div><span class="badge badge-green">Enforced</span></div>
      <div class="hard-rule-card"><div class="rule-num">2</div><div style="flex:1"><div style="font-size:13px;font-weight:600">No Personal Data Export</div><div style="font-size:12px;color:#6C6C70;margin-top:3px">Customer PII cannot be exported without explicit consent. GDPR Article 6.</div></div><span class="badge badge-green">Enforced</span></div>
      <div class="hard-rule-card"><div class="rule-num">3</div><div style="flex:1"><div style="font-size:13px;font-weight:600">Human Approval for Invoices &gt;&euro;500</div><div style="font-size:12px;color:#6C6C70;margin-top:3px">Any invoice