#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del prototipo HTML "Banreservas - Pago Instantaneo (IPS)".
Emite un unico archivo index.html autocontenido, pensado para importarse a Figma
con el plugin html.to.design (o similar). Cada pantalla es un <section class="frame">
de 1440px (o 390px en mobile) que Figma convierte en un frame independiente.
"""
import os, random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

# ---------------------------------------------------------------- tokens / css
CSS = r"""
:root{
  /* Marca Banreservas */
  --br-navy:#00396B;        /* azul institucional profundo */
  --br-blue:#00529B;        /* azul primario */
  --br-blue-600:#0A6FB7;
  --br-cyan:#1BA5DF;        /* cyan del menu lateral */
  --br-cyan-600:#128FC6;
  --br-cyan-050:#E7F5FC;
  --br-orange:#F58220;      /* naranja de accion */
  --br-orange-600:#DC6E10;
  --br-orange-050:#FFF3E7;

  /* Neutrales */
  --bg:#EFF2F6;
  --surface:#FFFFFF;
  --line:#E2E8F0;
  --line-strong:#CBD5E1;
  --ink:#1B2733;
  --ink-2:#48586B;
  --ink-3:#7A8A9C;

  /* Semanticos */
  --ok:#0F8A4D;   --ok-bg:#E8F6EE;
  --warn:#B7791F; --warn-bg:#FEF6E7;
  --err:#C62828;  --err-bg:#FDECEC;
  --info:#0A6FB7; --info-bg:#E7F1FA;

  --r-sm:6px; --r:10px; --r-lg:16px; --r-xl:22px;
  --sh-1:0 1px 2px rgba(16,36,58,.06), 0 1px 3px rgba(16,36,58,.06);
  --sh-2:0 4px 14px rgba(16,36,58,.10);
  --sh-3:0 18px 40px rgba(16,36,58,.18);
}
*{box-sizing:border-box;margin:0;padding:0}
body{
  font-family:'Nunito Sans','Segoe UI',Helvetica,Arial,sans-serif;
  background:#0E1620; color:var(--ink); -webkit-font-smoothing:antialiased;
}
img{max-width:100%}

/* ------------------------------------------------------------ canvas layout */
.canvas{padding:56px 56px 120px;display:flex;flex-direction:column;gap:64px}
.canvas-head{max-width:1440px;color:#fff}
.canvas-head h1{font-size:44px;line-height:1.05;font-weight:800;letter-spacing:-.5px}
.canvas-head h1 span{color:var(--br-orange)}
.canvas-head p{margin-top:14px;font-size:17px;line-height:1.6;color:#AFC0D2;max-width:1080px}
.canvas-meta{margin-top:22px;display:flex;gap:10px;flex-wrap:wrap}
.canvas-meta em{
  font-style:normal;font-size:12px;font-weight:700;letter-spacing:.3px;color:#CBD9E7;
  border:1px solid #2A3B4E;background:#16222F;border-radius:999px;padding:7px 14px;
}
.group{display:flex;flex-direction:column;gap:26px}
.group-head{display:flex;align-items:flex-end;gap:16px;color:#fff;border-bottom:1px solid #22303F;padding-bottom:14px}
.group-head .n{
  font-size:13px;font-weight:800;color:#0E1620;background:var(--br-orange);
  border-radius:8px;padding:6px 11px;letter-spacing:.5px
}
.group-head h2{font-size:26px;font-weight:800;letter-spacing:-.2px}
.group-head p{font-size:14px;color:#93A6B9;margin-left:auto;max-width:620px;text-align:right;line-height:1.5}
.row{display:flex;flex-wrap:wrap;gap:44px;align-items:flex-start}

.frame-wrap{display:flex;flex-direction:column;gap:12px}
.frame-label{display:flex;align-items:center;gap:10px;color:#fff;font-size:15px;font-weight:800}
.frame-label b{background:#22303F;color:#8FE3FF;border-radius:6px;padding:3px 8px;font-size:12px;letter-spacing:.6px}
.frame-label i{font-style:normal;font-weight:400;color:#8DA0B4;font-size:13px}
.frame{
  width:1440px;min-height:940px;background:var(--bg);border-radius:16px;overflow:hidden;
  box-shadow:var(--sh-3);display:flex;flex-direction:column;position:relative;
}
.frame.mobile{width:390px;min-height:844px;border-radius:34px}
.frame.doc{width:1440px;min-height:auto;background:#fff;padding:48px}

/* --------------------------------------------------------------- app chrome */
.topbar{
  height:70px;background:#fff;display:flex;align-items:center;gap:18px;padding:0 22px;
  border-bottom:1px solid #E6EBF1;flex:none
}
.burger{display:flex;flex-direction:column;gap:4px;width:26px;cursor:default}
.burger span{height:3px;background:var(--br-navy);border-radius:2px}
.brand{display:flex;align-items:center;gap:10px}
svg.mark{width:34px;height:32px;display:block;flex:none}
.brand .word{font-size:17px;font-weight:800;color:var(--br-navy);letter-spacing:.6px}
.top-right{margin-left:auto;display:flex;align-items:center;gap:12px}
.greet{
  display:flex;align-items:center;gap:12px;border:1px solid #E2E8F0;border-radius:10px;
  padding:6px 14px 6px 6px;background:#fff
}
.greet .av{width:36px;height:36px;border-radius:8px;background:var(--br-blue);display:flex;align-items:center;justify-content:center}
.greet b{font-size:15px;color:var(--br-navy);font-weight:800}
.greet svg.chev{color:var(--br-navy)}
.tb-btn{width:44px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center}
.tb-btn.mail{background:var(--br-blue);color:#fff}
.tb-btn.exit{border:1.5px solid var(--br-orange);color:var(--br-orange)}
.shell{display:flex;flex:1;min-height:0}

.sidebar{width:112px;background:var(--br-cyan);flex:none;padding-top:6px}
.nav-item{
  height:78px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;
  color:#fff;font-size:11.5px;font-weight:700;text-align:center;line-height:1.15
}
.nav-item.active{background:var(--br-orange)}
.nav-item.sub{background:#0E90CE}
.main{flex:1;min-width:0;padding:22px 26px 34px;display:flex;flex-direction:column;gap:18px}

/* ------------------------------------------------------------- primitivas */
.card{background:var(--surface);border-radius:var(--r-lg);box-shadow:var(--sh-1);padding:22px}
.card.flat{box-shadow:none;border:1px solid var(--line)}
.card-head{display:flex;align-items:center;gap:12px;padding-bottom:14px;border-bottom:1px solid var(--line);margin-bottom:18px}
.card-head .ico{width:34px;height:34px;border-radius:10px;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center;flex:none}
.card-head h3{font-size:18px;font-weight:800;color:var(--br-navy)}
.card-head .right{margin-left:auto;font-size:13px;font-weight:700;color:var(--br-blue-600)}
.panel-blue{background:var(--br-blue);color:#fff;border-radius:var(--r-lg);padding:22px}
.panel-navy{background:var(--br-navy);color:#fff;border-radius:var(--r-lg);padding:22px}

h1.page{font-size:26px;font-weight:800;color:var(--br-navy);letter-spacing:-.2px}
p.page-sub{font-size:14px;color:var(--ink-2);margin-top:4px;line-height:1.5}
.crumb{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink-3);font-weight:600}
.crumb b{color:var(--br-blue-600);font-weight:700}
.page-head{display:flex;align-items:flex-start;gap:16px}
.page-head .actions{margin-left:auto;display:flex;gap:10px;align-items:center}

.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:9px;height:44px;padding:0 22px;
  border-radius:10px;font-size:15px;font-weight:800;border:1.5px solid transparent;white-space:nowrap
}
.btn.sm{height:36px;padding:0 15px;font-size:13.5px;border-radius:8px}
.btn.lg{height:52px;padding:0 30px;font-size:16px}
.btn.block{width:100%}
.btn-primary{background:var(--br-orange);color:#fff}
.btn-blue{background:var(--br-blue);color:#fff}
.btn-outline{border-color:var(--br-blue);color:var(--br-blue);background:#fff}
.btn-outline-orange{border-color:var(--br-orange);color:var(--br-orange);background:#fff}
.btn-ghost{color:var(--ink-2);background:transparent}
.btn-danger{background:#fff;border-color:var(--err);color:var(--err)}
.btn.disabled{background:#DDE4EC;color:#98A6B5;border-color:transparent}

.field{display:flex;flex-direction:column;gap:7px}
.label{font-size:13px;font-weight:800;color:var(--ink-2);letter-spacing:.1px}
.label .opt{font-weight:600;color:var(--ink-3)}
.input{
  height:50px;border:1.5px solid var(--line-strong);border-radius:10px;background:#fff;
  display:flex;align-items:center;gap:10px;padding:0 14px;font-size:15px;color:var(--ink)
}
.input .ph{color:#98A6B5}
.input .pre{color:var(--ink-3);font-weight:800;padding-right:10px;border-right:1px solid var(--line);height:26px;display:flex;align-items:center}
.input .suf{margin-left:auto;color:var(--ink-3);font-size:13px;font-weight:700}
.input.focus{border-color:var(--br-blue);box-shadow:0 0 0 4px rgba(0,82,155,.12)}
.input.err{border-color:var(--err);box-shadow:0 0 0 4px rgba(198,40,40,.10)}
.input.ok{border-color:var(--ok)}
.input.big{height:64px;font-size:26px;font-weight:800;color:var(--br-navy)}
.input.ro{background:#F4F7FA;color:var(--ink-2)}
.hint{font-size:12.5px;color:var(--ink-3);line-height:1.45}
.hint.error{color:var(--err);font-weight:700}
.hint.ok{color:var(--ok);font-weight:700}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.stack{display:flex;flex-direction:column;gap:16px}
.stack.sm{gap:10px}
.stack.lg{gap:24px}
.hstack{display:flex;align-items:center;gap:12px}
.spacer{flex:1}

.tabs{display:flex;gap:6px;background:#E4EAF1;padding:5px;border-radius:12px}
.tab{flex:1;height:42px;display:flex;align-items:center;justify-content:center;gap:8px;border-radius:9px;font-size:14px;font-weight:800;color:var(--ink-2)}
.tab.active{background:#fff;color:var(--br-blue);box-shadow:var(--sh-1)}

.stepper{display:flex;align-items:center;gap:0;background:#fff;border-radius:var(--r-lg);padding:16px 22px;box-shadow:var(--sh-1)}
.stepper .st{display:flex;align-items:center;gap:10px}
.stepper .dot{width:30px;height:30px;border-radius:50%;background:#E4EAF1;color:#8A9AAB;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;flex:none}
.stepper .st span{font-size:13.5px;font-weight:700;color:var(--ink-3);white-space:nowrap}
.stepper .st.done .dot{background:var(--ok);color:#fff}
.stepper .st.done span{color:var(--ink-2)}
.stepper .st.active .dot{background:var(--br-orange);color:#fff}
.stepper .st.active span{color:var(--br-navy);font-weight:800}
.stepper .bar{flex:1;height:2px;background:#E4EAF1;margin:0 14px;min-width:24px}
.stepper .bar.done{background:var(--ok)}

.alert{display:flex;gap:12px;border-radius:12px;padding:14px 16px;font-size:13.5px;line-height:1.5;border:1px solid transparent}
.alert b{display:block;font-size:14px;margin-bottom:2px}
.alert .ai{flex:none;margin-top:1px}
.alert.info{background:var(--info-bg);border-color:#C7DEF3;color:#0A4F84}
.alert.ok{background:var(--ok-bg);border-color:#BFE6CF;color:#0B6438}
.alert.warn{background:var(--warn-bg);border-color:#F3DFB4;color:#8A5B0A}
.alert.err{background:var(--err-bg);border-color:#F5C9C9;color:#9B1D1D}

.badge{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px;border-radius:999px;font-size:11.5px;font-weight:800;letter-spacing:.2px}
.badge.ok{background:var(--ok-bg);color:var(--ok)}
.badge.warn{background:var(--warn-bg);color:var(--warn)}
.badge.err{background:var(--err-bg);color:var(--err)}
.badge.info{background:var(--info-bg);color:var(--info)}
.badge.neutral{background:#EDF1F6;color:var(--ink-2)}
.badge.orange{background:var(--br-orange-050);color:var(--br-orange-600)}

.rowitem{display:flex;align-items:center;gap:14px;padding:16px;border:1px solid var(--line);border-radius:12px;background:#fff}
.rowitem.sel{border-color:var(--br-blue);box-shadow:0 0 0 3px rgba(0,82,155,.10);background:#F7FBFE}
.rowitem .ic{width:44px;height:44px;border-radius:12px;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center;flex:none}
.rowitem .tx b{display:block;font-size:15px;font-weight:800;color:var(--br-navy)}
.rowitem .tx span{font-size:13px;color:var(--ink-3)}
.rowitem .rt{margin-left:auto;text-align:right}
.rowitem .rt b{display:block;font-size:15px;font-weight:800;color:var(--br-navy)}
.rowitem .rt span{font-size:12.5px;color:var(--ink-3)}
.radio{width:22px;height:22px;border-radius:50%;border:2px solid var(--line-strong);flex:none}
.radio.on{border-color:var(--br-blue);box-shadow:inset 0 0 0 4px #fff;background:var(--br-blue)}
.check{width:22px;height:22px;border-radius:6px;border:2px solid var(--line-strong);flex:none;display:flex;align-items:center;justify-content:center;color:#fff}
.check.on{background:var(--br-blue);border-color:var(--br-blue)}
.switch{width:46px;height:26px;border-radius:999px;background:#CBD5E1;position:relative;flex:none}
.switch i{position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:var(--sh-1)}
.switch.on{background:var(--ok)}
.switch.on i{left:23px}

.kv{display:flex;align-items:flex-start;gap:16px;padding:11px 0;border-bottom:1px dashed var(--line)}
.kv:last-child{border-bottom:0}
.kv .k{font-size:13.5px;color:var(--ink-3);font-weight:700;width:210px;flex:none}
.kv .v{font-size:14px;color:var(--ink);font-weight:700;text-align:right;margin-left:auto;line-height:1.45}
.kv .v small{display:block;font-size:12px;color:var(--ink-3);font-weight:600}

.amount{font-size:44px;font-weight:800;color:var(--br-navy);letter-spacing:-1px;line-height:1}
.amount small{font-size:18px;font-weight:800;color:var(--ink-3);letter-spacing:0}
.amount.lg{font-size:56px}
.amount.white{color:#fff}
.amount.ok{color:var(--ok)}

.otp{display:flex;gap:12px}
.otp .b{
  width:58px;height:66px;border-radius:12px;border:1.5px solid var(--line-strong);background:#fff;
  display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800;color:var(--br-navy)
}
.otp .b.on{border-color:var(--br-blue);background:#F7FBFE}
.otp .b.cursor{border-color:var(--br-blue);box-shadow:0 0 0 4px rgba(0,82,155,.12)}
.otp .b.err{border-color:var(--err);background:#FDF4F4}

.table{width:100%;border-collapse:collapse;font-size:13.5px}
.table th{
  text-align:left;font-size:11.5px;letter-spacing:.5px;text-transform:uppercase;color:var(--ink-3);
  font-weight:800;padding:0 14px 10px;border-bottom:1px solid var(--line)
}
.table td{padding:14px;border-bottom:1px solid #EEF2F7;color:var(--ink-2);font-weight:600}
.table td b{color:var(--br-navy);font-weight:800}
.table tr:last-child td{border-bottom:0}
.table td.num{text-align:right;font-weight:800;color:var(--br-navy)}

.progress{height:8px;border-radius:999px;background:#E4EAF1;overflow:hidden}
.progress i{display:block;height:100%;background:var(--br-cyan);border-radius:999px}
.progress i.warn{background:var(--br-orange)}
.progress i.err{background:var(--err)}

.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:46px 20px;text-align:center}
.empty .ic{width:74px;height:74px;border-radius:50%;background:#EDF3F9;color:var(--br-cyan);display:flex;align-items:center;justify-content:center}
.empty b{font-size:16px;color:var(--br-navy)}
.empty span{font-size:13.5px;color:var(--ink-3);max-width:340px;line-height:1.5}

/* modal sobre la pantalla */
.scrim{position:absolute;inset:0;background:rgba(9,26,44,.55);display:flex;align-items:center;justify-content:center;padding:40px}
.modal{width:620px;background:#fff;border-radius:18px;box-shadow:var(--sh-3);overflow:hidden}
.modal.sm{width:480px}
.modal.lg{width:860px}
.modal-head{display:flex;align-items:center;gap:12px;padding:20px 24px;border-bottom:1px solid var(--line)}
.modal-head h3{font-size:19px;font-weight:800;color:var(--br-navy)}
.modal-head .x{margin-left:auto;color:var(--ink-3)}
.modal-body{padding:24px}
.modal-foot{padding:18px 24px;border-top:1px solid var(--line);display:flex;gap:12px;justify-content:flex-end;background:#F8FAFC}

.toast{display:flex;gap:12px;align-items:flex-start;background:#0F2438;color:#fff;border-radius:12px;padding:14px 16px;box-shadow:var(--sh-2);width:380px}
.toast b{font-size:14px;display:block}
.toast span{font-size:12.5px;color:#B9CADA;line-height:1.45}

/* especificos */
.qr-box{background:#fff;border:2px solid var(--line);border-radius:16px;padding:18px;display:flex;align-items:center;justify-content:center}
.scanner{
  position:relative;background:#10202E;border-radius:16px;overflow:hidden;
  display:flex;align-items:center;justify-content:center
}
.scanner .reticle{width:250px;height:250px;border-radius:18px;box-shadow:0 0 0 2000px rgba(6,17,27,.55);position:relative}
.scanner .reticle i{position:absolute;width:34px;height:34px;border:4px solid var(--br-orange)}
.scanner .reticle i.tl{top:-2px;left:-2px;border-right:0;border-bottom:0;border-radius:12px 0 0 0}
.scanner .reticle i.tr{top:-2px;right:-2px;border-left:0;border-bottom:0;border-radius:0 12px 0 0}
.scanner .reticle i.bl{bottom:-2px;left:-2px;border-right:0;border-top:0;border-radius:0 0 0 12px}
.scanner .reticle i.br{bottom:-2px;right:-2px;border-left:0;border-top:0;border-radius:0 0 12px 0}
.scanner .laser{position:absolute;left:0;right:0;top:50%;height:2px;background:var(--br-orange);opacity:.85}
.scanner .cap{position:absolute;bottom:18px;left:0;right:0;text-align:center;color:#DCE9F5;font-size:13px;font-weight:700}

.receipt{background:#fff;border-radius:16px;box-shadow:var(--sh-2);overflow:hidden;width:100%}
.receipt .rh{background:var(--ok-bg);padding:26px;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center}
.receipt .rh .ic{width:64px;height:64px;border-radius:50%;background:var(--ok);color:#fff;display:flex;align-items:center;justify-content:center}
.receipt .rb{padding:22px 26px}
.notch{height:22px;position:relative;background:#fff}
.notch:before,.notch:after{content:"";position:absolute;top:-11px;width:22px;height:22px;border-radius:50%;background:var(--bg)}
.notch:before{left:-11px}.notch:after{right:-11px}
.dashed{border-top:2px dashed var(--line);margin:0 26px}

.limit-bar{display:flex;flex-direction:column;gap:8px}
.limit-bar .lt{display:flex;justify-content:space-between;font-size:12.5px;font-weight:700;color:var(--ink-2)}

.phone-status{height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 22px;font-size:13px;font-weight:800;color:var(--br-navy)}
.frame.mobile .kv .k{width:112px}
.frame.mobile .kv .v{font-size:13px}
.phone-nav{height:64px;border-top:1px solid var(--line);display:flex;align-items:center;justify-content:space-around;background:#fff}

.swatch{border-radius:12px;height:88px;display:flex;align-items:flex-end;padding:10px;color:#fff;font-size:11.5px;font-weight:800;box-shadow:var(--sh-1)}
.swatch.dark{color:var(--br-navy)}
.type-row{display:flex;align-items:baseline;gap:18px;padding:12px 0;border-bottom:1px solid var(--line)}
.type-row .meta{font-size:12px;color:var(--ink-3);font-weight:700;width:200px;flex:none}

.flowmap{display:flex;flex-direction:column;gap:22px}
.flowline{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.node{
  border:1.5px solid var(--line-strong);background:#fff;border-radius:12px;padding:12px 16px;
  font-size:13px;font-weight:800;color:var(--br-navy);box-shadow:var(--sh-1);min-width:120px;text-align:center
}
.node small{display:block;font-weight:600;color:var(--ink-3);font-size:11.5px;margin-top:3px}
.node.start{background:var(--br-blue);color:#fff;border-color:var(--br-blue)}
.node.start small{color:#BBD9F1}
.node.sec{background:var(--br-orange-050);border-color:#F6C99A}
.node.end{background:var(--ok-bg);border-color:#BFE6CF;color:#0B6438}
.node.err{background:var(--err-bg);border-color:#F5C9C9;color:#9B1D1D}
.arrow{color:var(--ink-3);flex:none}
"""

# ------------------------------------------------------------------- iconos
def ico(name, size=22, sw=1.9):
    p = {
 "home":'<path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.5V21h13V9.5"/>',
 "products":'<rect x="3" y="4" width="8" height="16" rx="1.5"/><rect x="13" y="4" width="8" height="16" rx="1.5"/>',
 "transfer":'<path d="M4 8h13"/><path d="M14 5l3 3-3 3"/><path d="M20 16H7"/><path d="M10 13l-3 3 3 3"/>',
 "pay":'<circle cx="12" cy="12" r="9"/><path d="M12 7v10"/><path d="M14.6 9.4c-.6-.6-1.6-.9-2.6-.9-1.4 0-2.5.7-2.5 1.9 0 2.6 5.2 1.3 5.2 3.9 0 1.2-1.1 2-2.7 2-1.1 0-2.1-.4-2.7-1"/>',
 "manage":'<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v5h4"/><path d="M9 13h6"/><path d="M9 17h6"/>',
 "admin":'<path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h16"/><circle cx="9" cy="7" r="2" fill="currentColor"/><circle cx="15" cy="12" r="2" fill="currentColor"/><circle cx="10" cy="17" r="2" fill="currentColor"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/>',
 "exit":'<path d="M14 4h5v16h-5"/><path d="M4 12h11"/><path d="m11 8 4 4-4 4"/>',
 "user":'<circle cx="12" cy="8.5" r="3.5"/><path d="M5 20c1.2-3.5 4-5.2 7-5.2s5.8 1.7 7 5.2"/>',
 "chev":'<path d="m6 9 6 6 6-6"/>',
 "chevr":'<path d="m9 6 6 6-6 6"/>',
 "back":'<path d="M15 6 9 12l6 6"/>',
 "arrow":'<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
 "plus":'<path d="M12 5v14"/><path d="M5 12h14"/>',
 "check":'<path d="m5 12.5 4.5 4.5L19 7.5"/>',
 "x":'<path d="m6 6 12 12"/><path d="m18 6-12 12"/>',
 "search":'<circle cx="11" cy="11" r="7"/><path d="m16.5 16.5 4 4"/>',
 "qr":'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3z" fill="currentColor"/><path d="M20 14v3"/><path d="M14 20h7"/>',
 "scan":'<path d="M4 8V5.5A1.5 1.5 0 0 1 5.5 4H8"/><path d="M16 4h2.5A1.5 1.5 0 0 1 20 5.5V8"/><path d="M20 16v2.5a1.5 1.5 0 0 1-1.5 1.5H16"/><path d="M8 20H5.5A1.5 1.5 0 0 1 4 18.5V16"/><path d="M4 12h16"/>',
 "phone":'<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
 "id":'<rect x="2.5" y="5" width="19" height="14" rx="2"/><circle cx="8.5" cy="11" r="2.2"/><path d="M5 16.2c.7-1.5 2-2.2 3.5-2.2s2.8.7 3.5 2.2"/><path d="M15 10h4"/><path d="M15 14h4"/>',
 "at":'<circle cx="12" cy="12" r="4"/><path d="M16 8v5.5a2.5 2.5 0 0 0 5 0V12a9 9 0 1 0-3.6 7.2"/>',
 "store":'<path d="M4 9h16l-1 11H5z"/><path d="M4 9 5.5 4h13L20 9"/><path d="M9.5 13.5h5"/>',
 "lock":'<rect x="4.5" y="10" width="15" height="11" rx="2"/><path d="M8 10V7.5a4 4 0 0 1 8 0V10"/>',
 "shield":'<path d="M12 3 5 6v6c0 4.2 2.9 7.8 7 9 4.1-1.2 7-4.8 7-9V6z"/>',
 "shieldcheck":'<path d="M12 3 5 6v6c0 4.2 2.9 7.8 7 9 4.1-1.2 7-4.8 7-9V6z"/><path d="m9 12 2.2 2.2L15.5 10"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5.4l3.4 2"/>',
 "bell":'<path d="M6.5 10a5.5 5.5 0 0 1 11 0c0 4 1.5 5.5 1.5 5.5H5S6.5 14 6.5 10Z"/><path d="M10 19a2 2 0 0 0 4 0"/>',
 "download":'<path d="M12 4v10"/><path d="m8 11 4 4 4-4"/><path d="M5 19h14"/>',
 "share":'<circle cx="6" cy="12" r="2.5"/><circle cx="17.5" cy="6" r="2.5"/><circle cx="17.5" cy="18" r="2.5"/><path d="m8.3 10.8 6.9-3.6"/><path d="m8.3 13.2 6.9 3.6"/>',
 "copy":'<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/>',
 "edit":'<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m14.5 5.5 4 4"/>',
 "trash":'<path d="M4.5 7h15"/><path d="M9 7V5h6v2"/><path d="M6.5 7 7.6 20h8.8L17.5 7"/>',
 "refresh":'<path d="M20 12a8 8 0 1 1-2.6-5.9"/><path d="M20 4v5h-5"/>',
 "device":'<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8"/><path d="M12 16v4"/>',
 "star":'<path d="m12 4 2.4 5 5.6.7-4.1 3.8 1.1 5.5L12 16.4 7 19l1.1-5.5L4 9.7 9.6 9z"/>',
 "heart":'<path d="M12 20s-7-4.4-7-9.2A3.9 3.9 0 0 1 12 8a3.9 3.9 0 0 1 7 2.8C19 15.6 12 20 12 20Z"/>',
 "request":'<path d="M20 8H7"/><path d="m10 5-3 3 3 3"/><path d="M4 16h13"/><path d="m14 13 3 3-3 3"/>',
 "info":'<circle cx="12" cy="12" r="9"/><path d="M12 11v6"/><circle cx="12" cy="7.6" r="1.1" fill="currentColor" stroke="none"/>',
 "alert":'<path d="M12 4 2.8 20h18.4z"/><path d="M12 10v4.5"/><circle cx="12" cy="17.3" r="1.1" fill="currentColor" stroke="none"/>',
 "list":'<path d="M8 6h12"/><path d="M8 12h12"/><path d="M8 18h12"/><circle cx="4.2" cy="6" r="1.2" fill="currentColor" stroke="none"/><circle cx="4.2" cy="12" r="1.2" fill="currentColor" stroke="none"/><circle cx="4.2" cy="18" r="1.2" fill="currentColor" stroke="none"/>',
 "filter":'<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
 "print":'<path d="M7 9V4h10v5"/><rect x="4" y="9" width="16" height="7" rx="2"/><path d="M7 14h10v6H7z"/>',
 "eye":'<path d="M2.5 12S6 6 12 6s9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6Z"/><circle cx="12" cy="12" r="2.8"/>',
 "key":'<circle cx="8" cy="12" r="4"/><path d="M12 12h9"/><path d="M17 12v3.5"/><path d="M20 12v2.5"/>',
 "fingerprint":'<path d="M12 4a8 8 0 0 1 8 8v2"/><path d="M4 12a8 8 0 0 1 4-6.9"/><path d="M8 12a4 4 0 0 1 8 0v3.5"/><path d="M12 12v5"/><path d="M6.5 17.5c1-1.4 1.5-3 1.5-4.6"/><path d="M16 19c.6-1 1-2.2 1-3.4"/>',
 "money":'<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5"/><path d="M18 9.5v5"/>',
 "bank":'<path d="M3.5 9.5 12 4l8.5 5.5"/><path d="M5.5 10v8"/><path d="M10 10v8"/><path d="M14 10v8"/><path d="M18.5 10v8"/><path d="M3.5 20.5h17"/>',
 "sliders":'<path d="M5 4v7"/><path d="M5 15v5"/><path d="M12 4v3"/><path d="M12 11v9"/><path d="M19 4v11"/><path d="M19 19v1"/><circle cx="5" cy="13" r="2"/><circle cx="12" cy="9" r="2"/><circle cx="19" cy="17" r="2"/>',
 "link":'<path d="M10.5 13.5a4 4 0 0 0 5.7 0l2.3-2.3a4 4 0 0 0-5.7-5.7L11.6 6.7"/><path d="M13.5 10.5a4 4 0 0 0-5.7 0l-2.3 2.3a4 4 0 0 0 5.7 5.7l1.2-1.2"/>',
 "wa":'<path d="M4 20l1.4-4A8 8 0 1 1 8.5 19z"/><path d="M9 10c.4 2 2 3.6 4 4l1-1.2 2 .9-.4 1.6c-2.6.5-5.9-2.4-6.6-5.3L10.5 9l-.9-2H8z" fill="currentColor" stroke="none"/>',
 "camera":'<path d="M4 8h3l1.5-2h7L17 8h3a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1Z"/><circle cx="12" cy="13" r="3.4"/>',
 "upload":'<path d="M12 19V8"/><path d="m8 11 4-3 4 3"/><path d="M5 20h14"/>',
 "calendar":'<rect x="3.5" y="5" width="17" height="16" rx="2"/><path d="M3.5 10h17"/><path d="M8 3v4"/><path d="M16 3v4"/>',
 "arrowup":'<path d="M12 19V5"/><path d="m6 11 6-6 6 6"/>',
 "arrowdown":'<path d="M12 5v14"/><path d="m6 13 6 6 6-6"/>',
 "spinner":'<path d="M12 3a9 9 0 1 0 9 9" />',
 "hand":'<path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M12 10.5V4.8a1.5 1.5 0 0 1 3 0V11"/><path d="M15 11V6.8a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-1a5 5 0 0 1-4.4-2.6L5 15.2a1.6 1.6 0 0 1 2.6-1.8L9 15"/>',
 "doc":'<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v5h4"/><path d="M9 12h6"/><path d="M9 16h4"/>',
 "wifi":'<path d="M4 9a12 12 0 0 1 16 0"/><path d="M7 12.5a8 8 0 0 1 10 0"/><path d="M10 16a4 4 0 0 1 4 0"/><circle cx="12" cy="19" r="1.2" fill="currentColor" stroke="none"/>',
    }.get(name, '<circle cx="12" cy="12" r="9"/>')
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>')

LOGO = ('<svg class="mark" viewBox="0 0 44 40" fill="none">'
        '<path d="M8 4h14c6 0 9.6 3 9.6 7.6 0 3.2-1.8 5.6-4.6 6.6 3.4.9 5.6 3.5 5.6 7.2 0 5.2-4 8.6-10.6 8.6H8z" fill="#00396B"/>'
        '<path d="M14.5 10.5h7c2.4 0 3.8 1.2 3.8 3.1s-1.4 3.2-3.8 3.2h-7z" fill="#fff"/>'
        '<path d="M14.5 22h8c2.6 0 4.2 1.3 4.2 3.3s-1.6 3.4-4.2 3.4h-8z" fill="#fff"/>'
        '<path d="M2 33.5c8-5.4 20-8.6 40-9.4-16 4.6-27.4 9.4-33.6 13.4z" fill="#F58220"/>'
        '</svg>')

# QR sintetico reproducible
def qr(size=180, seed=7, fg="#0E1B26"):
    rnd = random.Random(seed)
    n, q = 25, 2
    m = size / (n + q * 2)
    cells = []
    def finder(ox, oy):
        cells.append(f'<rect x="{(ox+q)*m:.2f}" y="{(oy+q)*m:.2f}" width="{7*m:.2f}" height="{7*m:.2f}" fill="{fg}"/>')
        cells.append(f'<rect x="{(ox+q+1)*m:.2f}" y="{(oy+q+1)*m:.2f}" width="{5*m:.2f}" height="{5*m:.2f}" fill="#fff"/>')
        cells.append(f'<rect x="{(ox+q+2)*m:.2f}" y="{(oy+q+2)*m:.2f}" width="{3*m:.2f}" height="{3*m:.2f}" fill="{fg}"/>')
    def infinder(x, y):
        return ((x < 8 and y < 8) or (x > n - 9 and y < 8) or (x < 8 and y > n - 9))
    for y in range(n):
        for x in range(n):
            if infinder(x, y):
                continue
            if rnd.random() < .46:
                cells.append(f'<rect x="{(x+q)*m:.2f}" y="{(y+q)*m:.2f}" width="{m:.2f}" height="{m:.2f}" fill="{fg}"/>')
    finder(0, 0); finder(n - 7, 0); finder(0, n - 7)
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
            f'<rect width="{size}" height="{size}" fill="#fff"/>' + "".join(cells) + '</svg>')

# ------------------------------------------------------------------ chrome
NAV = [("home", "Inicio"), ("products", "Mis Productos"), ("transfer", "Transferir"),
       ("pay", "Pagar"), ("manage", "Gestionar"), ("admin", "Administrar")]

def sidebar(active="Transferir"):
    out = ['<nav class="sidebar">']
    for k, lab in NAV:
        cls = "nav-item active" if lab == active else "nav-item"
        out.append(f'<div class="{cls}">{ico(k,26,1.8)}<span>{lab}</span></div>')
    out.append('</nav>')
    return "".join(out)

def topbar(user="EDWARD ALEJANDRO FIALLO SA..."):
    return f"""<header class="topbar">
  <div class="burger"><span></span><span></span><span></span></div>
  <div class="brand">{LOGO}<div class="word">BANRESERVAS</div></div>
  <div class="top-right">
    <div class="greet"><div class="av">{ico('user',20)}</div><b>Hola, {user}</b>{ico('chev',18)}</div>
    <div class="tb-btn mail">{ico('mail',20)}</div>
    <div class="tb-btn exit">{ico('exit',20)}</div>
  </div>
</header>"""

FRAMES = []   # (grupo, id, titulo, nota, html)

def frame(gid, fid, title, note, body, nav="Transferir", chrome=True, kind="", scrim=""):
    cls = "frame" + (f" {kind}" if kind else "")
    if chrome:
        inner = f'{topbar()}<div class="shell">{sidebar(nav)}<main class="main">{body}</main></div>{scrim}'
    else:
        inner = body
    FRAMES.append((gid, f"""<div class="frame-wrap" id="{fid}">
  <div class="frame-label"><b>{fid}</b> {title} <i>{note}</i></div>
  <section class="{cls}">{inner}</section>
</div>"""))

def page_head(title, sub="", crumb=None, actions=""):
    c = ""
    if crumb:
        parts = f' {ico("chevr",13,2.4)} '.join(crumb[:-1]) + f' {ico("chevr",13,2.4)} <b>{crumb[-1]}</b>'
        c = f'<div class="crumb">{parts}</div>'
    s = f'<p class="page-sub">{sub}</p>' if sub else ""
    a = f'<div class="actions">{actions}</div>' if actions else ""
    return f'<div class="stack sm">{c}<div class="page-head"><div><h1 class="page">{title}</h1>{s}</div>{a}</div></div>'

def stepper(steps, current):
    out = ['<div class="stepper">']
    for i, s in enumerate(steps):
        st = "done" if i < current else ("active" if i == current else "")
        dot = ico("check", 16, 2.6) if i < current else str(i + 1)
        out.append(f'<div class="st {st}"><div class="dot">{dot}</div><span>{s}</span></div>')
        if i < len(steps) - 1:
            out.append(f'<div class="bar {"done" if i < current else ""}"></div>')
    out.append('</div>')
    return "".join(out)

def alert(kind, title, text, icon=None):
    icon = icon or {"info": "info", "ok": "check", "warn": "alert", "err": "alert"}[kind]
    return f'<div class="alert {kind}"><div class="ai">{ico(icon,20)}</div><div><b>{title}</b>{text}</div></div>'

def kv(rows):
    return "".join(f'<div class="kv"><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in rows)

def field(label, inner, hint="", hint_cls="hint"):
    h = f'<div class="{hint_cls}">{hint}</div>' if hint else ""
    return f'<div class="field"><div class="label">{label}</div>{inner}{h}</div>'

def inp(text, ph=False, cls="", pre="", suf="", icon=""):
    a = f'<span class="pre">{pre}</span>' if pre else ""
    b = f'<span class="suf">{suf}</span>' if suf else ""
    i = f'{ico(icon,20)}' if icon else ""
    t = f'<span class="ph">{text}</span>' if ph else f'<span>{text}</span>'
    return f'<div class="input {cls}">{i}{a}{t}{b}</div>'

def acct_row(name, num, bal, sel=False, icon="money"):
    return (f'<div class="rowitem {"sel" if sel else ""}"><div class="radio {"on" if sel else ""}"></div>'
            f'<div class="ic">{ico(icon,22)}</div><div class="tx"><b>{name}</b><span>{num}</span></div>'
            f'<div class="rt"><b>{bal}</b><span>Balance disponible</span></div></div>')

# =========================================================== A. FUNDAMENTOS
def g_fundamentos():
    # A1 Portada
    body = f"""
<div class="stack lg">
  <div class="hstack" style="gap:18px">{LOGO}
    <div><div style="font-size:13px;font-weight:800;letter-spacing:2px;color:var(--br-orange)">BANRESERVAS · TUBANCO</div>
    <div style="font-size:40px;font-weight:800;color:var(--br-navy);letter-spacing:-1px;line-height:1.1">Pago Instantáneo RD<br>Internet Banking · Kit de pantallas</div></div>
  </div>
  <p style="font-size:16px;line-height:1.65;color:var(--ink-2);max-width:980px">
    Propuesta de experiencia para el sistema de pagos inmediatos (IPS) dentro del Internet Banking de Banreservas,
    modelada sobre las prácticas de <b>Bre-B</b> (Colombia), <b>Pix</b> (Brasil), <b>SPEI/DiMo</b> (México) y <b>Transfer 3.0</b> (Argentina):
    alias/llaves como identificador de cobro, envío y solicitud de dinero 24/7, QR interoperable EMVCo y liquidación en segundos.
  </p>
  <div class="grid-4">
    <div class="card"><div class="card-head"><div class="ico">{ico('arrow',20)}</div><h3>Enviar pago</h3></div>
      <p class="hint" style="font-size:13.5px">Alias, cuenta o contacto · confirmación de nombre · 2FA · comprobante</p><div style="margin-top:12px" class="badge info">12 pantallas</div></div>
    <div class="card"><div class="card-head"><div class="ico">{ico('request',20)}</div><h3>Solicitar pago</h3></div>
      <p class="hint" style="font-size:13.5px">Cobros con vencimiento, enlace y QR, bandeja de recibidas</p><div style="margin-top:12px" class="badge info">9 pantallas</div></div>
    <div class="card"><div class="card-head"><div class="ico">{ico('qr',20)}</div><h3>Pagar con QR</h3></div>
      <p class="hint" style="font-size:13.5px">QR estático y dinámico EMVCo, mi QR de cobro, errores</p><div style="margin-top:12px" class="badge info">9 pantallas</div></div>
    <div class="card"><div class="card-head"><div class="ico">{ico('at',20)}</div><h3>Mis Alias</h3></div>
      <p class="hint" style="font-size:13.5px">Registro, verificación, portabilidad, administración</p><div style="margin-top:12px" class="badge info">12 pantallas</div></div>
  </div>
  <div class="grid-2">
    <div class="panel-navy stack sm">
      <div class="hstack">{ico('shieldcheck',22)}<b style="font-size:17px">Seguridad incorporada en cada flujo</b></div>
      <ul style="font-size:13.5px;line-height:1.9;color:#C9DCEC;padding-left:20px">
        <li>Doble factor: aprobación push en la App TuBanco, token blando y OTP SMS/correo</li>
        <li>Confirmación del nombre del beneficiario antes de autorizar (anti-error y anti-estafa)</li>
        <li>Límites por transacción/día configurables con enfriamiento de 24 h</li>
        <li>Dispositivos de confianza, sello anti-phishing y monitoreo antifraude en tiempo real</li>
        <li>Comprobante con referencia única, trazabilidad y canal de devolución/reclamación</li>
      </ul>
    </div>
    <div class="card stack sm">
      <div class="card-head"><div class="ico">{ico('info',20)}</div><h3>Cómo usar este archivo en Figma</h3></div>
      <ol style="font-size:13.5px;line-height:1.95;color:var(--ink-2);padding-left:20px">
        <li>Instala el plugin <b>html.to.design</b> en Figma.</li>
        <li>Importa <b>index.html</b> (o la URL publicada) con ancho 1440 px.</li>
        <li>Cada tarjeta se convierte en un frame independiente, con auto-layout y SVG editables.</li>
        <li>Los colores están como variables CSS: se mapean a estilos/variables de Figma.</li>
      </ol>
      <div class="alert info"><div class="ai">{ico('info',20)}</div><div>Nomenclatura de frames: <b>[Grupo]-[N°] Nombre</b>, lista para agrupar por página en Figma.</div></div>
    </div>
  </div>
</div>"""
    frame("A", "A-01", "Portada del kit", "1440 · documento", body, chrome=False, kind="doc")

    # A2 Design system
    sw = lambda c, n, h: f'<div class="swatch{" dark" if h else ""}" style="background:{c}">{n}<br>{c}</div>'
    body = f"""
<div class="stack lg">
  <h1 class="page" style="font-size:32px">Fundamentos de diseño</h1>
  <div class="stack sm"><div class="label">Color de marca</div>
    <div class="grid-4">{sw('#00396B','Navy / titulares',0)}{sw('#00529B','Azul primario',0)}{sw('#0A6FB7','Azul enlaces',0)}{sw('#1BA5DF','Cyan menú',0)}</div>
    <div class="grid-4" style="margin-top:14px">{sw('#F58220','Naranja acción',0)}{sw('#DC6E10','Naranja hover',0)}{sw('#E7F5FC','Cyan 050',1)}{sw('#FFF3E7','Naranja 050',1)}</div>
  </div>
  <div class="stack sm"><div class="label">Semántico y neutrales</div>
    <div class="grid-4">{sw('#0F8A4D','Éxito',0)}{sw('#B7791F','Advertencia',0)}{sw('#C62828','Error',0)}{sw('#1B2733','Texto',0)}</div>
    <div class="grid-4" style="margin-top:14px">{sw('#48586B','Texto 2',0)}{sw('#7A8A9C','Texto 3',0)}{sw('#E2E8F0','Línea',1)}{sw('#EFF2F6','Fondo app',1)}</div>
  </div>
  <div class="grid-2">
    <div class="stack sm"><div class="label">Tipografía · Nunito Sans</div>
      <div class="type-row"><div class="meta">Display / 44 / 800</div><div style="font-size:44px;font-weight:800;color:var(--br-navy);letter-spacing:-1px">DOP 2,383.33</div></div>
      <div class="type-row"><div class="meta">Título página / 26 / 800</div><div style="font-size:26px;font-weight:800;color:var(--br-navy)">Enviar pago instantáneo</div></div>
      <div class="type-row"><div class="meta">Título tarjeta / 18 / 800</div><div style="font-size:18px;font-weight:800;color:var(--br-navy)">Datos del beneficiario</div></div>
      <div class="type-row"><div class="meta">Cuerpo / 15 / 600</div><div style="font-size:15px;font-weight:600">Confirma el nombre antes de enviar.</div></div>
      <div class="type-row"><div class="meta">Etiqueta / 13 / 800</div><div class="label">CUENTA DE ORIGEN</div></div>
      <div class="type-row"><div class="meta">Ayuda / 12.5 / 600</div><div class="hint">La transferencia se acredita en segundos, 24/7.</div></div>
    </div>
    <div class="stack sm"><div class="label">Rejilla, radios y elevación</div>
      <div class="card flat stack sm">
        <div class="kv"><div class="k">Ancho de trabajo</div><div class="v">1440 px · contenido 1328 px</div></div>
        <div class="kv"><div class="k">Menú lateral</div><div class="v">112 px fijo · ítem 78 px alto</div></div>
        <div class="kv"><div class="k">Barra superior</div><div class="v">70 px</div></div>
        <div class="kv"><div class="k">Rejilla</div><div class="v">12 columnas · gutter 18 px</div></div>
        <div class="kv"><div class="k">Radios</div><div class="v">6 / 10 / 16 / 22 px</div></div>
        <div class="kv"><div class="k">Espaciado base</div><div class="v">4 px (4·8·12·16·22·26·34)</div></div>
        <div class="kv"><div class="k">Sombra 1 / 2 / 3</div><div class="v">tarjeta / flotante / modal</div></div>
      </div>
      <div class="hstack" style="gap:14px;margin-top:6px">
        <div class="card" style="width:150px;height:80px"></div>
        <div class="card" style="width:150px;height:80px;box-shadow:var(--sh-2)"></div>
        <div class="card" style="width:150px;height:80px;box-shadow:var(--sh-3)"></div>
      </div>
    </div>
  </div>
</div>"""
    frame("A", "A-02", "Design system · color y tipografía", "tokens", body, chrome=False, kind="doc")

    # A3 Componentes
    icons = ["at","qr","request","shieldcheck","lock","key","fingerprint","phone","id","store","bank","money",
             "device","bell","clock","star","link","share","download","print","filter","search","refresh","trash"]
    icon_grid = "".join(f'<div class="card flat" style="display:flex;flex-direction:column;align-items:center;gap:8px;padding:14px"><div style="color:var(--br-blue)">{ico(i,26)}</div><span class="hint" style="font-size:11px">{i}</span></div>' for i in icons)
    body = f"""
<div class="stack lg">
  <h1 class="page" style="font-size:32px">Librería de componentes</h1>
  <div class="grid-2">
    <div class="stack sm"><div class="label">Botones</div>
      <div class="hstack" style="flex-wrap:wrap">
        <div class="btn btn-primary">Continuar {ico('arrow',18)}</div>
        <div class="btn btn-blue">Confirmar</div>
        <div class="btn btn-outline">Volver</div>
        <div class="btn btn-outline-orange">Editar</div>
        <div class="btn btn-ghost">Cancelar</div>
        <div class="btn disabled">Continuar</div>
      </div>
      <div class="hstack"><div class="btn btn-primary sm">Acción sm</div><div class="btn btn-outline sm">Acción sm</div><div class="btn btn-danger sm">{ico('trash',16)} Eliminar</div></div>
    </div>
    <div class="stack sm"><div class="label">Campos</div>
      {field("Alias del beneficiario", inp("@nombredeusuario", True, icon="at"), "Escribe el alias tal como te lo compartieron")}
      {field("Monto", inp("2,500.00", False, "big", pre="DOP"))}
      <div class="grid-2">{field("Con foco", inp("809 555 1234","","focus"))}{field("Con error", inp("00", False,"err"), "El monto debe ser mayor a DOP 1.00","hint error")}</div>
    </div>
  </div>
  <div class="grid-2">
    <div class="stack sm"><div class="label">Mensajería</div>
      {alert('info','Acreditación inmediata','El dinero llega en segundos, cualquier día y hora.')}
      {alert('ok','Pago completado','Referencia PI-2026-0098231 enviada a tu correo.')}
      {alert('warn','Beneficiario nuevo','Es la primera vez que pagas a este alias. Verifica el nombre antes de continuar.')}
      {alert('err','Alias no encontrado','Revisa el alias o pide a la persona que lo verifique en su banco.')}
    </div>
    <div class="stack sm"><div class="label">Estados, badges y controles</div>
      <div class="hstack" style="flex-wrap:wrap">
        <span class="badge ok">{ico('check',13,3)} Completado</span><span class="badge warn">{ico('clock',13,2.4)} Pendiente</span>
        <span class="badge err">Rechazado</span><span class="badge info">En verificación</span>
        <span class="badge neutral">Vencido</span><span class="badge orange">Nuevo</span>
      </div>
      <div class="hstack" style="gap:22px;margin-top:6px">
        <div class="hstack"><div class="radio on"></div><span class="hint">Radio</span></div>
        <div class="hstack"><div class="check on">{ico('check',14,3)}</div><span class="hint">Check</span></div>
        <div class="hstack"><div class="switch on"><i></i></div><span class="hint">Switch on</span></div>
        <div class="hstack"><div class="switch"><i></i></div><span class="hint">off</span></div>
      </div>
      {stepper(["Destino","Monto","Revisión","Autenticación"],2)}
      <div class="tabs"><div class="tab active">{ico('at',18)} Alias</div><div class="tab">{ico('bank',18)} Cuenta</div><div class="tab">{ico('star',18)} Frecuentes</div></div>
      <div class="otp"><div class="b on">4</div><div class="b on">7</div><div class="b on">1</div><div class="b cursor"></div><div class="b"></div><div class="b"></div></div>
    </div>
  </div>
  <div class="stack sm"><div class="label">Iconografía (SVG editable)</div>
    <div style="display:grid;grid-template-columns:repeat(12,1fr);gap:12px">{icon_grid}</div>
  </div>
</div>"""
    frame("A", "A-03", "Design system · componentes", "librería", body, chrome=False, kind="doc")

    # A4 Mapa de flujos
    def node(t, s="", c=""):
        return f'<div class="node {c}">{t}{f"<small>{s}</small>" if s else ""}</div>'
    ar = f'<span class="arrow">{ico("arrow",20,2.2)}</span>'
    def line(*nodes):
        return '<div class="flowline">' + ar.join(nodes) + '</div>'
    body = f"""
<div class="stack lg">
  <h1 class="page" style="font-size:32px">Mapa de flujos · Pago Instantáneo RD</h1>
  <div class="flowmap">
    <div class="stack sm"><div class="label">1 · Registro de alias (onboarding obligatorio la primera vez)</div>
      {line(node('Hub IPS','B-03','start'),node('Qué es','C-01'),node('T&C','C-02'),node('Tipo de alias','C-03'),node('Datos','C-04'),node('OTP','C-05','sec'),node('Cuenta','C-06'),node('Confirmar','C-07'),node('Alias activo','C-08','end'))}
      {line(node('Alias tomado','C-11','err'),node('Reclamo de portabilidad','C-11'),node('OTP + validación 5 días','C-11','sec'),node('Alias portado','end'))}
    </div>
    <div class="stack sm"><div class="label">2 · Enviar pago</div>
      {line(node('Destino','D-01','start'),node('Resolver alias','D-02'),node('Confirmar nombre','D-03','sec'),node('Monto y concepto','D-05'),node('Revisión','D-06'),node('2FA push/OTP','D-07','sec'),node('Procesando','D-10'),node('Comprobante','D-11','end'))}
      {line(node('Alias inexistente','D-04','err'),node('Fondos insuficientes','D-12','err'),node('Límite excedido','D-12','err'),node('Retenido por riesgo','D-13','err'),node('Timeout / reversa','D-12','err'))}
    </div>
    <div class="stack sm"><div class="label">3 · Solicitar pago</div>
      {line(node('Nueva solicitud','E-01','start'),node('Monto y vencimiento','E-02'),node('Revisión','E-03'),node('Compartir link/QR','E-04','end'),node('Bandeja enviadas','E-05'))}
      {line(node('Notificación al pagador','E-07','start'),node('Detalle','E-08'),node('Pagar (prellenado)','E-08'),node('2FA','sec'),node('Comprobante','end'),node('Rechazar con motivo','E-09','err'))}
    </div>
    <div class="stack sm"><div class="label">4 · QR</div>
      {line(node('Hub QR','F-01','start'),node('Escanear / subir','F-02'),node('Lectura','F-03'),node('QR estático: monto','F-04'),node('QR dinámico: monto fijo','F-05'),node('2FA','F-06','sec'),node('Comprobante','F-07','end'))}
      {line(node('Mi QR de cobro','F-08','start'),node('Estático o con monto','F-08'),node('Descargar / imprimir / compartir','F-08','end'),node('QR vencido o inválido','F-09','err'))}
    </div>
    <div class="stack sm"><div class="label">5 · Seguridad y post-venta</div>
      {line(node('Panel de seguridad','G-01','sec'),node('Límites','G-02','sec'),node('Dispositivos','G-03','sec'),node('Métodos 2FA','G-04','sec'),node('Alertas','G-05','sec'),node('Alias reportados','G-06','sec'))}
      {line(node('Movimientos','G-07','start'),node('Detalle','G-07'),node('Solicitar devolución','G-08'),node('Reclamación abierta','G-08','end'))}
    </div>
  </div>
</div>"""
    frame("A", "A-04", "Mapa de flujos", "diagrama", body, chrome=False, kind="doc")

# ==================================================== B. ENTRADA AL PRODUCTO
def g_entrada():
    # B-01 Dashboard con modulo IPS
    body = f"""
<div class="stack">
  <div class="grid-2" style="grid-template-columns:1fr 380px">
    <div style="background:linear-gradient(120deg,#0B3F6B 0%,#0E5D97 55%,#1BA5DF 100%);border-radius:var(--r-lg);padding:34px;min-height:250px;display:flex;flex-direction:column;justify-content:center;color:#fff;position:relative;overflow:hidden">
      <div style="font-size:40px;font-weight:800;line-height:1.05;letter-spacing:-1px">¡Nuestra<br>dominicanidad<br><span style="color:var(--br-orange)">nos hace invencibles!</span></div>
      <div class="hstack" style="margin-top:20px;gap:7px"><i style="width:9px;height:9px;border-radius:50%;background:#fff;opacity:.5"></i><i style="width:9px;height:9px;border-radius:50%;background:#fff;opacity:.5"></i><i style="width:9px;height:9px;border-radius:50%;background:#fff"></i></div>
    </div>
    <div class="stack sm">
      <div class="panel-blue stack sm" style="padding:18px">
        <b style="font-size:17px">Último acceso</b>
        <div style="font-size:12.5px;line-height:1.9;color:#CFE4F5">
          <div class="hstack"><span>Último acceso:</span><span class="spacer"></span><b>22 de jul. de 2026 15:42</b></div>
          <div class="hstack"><span>IP de la terminal:</span><span class="spacer"></span><b>126.1.28.49</b></div>
          <div class="hstack"><span>Motivo de la última salida:</span><span class="spacer"></span><b>Sesión expirada</b></div>
          <div class="hstack"><span>Último cambio de contraseña:</span><span class="spacer"></span><b>22 feb. 2026</b></div>
        </div>
      </div>
      <div class="panel-navy" style="padding:16px"><b style="font-size:15px">Contáctenos</b>
        <div class="hstack" style="margin-top:12px;gap:10px">
          <div class="tb-btn" style="border:1.5px solid #4E7BA3;color:#fff">{ico('mail',18)}</div><div class="spacer"></div>
          <div class="tb-btn" style="border:1.5px solid #4E7BA3;color:#fff">{ico('share',18)}</div>
          <div class="tb-btn" style="border:1.5px solid #4E7BA3;color:#fff">{ico('bell',18)}</div>
        </div>
      </div>
    </div>
  </div>

  <div class="card" style="padding:0">
    <div style="display:grid;grid-template-columns:repeat(4,1fr)">
      <div style="padding:18px 22px;border-right:1px solid var(--line);display:flex;align-items:center;gap:14px">
        <div class="rowitem" style="border:0;padding:0;background:transparent"><div class="ic">{ico('money',22)}</div></div>
        <div><div class="hint" style="font-size:13px">Cuenta de ahorros</div><div style="font-size:24px;font-weight:800;color:var(--br-navy)"><small style="font-size:13px;color:var(--ink-3)">DOP</small> 380.51</div><div style="font-size:12px;color:var(--br-blue-600);font-weight:700">Balance disponible</div></div>
      </div>
      <div style="padding:18px 22px;border-right:1px solid var(--line);display:flex;align-items:center;gap:14px">
        <div class="rowitem" style="border:0;padding:0;background:transparent"><div class="ic">{ico('money',22)}</div></div>
        <div><div class="hint" style="font-size:13px">Cuenta de ahorros</div><div style="font-size:24px;font-weight:800;color:var(--br-navy)"><small style="font-size:13px;color:var(--ink-3)">DOP</small> 499.13</div><div style="font-size:12px;color:var(--br-blue-600);font-weight:700">Balance disponible</div></div>
      </div>
      <div style="padding:18px 22px;border-right:1px solid var(--line);display:flex;align-items:center;gap:14px">
        <div class="rowitem" style="border:0;padding:0;background:transparent"><div class="ic">{ico('refresh',22)}</div></div>
        <div><div class="hint" style="font-size:13px">Cuenta corriente</div><div style="font-size:24px;font-weight:800;color:var(--br-navy)"><small style="font-size:13px;color:var(--ink-3)">DOP</small> 2,383.33</div><div style="font-size:12px;color:var(--br-blue-600);font-weight:700">Balance disponible</div></div>
      </div>
      <div style="padding:18px 22px;display:flex;align-items:center;gap:12px">
        <div class="btn btn-outline sm">{ico('plus',16)} Agregar producto</div>
      </div>
    </div>
  </div>

  <div class="card" style="border:2px solid var(--br-orange);background:linear-gradient(100deg,#FFF8F1 0%,#FFFFFF 60%)">
    <div class="hstack" style="gap:20px">
      <div style="width:58px;height:58px;border-radius:16px;background:var(--br-orange);color:#fff;display:flex;align-items:center;justify-content:center;flex:none">{ico('transfer',30,2.2)}</div>
      <div>
        <div class="hstack" style="gap:10px"><b style="font-size:20px;color:var(--br-navy)">Pago Instantáneo RD</b><span class="badge orange">NUEVO</span></div>
        <div class="hint" style="font-size:13.5px;margin-top:3px">Envía y recibe dinero en segundos con un alias, 24/7, sin costo. Registra tu alias para empezar.</div>
      </div>
      <div class="spacer"></div>
      <div class="btn btn-outline">{ico('at',18)} Registrar mi alias</div>
      <div class="btn btn-primary">Enviar pago {ico('arrow',18)}</div>
    </div>
    <div class="grid-4" style="margin-top:20px">
      <div class="rowitem"><div class="ic">{ico('arrow',22)}</div><div class="tx"><b>Enviar pago</b><span>A un alias o cuenta</span></div></div>
      <div class="rowitem"><div class="ic">{ico('request',22)}</div><div class="tx"><b>Solicitar pago</b><span>Cobra con un enlace</span></div></div>
      <div class="rowitem"><div class="ic">{ico('qr',22)}</div><div class="tx"><b>Pagar con QR</b><span>Comercios y personas</span></div></div>
      <div class="rowitem"><div class="ic">{ico('at',22)}</div><div class="tx"><b>Mis alias</b><span>Administra tus llaves</span></div></div>
    </div>
  </div>

  <div class="grid-3">
    <div class="card"><div class="card-head"><div class="ico">{ico('doc',20)}</div><h3>Noticias TuBanco</h3></div>
      <div class="stack sm">
        <div><b style="font-size:14px;color:var(--br-navy)">Ya puedes pagar con QR</b><div class="hint">Escanea el código de cualquier comercio afiliado al sistema.</div></div>
        <div><b style="font-size:14px;color:var(--br-navy)">Suspender cheques</b><div class="hint">Envía tu solicitud en línea aquí.</div></div>
        <div><b style="font-size:14px;color:var(--br-navy)">Configurar notificaciones</b><div class="hint">Recibe alertas de cada pago instantáneo.</div></div>
      </div>
    </div>
    <div class="card"><div class="card-head"><div class="ico">{ico('heart',20)}</div><h3>Mis transacciones favoritas</h3><div class="right">Administrar</div></div>
      <div class="stack sm">
        <div class="rowitem" style="padding:11px"><div class="ic">{ico('at',20)}</div><div class="tx"><b>@mariaperez</b><span>Banco Popular</span></div><div class="rt"><b>DOP 1,500</b><span>Último envío</span></div></div>
        <div class="rowitem" style="padding:11px"><div class="ic">{ico('store',20)}</div><div class="tx"><b>Colmado La Esquina</b><span>QR · RNC 1-31-***-4</span></div><div class="rt"><b>DOP 420</b><span>Ayer</span></div></div>
      </div>
    </div>
    <div class="card"><div class="card-head"><div class="ico">{ico('refresh',20)}</div><h3>Tasas de cambio</h3></div>
      <table class="table"><tr><th>Compra</th><th style="text-align:right">Venta</th></tr>
      <tr><td><b>USD</b> Dólar</td><td class="num">56.40 / 59.90</td></tr>
      <tr><td><b>EUR</b> Euro</td><td class="num">66.00 / 71.50</td></tr></table>
    </div>
  </div>
</div>"""
    frame("B", "B-01", "Inicio · con módulo de Pago Instantáneo", "punto de entrada", body, nav="Inicio")

    # B-02 submenu Transferir
    sub = f"""<div style="position:absolute;left:112px;top:70px;width:330px;bottom:0;background:#0E90CE;padding:20px 0;color:#fff">
  <div style="padding:0 22px 14px;font-size:12px;letter-spacing:1.4px;font-weight:800;color:#BFE8FF">TRANSFERIR</div>
  {"".join(f'<div style="padding:14px 22px;display:flex;align-items:center;gap:12px;font-size:14.5px;font-weight:700{";background:#0A7FB8" if a else ""}">{ico(i,20)}<span>{t}</span>{"<span class=badge orange style=margin-left:auto>NUEVO</span>" if n else ""}</div>'
    for i,t,a,n in [("transfer","Entre mis cuentas",0,0),("bank","A otros Banreservas",0,0),("bank","A otros bancos (ACH)",0,0),
                    ("arrow","Pago Instantáneo · Enviar",1,1),("request","Pago Instantáneo · Solicitar",0,1),
                    ("qr","Pagar con QR",0,1),("at","Mis alias",0,1),("clock","Programadas",0,0),("star","Favoritas",0,0)])}
</div>"""
    body = f"""<div class="stack">{page_head("Transferir","Selecciona el tipo de transferencia que deseas realizar.")}
  <div style="height:520px"></div></div>"""
    frame("B", "B-02", "Menú Transferir desplegado", "navegación", body, scrim=sub)

    # B-03 Hub IPS
    body = f"""
<div class="stack">
  {page_head("Pago Instantáneo RD","Envía, cobra y paga en segundos con tu alias. Disponible 24 horas, todos los días.",["Inicio","Transferir","Pago Instantáneo"],
    f'<div class="btn btn-outline sm">{ico("shieldcheck",16)} Seguridad</div><div class="btn btn-outline sm">{ico("list",16)} Movimientos</div>')}
  <div class="grid-4">
    <div class="card" style="border-top:4px solid var(--br-orange)"><div class="ico" style="width:48px;height:48px;border-radius:14px;background:var(--br-orange-050);color:var(--br-orange);display:flex;align-items:center;justify-content:center">{ico('arrow',26)}</div>
      <b style="display:block;font-size:18px;color:var(--br-navy);margin:14px 0 6px">Enviar pago</b><div class="hint">A un alias, cuenta o contacto frecuente. Acreditación en segundos.</div>
      <div class="btn btn-primary sm block" style="margin-top:16px">Enviar</div></div>
    <div class="card" style="border-top:4px solid var(--br-blue)"><div class="ico" style="width:48px;height:48px;border-radius:14px;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center">{ico('request',26)}</div>
      <b style="display:block;font-size:18px;color:var(--br-navy);margin:14px 0 6px">Solicitar pago</b><div class="hint">Genera un cobro con enlace o QR y compártelo.</div>
      <div class="btn btn-outline sm block" style="margin-top:16px">Solicitar</div></div>
    <div class="card" style="border-top:4px solid var(--br-cyan)"><div class="ico" style="width:48px;height:48px;border-radius:14px;background:var(--br-cyan-050);color:var(--br-cyan-600);display:flex;align-items:center;justify-content:center">{ico('qr',26)}</div>
      <b style="display:block;font-size:18px;color:var(--br-navy);margin:14px 0 6px">Pagar con QR</b><div class="hint">Escanea el QR del comercio o de otra persona.</div>
      <div class="btn btn-outline sm block" style="margin-top:16px">Escanear</div></div>
    <div class="card" style="border-top:4px solid #0F8A4D"><div class="ico" style="width:48px;height:48px;border-radius:14px;background:var(--ok-bg);color:var(--ok);display:flex;align-items:center;justify-content:center">{ico('at',26)}</div>
      <b style="display:block;font-size:18px;color:var(--br-navy);margin:14px 0 6px">Mis alias</b><div class="hint">2 alias activos · administra a dónde llega tu dinero.</div>
      <div class="btn btn-outline sm block" style="margin-top:16px">Administrar</div></div>
  </div>
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Actividad reciente</h3><div class="right">Ver todos</div></div>
      <table class="table">
        <tr><th>Fecha</th><th>Detalle</th><th>Referencia</th><th style="text-align:right">Monto</th><th style="text-align:right">Estado</th></tr>
        <tr><td>Hoy 14:32</td><td><b>@mariaperez</b><div class="hint">Enviado · Banco Popular</div></td><td>PI-26-0098231</td><td class="num" style="color:var(--err)">- DOP 1,500.00</td><td style="text-align:right"><span class="badge ok">Completado</span></td></tr>
        <tr><td>Hoy 09:15</td><td><b>Colmado La Esquina</b><div class="hint">Pago con QR</div></td><td>PI-26-0097884</td><td class="num" style="color:var(--err)">- DOP 420.00</td><td style="text-align:right"><span class="badge ok">Completado</span></td></tr>
        <tr><td>Ayer 18:40</td><td><b>Juan Rodríguez</b><div class="hint">Recibido · 809-***-4471</div></td><td>PI-26-0097102</td><td class="num" style="color:var(--ok)">+ DOP 6,800.00</td><td style="text-align:right"><span class="badge ok">Completado</span></td></tr>
        <tr><td>Ayer 11:02</td><td><b>@carlosgm</b><div class="hint">Solicitud de pago enviada</div></td><td>SP-26-0004410</td><td class="num">DOP 2,300.00</td><td style="text-align:right"><span class="badge warn">Pendiente</span></td></tr>
      </table>
    </div>
    <div class="stack">
      <div class="card"><div class="card-head"><div class="ico">{ico('sliders',20)}</div><h3>Tus límites de hoy</h3></div>
        <div class="stack sm">
          <div class="limit-bar"><div class="lt"><span>Diario consumido</span><b>DOP 1,920 / 50,000</b></div><div class="progress"><i style="width:4%"></i></div></div>
          <div class="limit-bar"><div class="lt"><span>Por transacción</span><b>Máx. DOP 25,000</b></div><div class="progress"><i style="width:100%;background:#CBD5E1"></i></div></div>
          <div class="hint">Puedes ajustarlos en Seguridad. Los aumentos se activan 24 h después.</div>
        </div>
      </div>
      <div class="card"><div class="card-head"><div class="ico">{ico('at',20)}</div><h3>Mis alias</h3><div class="right">Administrar</div></div>
        <div class="stack sm">
          <div class="rowitem" style="padding:12px"><div class="ic">{ico('phone',20)}</div><div class="tx"><b>809-555-1234</b><span>Cuenta corriente ***3341</span></div><span class="badge ok" style="margin-left:auto">Activo</span></div>
          <div class="rowitem" style="padding:12px"><div class="ic">{ico('at',20)}</div><div class="tx"><b>@edwardf</b><span>Cuenta de ahorros ***8890</span></div><span class="badge ok" style="margin-left:auto">Activo</span></div>
          <div class="btn btn-outline sm block">{ico('plus',16)} Registrar otro alias</div>
        </div>
      </div>
      {alert('info','Banreservas nunca te pedirá tu clave ni el código OTP','Ni por teléfono, correo o WhatsApp. Si alguien te lo pide, es fraude.','shieldcheck')}
    </div>
  </div>
</div>"""
    frame("B", "B-03", "Hub Pago Instantáneo", "landing del producto", body)

# ============================================================== C. MIS ALIAS
ALIAS_STEPS = ["Tipo de alias","Verificación","Cuenta","Confirmación"]

def g_alias():
    # C-01 Educativo
    body = f"""
<div class="stack">
  {page_head("Registra tu alias","Un alias es un dato fácil de recordar que reemplaza tu número de cuenta para recibir dinero.",["Pago Instantáneo","Mis alias","Registro"])}
  <div class="grid-2" style="grid-template-columns:1fr 460px">
    <div class="stack">
      <div class="card stack">
        <div class="grid-2">
          <div class="rowitem" style="align-items:flex-start"><div class="ic">{ico('phone',22)}</div><div class="tx"><b>Tu celular</b><span>809-555-1234</span></div></div>
          <div class="rowitem" style="align-items:flex-start"><div class="ic">{ico('mail',22)}</div><div class="tx"><b>Tu correo</b><span>nombre@correo.com</span></div></div>
          <div class="rowitem" style="align-items:flex-start"><div class="ic">{ico('id',22)}</div><div class="tx"><b>Tu cédula</b><span>001-1234567-8</span></div></div>
          <div class="rowitem" style="align-items:flex-start"><div class="ic">{ico('at',22)}</div><div class="tx"><b>Un alias propio</b><span>@edwardf</span></div></div>
        </div>
        <div class="dashed" style="margin:4px 0"></div>
        <div class="grid-3">
          <div class="stack sm"><div style="color:var(--br-orange)">{ico('clock',26)}</div><b style="font-size:15px;color:var(--br-navy)">En segundos</b><div class="hint">El dinero se acredita al instante, 24/7, incluso fines de semana y feriados.</div></div>
          <div class="stack sm"><div style="color:var(--br-orange)">{ico('money',26)}</div><b style="font-size:15px;color:var(--br-navy)">Sin costo para ti</b><div class="hint">Enviar y recibir pagos instantáneos entre personas no tiene comisión.</div></div>
          <div class="stack sm"><div style="color:var(--br-orange)">{ico('bank',26)}</div><b style="font-size:15px;color:var(--br-navy)">Con cualquier banco</b><div class="hint">Interoperable con todas las entidades del sistema financiero dominicano.</div></div>
        </div>
      </div>
      {alert('info','Tu alias no revela tus datos','Quien te paga solo ve tu nombre parcialmente enmascarado y tu entidad. Nunca ve tu número de cuenta ni tu saldo.','shieldcheck')}
      <div class="hstack"><div class="btn btn-ghost">Ahora no</div><div class="spacer"></div><div class="btn btn-primary lg">Comenzar registro {ico('arrow',18)}</div></div>
    </div>
    <div class="card stack sm" style="background:var(--br-navy);color:#fff">
      <div class="hstack">{ico('info',20)}<b style="font-size:16px">Reglas del sistema</b></div>
      <div style="font-size:13.5px;line-height:1.85;color:#C9DCEC">
        <div class="hstack" style="align-items:flex-start;gap:10px">{ico('check',16,3)}<span>Cada alias es único en todo el país y apunta a <b>una sola cuenta</b>.</span></div>
        <div class="hstack" style="align-items:flex-start;gap:10px">{ico('check',16,3)}<span>Puedes registrar hasta <b>5 alias</b> (uno por tipo) en Banreservas.</span></div>
        <div class="hstack" style="align-items:flex-start;gap:10px">{ico('check',16,3)}<span>El celular, correo y cédula deben estar <b>verificados y a tu nombre</b>.</span></div>
        <div class="hstack" style="align-items:flex-start;gap:10px">{ico('check',16,3)}<span>Si tu alias ya está en otro banco, puedes <b>portarlo</b> a Banreservas.</span></div>
        <div class="hstack" style="align-items:flex-start;gap:10px">{ico('check',16,3)}<span>Puedes cambiar la cuenta asociada o eliminar tu alias cuando quieras.</span></div>
      </div>
    </div>
  </div>
</div>"""
    frame("C", "C-01", "Mis alias · qué es y beneficios", "onboarding 1/8", body)

    # C-02 T&C
    body = f"""
<div class="stack">
  {page_head("Términos y condiciones","Lee y acepta antes de registrar tu alias.",["Pago Instantáneo","Mis alias","Registro"])}
  {stepper(ALIAS_STEPS,0)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack sm">
      <b style="font-size:16px;color:var(--br-navy)">Contrato de adhesión al servicio de Pago Instantáneo RD</b>
      <div style="height:330px;overflow:hidden;border:1px solid var(--line);border-radius:12px;padding:18px;font-size:13px;line-height:1.75;color:var(--ink-2)">
        <b>1. Objeto.</b> Banreservas pone a disposición del Cliente el servicio de pagos inmediatos interoperable,
        que permite enviar y recibir fondos en tiempo real mediante identificadores simplificados (alias).<br><br>
        <b>2. Registro y titularidad del alias.</b> El Cliente declara que los datos utilizados como alias (número celular,
        correo electrónico, documento de identidad o alias personalizado) son de su titularidad. El alias es único a nivel
        nacional y se registra en el Directorio Centralizado de Alias administrado por la entidad rectora del sistema.<br><br>
        <b>3. Irrevocabilidad.</b> Las transferencias son <b>inmediatas e irrevocables</b>. Una vez autorizadas no pueden
        anularse unilateralmente; el Cliente podrá solicitar una devolución al beneficiario a través del canal de reclamaciones.<br><br>
        <b>4. Responsabilidad del Cliente.</b> Es responsabilidad del Cliente verificar el nombre del beneficiario
        mostrado antes de autorizar. Banreservas no responde por pagos correctamente ejecutados hacia un alias digitado por el Cliente.<br><br>
        <b>5. Seguridad.</b> El Cliente se obliga a custodiar sus credenciales, claves de un solo uso y dispositivos.
        Banreservas nunca solicitará contraseñas, tokens ni códigos OTP por ningún medio.<br><br>
        <b>6. Tratamiento de datos.</b> El Cliente autoriza el tratamiento y la consulta de sus datos en el directorio de alias
        para la prestación del servicio, conforme a la Ley 172-13 de Protección de Datos Personales.
      </div>
      <div class="stack sm" style="margin-top:8px">
        <div class="hstack" style="align-items:flex-start"><div class="check on">{ico('check',14,3)}</div><span style="font-size:13.5px;color:var(--ink-2)">He leído y acepto los <b>términos y condiciones</b> del servicio de Pago Instantáneo RD.</span></div>
        <div class="hstack" style="align-items:flex-start"><div class="check on">{ico('check',14,3)}</div><span style="font-size:13.5px;color:var(--ink-2)">Autorizo el registro de mis datos en el <b>Directorio Centralizado de Alias</b> y su consulta por otras entidades para recibir pagos.</span></div>
        <div class="hstack" style="align-items:flex-start"><div class="check"></div><span style="font-size:13.5px;color:var(--ink-2)">Deseo recibir notificaciones y promociones sobre el servicio <span class="hint" style="display:inline">(opcional)</span>.</span></div>
      </div>
      <div class="hstack" style="margin-top:10px"><div class="btn btn-outline">{ico('download',18)} Descargar contrato</div><div class="spacer"></div><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary">Aceptar y continuar</div></div>
    </div>
    <div class="stack">
      {alert('warn','Los pagos son irrevocables','Verifica siempre el nombre del beneficiario antes de autorizar. No podrás cancelar un pago ya enviado.')}
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('doc',20)}</div><h3>Resumen en lenguaje claro</h3></div>
        <div class="kv"><div class="k">Costo</div><div class="v">DOP 0.00 para personas</div></div>
        <div class="kv"><div class="k">Horario</div><div class="v">24/7/365</div></div>
        <div class="kv"><div class="k">Tiempo de acreditación</div><div class="v">Menos de 20 segundos</div></div>
        <div class="kv"><div class="k">Anulación</div><div class="v">No aplica · solo devolución voluntaria</div></div>
        <div class="kv"><div class="k">Reclamaciones</div><div class="v">Hasta 90 días · vía Movimientos</div></div>
      </div>
    </div>
  </div>
</div>"""
    frame("C", "C-02", "Mis alias · términos y condiciones", "onboarding 2/8", body)

    # C-03 Tipo de alias
    def atype(icon, title, sub, badge="", sel=False, dis=False):
        b = f'<span class="badge {badge[1]}" style="margin-left:auto">{badge[0]}</span>' if badge else '<span style="margin-left:auto"></span>'
        op = "opacity:.55" if dis else ""
        return (f'<div class="rowitem {"sel" if sel else ""}" style="{op}"><div class="radio {"on" if sel else ""}"></div>'
                f'<div class="ic">{ico(icon,22)}</div><div class="tx"><b>{title}</b><span>{sub}</span></div>{b}</div>')
    body = f"""
<div class="stack">
  {page_head("¿Qué alias quieres registrar?","Elige el dato con el que quieres que te paguen. Puedes registrar más de uno.",["Pago Instantáneo","Mis alias","Registro"])}
  {stepper(ALIAS_STEPS,0)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack sm">
      {atype('phone','Número de celular','809-555-1234 · verificado en tu perfil',("RECOMENDADO","orange"),sel=True)}
      {atype('mail','Correo electrónico','edw****@correo.com · verificado')}
      {atype('id','Cédula de identidad','001-*******-8 · titular verificado')}
      {atype('at','Alias personalizado','Créalo tú: @edwardf, @edw.pagos')}
      {atype('store','RNC / comercio','Solo para cuentas de negocio',("No disponible","neutral"),dis=True)}
      <div class="hstack" style="margin-top:12px"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('info',20)}</div><h3>¿Cuál me conviene?</h3></div>
        <div class="hint" style="line-height:1.7">
          <b style="color:var(--br-navy)">Celular:</b> el más usado; quien tenga tu número puede pagarte sin pedirte nada más.<br><br>
          <b style="color:var(--br-navy)">Correo:</b> útil para cobros formales y facturas.<br><br>
          <b style="color:var(--br-navy)">Cédula:</b> práctico entre familiares, pero expone tu documento a quien te paga.<br><br>
          <b style="color:var(--br-navy)">Alias propio:</b> el más privado; no revela ningún dato personal tuyo.
        </div>
      </div>
      {alert('info','Cada alias apunta a una sola cuenta','Puedes tener varios alias apuntando a cuentas distintas, por ejemplo tu celular a la corriente y @edwardf a la de ahorros.')}
    </div>
  </div>
</div>"""
    frame("C", "C-03", "Mis alias · elegir tipo", "onboarding 3/8", body)

    # C-04 Datos + envio OTP
    body = f"""
<div class="stack">
  {page_head("Verifica tu número de celular","Enviaremos un código de un solo uso para confirmar que el número es tuyo.",["Pago Instantáneo","Mis alias","Registro"])}
  {stepper(ALIAS_STEPS,1)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      {field("Número de celular registrado en tu perfil", inp("809-555-1234","",'ro',pre="+1",icon="phone"), "Para usar otro número debes actualizarlo primero en Administrar → Datos personales.")}
      <div class="stack sm">
        <div class="label">¿Dónde quieres recibir el código?</div>
        <div class="rowitem sel"><div class="radio on"></div><div class="ic">{ico('phone',22)}</div><div class="tx"><b>SMS al 809-***-1234</b><span>Llega en menos de 30 segundos</span></div></div>
        <div class="rowitem"><div class="radio"></div><div class="ic">{ico('bell',22)}</div><div class="tx"><b>Notificación en la App TuBanco</b><span>Aprobación con biometría · más seguro</span></div></div>
      </div>
      {alert('warn','Nunca compartas este código','Banreservas jamás te lo pedirá por llamada, correo o WhatsApp.','shieldcheck')}
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Enviar código {ico('arrow',18)}</div></div>
    </div>
    <div class="card stack sm" style="align-self:flex-start"><div class="card-head"><div class="ico">{ico('at',20)}</div><h3>Alias a registrar</h3></div>
      <div class="rowitem"><div class="ic">{ico('phone',22)}</div><div class="tx"><b>809-555-1234</b><span>Alias tipo celular</span></div></div>
      <div class="kv"><div class="k">Titular</div><div class="v">Edward A. Fiallo S.</div></div>
      <div class="kv"><div class="k">Entidad</div><div class="v">Banreservas</div></div>
      <div class="kv"><div class="k">Estado</div><div class="v"><span class="badge warn">Pendiente de verificación</span></div></div>
    </div>
  </div>
</div>"""
    frame("C", "C-04", "Mis alias · datos del alias", "onboarding 4/8", body)

    # C-05 OTP
    body = f"""
<div class="stack">
  {page_head("Ingresa el código de verificación","Enviamos un código de 6 dígitos al 809-***-1234.",["Pago Instantáneo","Mis alias","Registro"])}
  {stepper(ALIAS_STEPS,1)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="otp"><div class="b on">7</div><div class="b on">3</div><div class="b on">9</div><div class="b cursor"></div><div class="b"></div><div class="b"></div></div>
      <div class="hstack" style="gap:16px">
        <span class="badge info">{ico('clock',13,2.4)} Expira en 01:47</span>
        <span class="hint">¿No lo recibiste? <b style="color:var(--br-blue-600)">Reenviar código</b> (disponible en 0:32)</span>
      </div>
      <div class="hint">Intentos restantes: <b>3 de 3</b>. Tras 3 intentos fallidos el registro se bloquea por 15 minutos.</div>
      <div class="dashed" style="margin:6px 0"></div>
      {alert('info','Sello anti-phishing','Tu sello de seguridad es <b>"Palmera azul"</b>. Si el mensaje que recibiste no lo incluye, no lo uses.','shieldcheck')}
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Verificar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('phone',20)}</div><h3>Vista del SMS</h3></div>
        <div style="background:#F1F5F9;border-radius:14px;padding:16px;font-size:13.5px;line-height:1.6;color:var(--ink-2)">
          <b style="color:var(--br-navy)">BANRESERVAS</b><br>Palmera azul · Tu código para registrar el alias 809-555-1234 es <b>739 428</b>.
          Vence en 2 min. <b>Nunca lo compartas</b>; el banco no te lo pedirá.
        </div>
      </div>
      {alert('err','Si no solicitaste este código','Alguien podría estar intentando registrar tu número. Repórtalo al 809-960-2000.','alert')}
    </div>
  </div>
</div>"""
    frame("C", "C-05", "Mis alias · verificación OTP", "onboarding 5/8", body)

    # C-06 Cuenta
    body = f"""
<div class="stack">
  {page_head("¿A qué cuenta llegará el dinero?","Selecciona la cuenta que se asociará a este alias. Podrás cambiarla después.",["Pago Instantáneo","Mis alias","Registro"])}
  {stepper(ALIAS_STEPS,2)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack sm">
      {acct_row("Cuenta corriente","No. ****3341 · DOP","DOP 2,383.33",sel=True,icon="refresh")}
      {acct_row("Cuenta de ahorros","No. ****8890 · DOP","DOP 499.13")}
      {acct_row("Cuenta de ahorros","No. ****1207 · DOP","DOP 380.51")}
      <div class="rowitem" style="opacity:.55"><div class="radio"></div><div class="ic">{ico('money',22)}</div><div class="tx"><b>Cuenta de ahorros USD</b><span>No. ****5512 · USD</span></div><span class="badge neutral" style="margin-left:auto">Solo cuentas en DOP</span></div>
      <div class="hstack" style="margin-top:12px"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      {alert('ok','Alias verificado','El número 809-555-1234 quedó confirmado como tuyo.','check')}
      {alert('info','El pagador nunca ve tu cuenta','Solo verá tu nombre enmascarado (E***** F*****) y que tu entidad es Banreservas.','shieldcheck')}
    </div>
  </div>
</div>"""
    frame("C", "C-06", "Mis alias · cuenta asociada", "onboarding 6/8", body)

    # C-07 Confirmacion
    body = f"""
<div class="stack">
  {page_head("Confirma el registro de tu alias","Revisa los datos antes de finalizar.",["Pago Instantáneo","Mis alias","Registro"])}
  {stepper(ALIAS_STEPS,3)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="rowitem" style="background:#F7FBFE;border-color:#BFDDF2"><div class="ic">{ico('phone',22)}</div><div class="tx"><b style="font-size:19px">809-555-1234</b><span>Alias tipo celular · verificado</span></div><span class="badge ok" style="margin-left:auto">{ico('check',13,3)} Verificado</span></div>
      {kv([("Titular","EDWARD ALEJANDRO FIALLO S."),("Documento","001-*******-8"),
           ("Entidad","Banreservas"),("Cuenta asociada","Cuenta corriente ****3341<small>Moneda DOP</small>"),
           ("Visible para el pagador","Nombre enmascarado + entidad"),("Fecha de registro","02 de sep. de 2026")])}
      {alert('info','Confirmación con tu App TuBanco','Recibirás una notificación para aprobar el registro con tu huella o Face ID.','shieldcheck')}
      <div class="hstack"><div class="btn btn-outline">{ico('edit',18)} Modificar</div><div class="spacer"></div><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary lg">Registrar alias</div></div>
    </div>
    <div class="card stack sm" style="align-self:flex-start"><div class="card-head"><div class="ico">{ico('eye',20)}</div><h3>Así te verán</h3></div>
      <div class="card flat stack sm" style="background:#F8FAFC">
        <div class="hint">Vista del pagador al buscar tu alias</div>
        <div class="rowitem" style="background:#fff"><div class="ic">{ico('user',22)}</div><div class="tx"><b>E***** A***** F***** S.</b><span>Banreservas · Cuenta corriente</span></div><span class="badge ok" style="margin-left:auto">Alias válido</span></div>
      </div>
      <div class="hint">El enmascaramiento del nombre es un estándar antifraude: permite confirmar a quién se paga sin exponer la identidad completa.</div>
    </div>
  </div>
</div>"""
    frame("C", "C-07", "Mis alias · confirmación", "onboarding 7/8", body)

    # C-08 Exito
    body = f"""
<div class="stack">
  <div style="display:flex;justify-content:center;padding-top:22px">
    <div class="card" style="width:760px;text-align:center;padding:40px">
      <div style="width:88px;height:88px;border-radius:50%;background:var(--ok-bg);color:var(--ok);display:flex;align-items:center;justify-content:center;margin:0 auto 18px">{ico('check',44,3)}</div>
      <h1 class="page" style="font-size:28px">¡Tu alias está activo!</h1>
      <p class="page-sub" style="font-size:15px">Ya puedes recibir dinero de cualquier banco del país con solo compartir tu número.</p>
      <div class="rowitem" style="margin:24px 0;justify-content:center;background:#F7FBFE;border-color:#BFDDF2">
        <div class="ic">{ico('phone',22)}</div><div class="tx" style="text-align:left"><b style="font-size:20px">809-555-1234</b><span>Cuenta corriente ****3341</span></div>
        <span class="badge ok" style="margin-left:24px">Activo</span>
      </div>
      <div class="grid-3" style="text-align:left">
        <div class="rowitem"><div class="ic">{ico('qr',20)}</div><div class="tx"><b>Ver mi QR</b><span>Para cobrar</span></div></div>
        <div class="rowitem"><div class="ic">{ico('share',20)}</div><div class="tx"><b>Compartir alias</b><span>WhatsApp o correo</span></div></div>
        <div class="rowitem"><div class="ic">{ico('plus',20)}</div><div class="tx"><b>Registrar otro</b><span>Correo, cédula, @alias</span></div></div>
      </div>
      <div class="hstack" style="margin-top:26px;justify-content:center"><div class="btn btn-outline">Ir a mis alias</div><div class="btn btn-primary">Enviar mi primer pago {ico('arrow',18)}</div></div>
      <div class="hint" style="margin-top:18px">Referencia de registro: <b>ALS-2026-0044182</b> · Te enviamos la confirmación a edw****@correo.com</div>
    </div>
  </div>
</div>"""
    frame("C", "C-08", "Mis alias · registro exitoso", "onboarding 8/8", body)

    # C-09 Lista
    def alias_row(icon, name, acct, badge, extra=""):
        return f"""<div class="rowitem"><div class="ic">{ico(icon,22)}</div>
          <div class="tx"><b>{name}</b><span>{acct}</span></div>
          <div style="margin-left:auto" class="hstack">{extra}{badge}<div class="btn btn-outline sm">{ico('edit',15)} Editar</div><div style="color:var(--ink-3)">{ico('chevr',18)}</div></div></div>"""
    body = f"""
<div class="stack">
  {page_head("Mis alias","Administra los alias con los que recibes dinero.",["Pago Instantáneo","Mis alias"],
    f'<div class="btn btn-outline sm">{ico("qr",16)} Mi QR</div><div class="btn btn-primary sm">{ico("plus",16)} Registrar alias</div>')}
  <div class="grid-2" style="grid-template-columns:1fr 400px">
    <div class="card stack sm">
      <div class="card-head"><div class="ico">{ico('at',20)}</div><h3>4 alias registrados</h3><div class="right">Máximo 5</div></div>
      {alias_row('phone','809-555-1234','Cuenta corriente ****3341 · registrado 02 sep. 2026','<span class="badge ok">Activo</span>')}
      {alias_row('at','@edwardf','Cuenta de ahorros ****8890 · registrado 02 sep. 2026','<span class="badge ok">Activo</span>')}
      {alias_row('mail','edw****@correo.com','Pendiente de confirmar el correo','<span class="badge warn">En verificación</span>')}
      {alias_row('id','001-*******-8','Reclamo de portabilidad en curso · vence 07 sep.','<span class="badge info">Portabilidad</span>')}
      <div class="rowitem" style="border-style:dashed;justify-content:center;color:var(--br-blue-600);font-weight:800;font-size:14px">{ico('plus',20)} Registrar un nuevo alias</div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('shieldcheck',20)}</div><h3>Recomendaciones</h3></div>
        <div class="hstack" style="align-items:flex-start;gap:10px"><div style="color:var(--ok)">{ico('check',18,3)}</div><span class="hint">Usa <b>@alias</b> con desconocidos: no revela tu celular ni tu cédula.</span></div>
        <div class="hstack" style="align-items:flex-start;gap:10px"><div style="color:var(--ok)">{ico('check',18,3)}</div><span class="hint">Revisa periódicamente a qué cuenta apunta cada alias.</span></div>
        <div class="hstack" style="align-items:flex-start;gap:10px"><div style="color:var(--ok)">{ico('check',18,3)}</div><span class="hint">Si cambias de número, elimina el alias anterior de inmediato.</span></div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Historial de cambios</h3></div>
        <div class="kv"><div class="k">02 sep. 15:10</div><div class="v">Alias @edwardf creado</div></div>
        <div class="kv"><div class="k">02 sep. 14:58</div><div class="v">809-555-1234 → cuenta ****3341</div></div>
        <div class="kv"><div class="k">28 ago. 09:31</div><div class="v">Alias 849-***-0090 eliminado</div></div>
      </div>
    </div>
  </div>
</div>"""
    frame("C", "C-09", "Mis alias · listado", "gestión", body)

    # C-10 Detalle / editar
    modal = f"""<div class="scrim"><div class="modal">
  <div class="modal-head"><div class="ico" style="width:34px;height:34px;border-radius:10px;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center">{ico('phone',20)}</div><h3>809-555-1234</h3><div class="x">{ico('x',20)}</div></div>
  <div class="modal-body stack">
    {kv([("Tipo","Alias de celular"),("Estado",'<span class="badge ok">Activo</span>'),("Registrado","02 de sep. de 2026 · 14:58"),("Pagos recibidos","18 · DOP 46,200.00 en 30 días")])}
    <div class="field"><div class="label">Cuenta asociada</div>
      <div class="rowitem sel"><div class="ic">{ico('refresh',22)}</div><div class="tx"><b>Cuenta corriente ****3341</b><span>Balance DOP 2,383.33</span></div><div class="btn btn-outline sm" style="margin-left:auto">Cambiar</div></div>
    </div>
    {alert('warn','Cambiar la cuenta requiere verificación','Te pediremos una aprobación en la App TuBanco. El cambio aplica de inmediato para los pagos nuevos.')}
    <div class="hstack" style="gap:10px"><div class="btn btn-danger sm">{ico('trash',15)} Eliminar alias</div><div class="btn btn-outline sm">{ico('lock',15)} Desactivar temporalmente</div></div>
  </div>
  <div class="modal-foot"><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary">Guardar cambios</div></div>
</div></div>"""
    body = f"""<div class="stack">{page_head("Mis alias","Administra los alias con los que recibes dinero.",["Pago Instantáneo","Mis alias"])}<div style="height:520px"></div></div>"""
    frame("C", "C-10", "Mis alias · detalle y edición", "modal", body, scrim=modal)

    # C-11 Portabilidad
    body = f"""
<div class="stack">
  {page_head("Este alias ya está registrado en otra entidad","Puedes reclamarlo para recibir tus pagos en Banreservas.",["Pago Instantáneo","Mis alias","Portabilidad"])}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      {alert('warn','001-1234567-8 está asociado a otra entidad','El Directorio Centralizado de Alias indica que este documento ya recibe pagos en <b>Banco X</b>. Como titular verificado puedes solicitar su portabilidad.')}
      <div class="stack sm">
        <div class="label">¿Cómo funciona el reclamo?</div>
        <div class="rowitem"><div class="ic" style="background:var(--br-orange-050);color:var(--br-orange)">1</div><div class="tx"><b>Solicitas la portabilidad</b><span>Validamos tu identidad con la App TuBanco</span></div></div>
        <div class="rowitem"><div class="ic" style="background:var(--br-orange-050);color:var(--br-orange)">2</div><div class="tx"><b>La otra entidad te notifica</b><span>Tienes 5 días calendario para confirmar o rechazar allí</span></div></div>
        <div class="rowitem"><div class="ic" style="background:var(--br-orange-050);color:var(--br-orange)">3</div><div class="tx"><b>El alias se traslada</b><span>Si no respondes, se traslada automáticamente a Banreservas</span></div></div>
      </div>
      <div class="hstack"><div class="btn btn-outline">Usar otro alias</div><div class="spacer"></div><div class="btn btn-primary">Solicitar portabilidad {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Reclamo en curso</h3></div>
        <div class="rowitem"><div class="ic">{ico('id',22)}</div><div class="tx"><b>001-*******-8</b><span>Solicitado el 02 sep. 2026</span></div><span class="badge info" style="margin-left:auto">Día 1 de 5</span></div>
        <div class="progress"><i class="warn" style="width:20%"></i></div>
        <div class="hint">Vence el 07 de sep. de 2026 a las 14:58. Mientras tanto, los pagos a este alias siguen llegando a la otra entidad.</div>
        <div class="btn btn-danger sm block">Cancelar reclamo</div>
      </div>
      {alert('info','¿Recibiste un reclamo sobre tu alias?','Si otra entidad reclama un alias tuyo, te avisaremos por push y correo para que lo confirmes o rechaces.','bell')}
    </div>
  </div>
</div>"""
    frame("C", "C-11", "Mis alias · portabilidad / reclamo", "caso alterno", body)

    # C-12 Alias personalizado
    body = f"""
<div class="stack">
  {page_head("Crea tu alias personalizado","Es la forma más privada de recibir pagos: no revela tu celular, correo ni cédula.",["Pago Instantáneo","Mis alias","Registro"])}
  {stepper(ALIAS_STEPS,0)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      {field("Tu alias", inp("edwardf","", "ok", pre="@", suf="Disponible"), "Disponible · quedará como <b>@edwardf</b>","hint ok")}
      <div class="stack sm">
        <div class="label">Reglas</div>
        <div class="hstack"><div style="color:var(--ok)">{ico('check',16,3)}</div><span class="hint">Entre 4 y 20 caracteres</span></div>
        <div class="hstack"><div style="color:var(--ok)">{ico('check',16,3)}</div><span class="hint">Solo letras, números, punto y guion bajo</span></div>
        <div class="hstack"><div style="color:var(--ok)">{ico('check',16,3)}</div><span class="hint">Sin espacios ni caracteres especiales</span></div>
        <div class="hstack"><div style="color:var(--err)">{ico('x',16,3)}</div><span class="hint">No puede parecerse a nombres de bancos o instituciones</span></div>
      </div>
      <div class="dashed" style="margin:2px 0"></div>
      <div class="stack sm"><div class="label">Ejemplos no disponibles</div>
        <div class="hstack" style="flex-wrap:wrap;gap:8px">
          <span class="badge err">@banreservas</span><span class="badge err">@soporte.banco</span><span class="badge err">@edward</span><span class="badge neutral">@edw</span>
        </div>
        <div class="hint">Un alias ya tomado no puede reclamarse: los alias personalizados no son portables entre personas.</div>
      </div>
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('eye',20)}</div><h3>Vista previa</h3></div>
        <div class="rowitem" style="background:#F7FBFE;border-color:#BFDDF2"><div class="ic">{ico('at',22)}</div><div class="tx"><b>@edwardf</b><span>E***** F***** · Banreservas</span></div></div>
        <div class="hint">Así aparecerá cuando alguien te busque para pagarte.</div>
      </div>
      {alert('err','Alias no disponible','Ejemplo de estado de error: “@edward ya está en uso. Prueba con @edward.rd o @edwardf”.','alert')}
    </div>
  </div>
</div>"""
    frame("C", "C-12", "Mis alias · alias personalizado @", "variante", body)

# =========================================================== D. ENVIAR PAGO
SEND_STEPS = ["Destino","Monto y concepto","Revisión","Autenticación"]

def g_enviar():
    tabs = lambda a: f"""<div class="tabs">
      <div class="tab {'active' if a==0 else ''}">{ico('at',18)} Alias</div>
      <div class="tab {'active' if a==1 else ''}">{ico('bank',18)} Número de cuenta</div>
      <div class="tab {'active' if a==2 else ''}">{ico('star',18)} Frecuentes</div>
      <div class="tab {'active' if a==3 else ''}">{ico('qr',18)} QR</div></div>"""

    # D-01 destino
    body = f"""
<div class="stack">
  {page_head("Enviar pago instantáneo","El dinero llega en segundos a cualquier banco del país.",["Pago Instantáneo","Enviar pago"])}
  {stepper(SEND_STEPS,0)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      {tabs(0)}
      {field("Alias del beneficiario", inp("Celular, correo, cédula o @alias", True, icon="search"), "Escríbelo tal como te lo compartieron. No distingue mayúsculas.")}
      <div class="stack sm">
        <div class="label">Contactos frecuentes</div>
        <div class="grid-4">
          {"".join(f'<div class="card flat" style="display:flex;flex-direction:column;align-items:center;gap:8px;padding:16px 10px;text-align:center"><div style="width:44px;height:44px;border-radius:50%;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center;font-weight:800">{ini}</div><b style="font-size:13px;color:var(--br-navy)">{n}</b><span class="hint" style="font-size:11.5px">{a}</span></div>' for ini,n,a in [("MP","María P.","@mariaperez"),("JR","Juan R.","809-***-4471"),("CG","Carlos G.","@carlosgm"),("LS","Luisa S.","luisa***@correo.com")])}
        </div>
      </div>
      <div class="hstack"><div class="btn btn-ghost">Cancelar</div><div class="spacer"></div><div class="btn disabled">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('money',20)}</div><h3>Cuenta de origen</h3></div>
        {acct_row("Cuenta corriente","No. ****3341","DOP 2,383.33",sel=True,icon="refresh")}
        <div class="hint">Podrás cambiarla en el siguiente paso.</div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('sliders',20)}</div><h3>Disponible hoy</h3></div>
        <div class="limit-bar"><div class="lt"><span>Límite diario</span><b>DOP 48,080 de 50,000</b></div><div class="progress"><i style="width:4%"></i></div></div>
        <div class="hint">Máximo por transacción: DOP 25,000</div>
      </div>
      {alert('info','Pagos irrevocables','Una vez autorizado, el pago no se puede cancelar. Verifica siempre el nombre del beneficiario.')}
    </div>
  </div>
</div>"""
    frame("D", "D-01", "Enviar · paso 1 destino", "1/4", body)

    # D-02 resolviendo
    body = f"""
<div class="stack">
  {page_head("Enviar pago instantáneo","Buscando el alias en el directorio nacional...",["Pago Instantáneo","Enviar pago"])}
  {stepper(SEND_STEPS,0)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      {tabs(0)}
      {field("Alias del beneficiario", inp("@mariaperez","", "focus", icon="at", suf="Buscando..."))}
      <div class="card flat stack sm" style="align-items:center;padding:34px">
        <div style="width:52px;height:52px;border-radius:50%;border:4px solid #E4EAF1;border-top-color:var(--br-orange)"></div>
        <b style="font-size:15px;color:var(--br-navy)">Consultando el Directorio Centralizado de Alias</b>
        <span class="hint">Verificando titularidad y entidad receptora · toma menos de 2 segundos</span>
      </div>
      <div class="hstack"><div class="btn btn-ghost">Cancelar</div><div class="spacer"></div><div class="btn disabled">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      {alert('info','¿Por qué consultamos el directorio?','Para confirmar que el alias existe, a qué entidad pertenece y mostrarte el nombre del titular antes de que pagues.','shieldcheck')}
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('lock',20)}</div><h3>Conexión segura</h3></div>
        <div class="kv"><div class="k">Canal</div><div class="v">TLS 1.3 · certificado EV</div></div>
        <div class="kv"><div class="k">Sesión</div><div class="v">Expira por inactividad en 4:32</div></div>
        <div class="kv"><div class="k">Dispositivo</div><div class="v">Reconocido {ico('check',14,3)}</div></div>
      </div>
    </div>
  </div>
</div>"""
    frame("D", "D-02", "Enviar · resolviendo alias", "estado de carga", body)

    # D-03 alias encontrado
    body = f"""
<div class="stack">
  {page_head("Confirma a quién le vas a pagar","Compara el nombre con la persona que te compartió el alias.",["Pago Instantáneo","Enviar pago"])}
  {stepper(SEND_STEPS,0)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      {tabs(0)}
      {field("Alias del beneficiario", inp("@mariaperez","", "ok", icon="at", suf="Encontrado"))}
      <div class="card flat stack sm" style="border:2px solid var(--ok);background:#F6FCF8">
        <div class="hstack" style="gap:16px">
          <div style="width:56px;height:56px;border-radius:50%;background:#fff;border:2px solid var(--ok);color:var(--ok);display:flex;align-items:center;justify-content:center">{ico('user',28)}</div>
          <div><div style="font-size:22px;font-weight:800;color:var(--br-navy)">M**** F***** P***** G*****</div>
            <div class="hint" style="font-size:13.5px">Banco Popular Dominicano · Cuenta de ahorros · Persona física</div></div>
          <span class="badge ok" style="margin-left:auto">{ico('check',13,3)} Alias verificado</span>
        </div>
        <div class="dashed" style="margin:6px 0"></div>
        <div class="hstack" style="align-items:flex-start;gap:10px"><div class="check on">{ico('check',14,3)}</div>
          <span style="font-size:13.5px;color:var(--ink-2)"><b>Confirmo que esta es la persona a la que quiero pagar.</b> Entiendo que el pago es inmediato e irrevocable.</span></div>
      </div>
      {alert('warn','Primera vez que le pagas a este alias','Como medida de seguridad, el monto máximo hacia un beneficiario nuevo es DOP 10,000 durante las primeras 24 horas.')}
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('shieldcheck',20)}</div><h3>Verificación de nombre</h3></div>
        <div class="hint" style="line-height:1.7">Mostramos el nombre parcialmente enmascarado que la entidad receptora reporta para ese alias.
        Si <b>no coincide</b> con la persona que esperas, detente: es el patrón más común de estafa por suplantación.</div>
        <div class="btn btn-outline sm block">{ico('alert',16)} Reportar este alias</div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('star',20)}</div><h3>Guardar contacto</h3></div>
        <div class="hstack"><div class="switch on"><i></i></div><span class="hint">Agregar a mis frecuentes al finalizar</span></div>
      </div>
    </div>
  </div>
</div>"""
    frame("D", "D-03", "Enviar · confirmación del beneficiario", "control antifraude", body)

    # D-04 alias no encontrado / riesgo
    body = f"""
<div class="stack">
  {page_head("Enviar pago instantáneo","",["Pago Instantáneo","Enviar pago"])}
  {stepper(SEND_STEPS,0)}
  <div class="grid-2">
    <div class="card stack">
      <b style="font-size:15px;color:var(--br-navy)">Caso A · Alias inexistente</b>
      {field("Alias del beneficiario", inp("@mariapérez","", "err", icon="at", suf="No encontrado"), "No encontramos este alias en el directorio nacional.","hint error")}
      {alert('err','Alias no encontrado','Verifica que esté bien escrito o pídele a la persona que confirme su alias en su banco. También puedes pagar con el número de cuenta.')}
      <div class="hstack" style="gap:10px"><div class="btn btn-outline sm">{ico('refresh',16)} Reintentar</div><div class="btn btn-outline sm">{ico('bank',16)} Pagar con número de cuenta</div></div>
      <div class="dashed" style="margin:8px 0"></div>
      <b style="font-size:15px;color:var(--br-navy)">Caso B · Alias inactivo</b>
      {alert('warn','El alias existe pero está inactivo','El titular lo desactivó temporalmente o su cuenta está inhabilitada para recibir. No es posible completar el pago.')}
    </div>
    <div class="card stack">
      <b style="font-size:15px;color:var(--br-navy)">Caso C · Alias con reportes de fraude</b>
      {field("Alias del beneficiario", inp("@ofertas.rd2026","", "err", icon="at", suf="Riesgo alto"))}
      <div class="card flat stack sm" style="border:2px solid var(--err);background:#FDF6F6">
        <div class="hstack" style="gap:14px">
          <div style="width:52px;height:52px;border-radius:50%;background:var(--err-bg);color:var(--err);display:flex;align-items:center;justify-content:center">{ico('alert',26)}</div>
          <div><b style="font-size:17px;color:var(--err)">Este alias ha sido reportado</b>
          <div class="hint">14 usuarios lo reportaron por estafa en los últimos 30 días.</div></div>
        </div>
        <div class="dashed" style="margin:4px 0"></div>
        <div class="hint" style="line-height:1.7">Si insistes, el pago se realizará bajo tu responsabilidad y podría ser retenido para revisión antifraude.
        Recuerda: <b>los pagos instantáneos no se pueden reversar</b>.</div>
        <div class="hstack" style="align-items:flex-start;gap:10px"><div class="check"></div><span style="font-size:13px;color:var(--ink-2)">Entiendo el riesgo y deseo continuar</span></div>
      </div>
      <div class="hstack"><div class="btn btn-outline">Cancelar pago</div><div class="spacer"></div><div class="btn disabled">Continuar</div></div>
      {alert('info','¿Cómo funciona esta señal?','Se alimenta de los reportes de clientes de todas las entidades y del motor antifraude central. No confirma un delito, es una advertencia preventiva.')}
    </div>
  </div>
</div>"""
    frame("D", "D-04", "Enviar · errores y alias en riesgo", "estados negativos", body)

    # D-05 monto
    body = f"""
<div class="stack">
  {page_head("¿Cuánto quieres enviar?","",["Pago Instantáneo","Enviar pago"])}
  {stepper(SEND_STEPS,1)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="rowitem" style="background:#F7FBFE;border-color:#BFDDF2"><div class="ic">{ico('user',22)}</div><div class="tx"><b>M**** F***** P***** G*****</b><span>@mariaperez · Banco Popular</span></div><div class="btn btn-outline sm" style="margin-left:auto">Cambiar</div></div>
      {field("Monto a enviar", inp("2,500.00","", "big focus", pre="DOP"), "Disponible en la cuenta: DOP 2,383.33")}
      <div class="hstack" style="gap:8px">{"".join(f'<div class="btn btn-outline sm">DOP {m}</div>' for m in ["500","1,000","2,000","5,000"])}</div>
      <div class="stack sm">
        <div class="label">Cuenta de origen</div>
        {acct_row("Cuenta corriente","No. ****3341","DOP 2,383.33",sel=True,icon="refresh")}
        {acct_row("Cuenta de ahorros","No. ****8890","DOP 499.13")}
      </div>
      {field("Concepto <span class='opt'>(lo verá el beneficiario)</span>", inp("Pago del almuerzo","",suf="18/40"))}
      {field("Referencia interna <span class='opt'>(opcional, solo tú la ves)</span>", inp("Ej. gasto personal", True))}
      <div class="hstack" style="align-items:flex-start;gap:10px"><div class="check"></div><span style="font-size:13.5px;color:var(--ink-2)">Programar este pago para otra fecha</span></div>
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('sliders',20)}</div><h3>Tus límites</h3></div>
        <div class="limit-bar"><div class="lt"><span>Por transacción</span><b>DOP 25,000</b></div><div class="progress"><i style="width:10%"></i></div></div>
        <div class="limit-bar"><div class="lt"><span>Diario disponible</span><b>DOP 48,080</b></div><div class="progress"><i style="width:4%"></i></div></div>
        <div class="limit-bar"><div class="lt"><span>Beneficiario nuevo (24 h)</span><b>DOP 10,000</b></div><div class="progress"><i class="warn" style="width:25%"></i></div></div>
        <div class="btn btn-outline sm block">{ico('sliders',15)} Ajustar límites</div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('money',20)}</div><h3>Costos</h3></div>
        <div class="kv"><div class="k">Comisión</div><div class="v" style="color:var(--ok)">DOP 0.00</div></div>
        <div class="kv"><div class="k">Impuesto 0.15% (Ley 288-04)</div><div class="v">DOP 3.75</div></div>
        <div class="kv"><div class="k">Total a debitar</div><div class="v" style="font-size:16px">DOP 2,503.75</div></div>
      </div>
    </div>
  </div>
</div>"""
    frame("D", "D-05", "Enviar · paso 2 monto y concepto", "2/4", body)

    # D-06 revision
    body = f"""
<div class="stack">
  {page_head("Revisa y confirma tu pago","Verifica cada dato. El pago es inmediato e irrevocable.",["Pago Instantáneo","Enviar pago"])}
  {stepper(SEND_STEPS,2)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div style="text-align:center;padding:10px 0">
        <div class="hint">Vas a enviar</div>
        <div class="amount lg">DOP 2,500<small>.00</small></div>
      </div>
      <div class="dashed"></div>
      {kv([("Beneficiario","M**** F***** P***** G*****<small>@mariaperez</small>"),
           ("Entidad receptora","Banco Popular Dominicano"),
           ("Tipo de cuenta","Ahorros"),
           ("Cuenta de origen","Cuenta corriente ****3341"),
           ("Concepto","Pago del almuerzo"),
           ("Comisión","DOP 0.00"),
           ("Impuesto 0.15%","DOP 3.75"),
           ("Total a debitar","<span style='font-size:18px'>DOP 2,503.75</span>"),
           ("Fecha de ejecución","Inmediata · 02 sep. 2026 15:12"),
           ("Referencia","Se generará al confirmar")])}
      {alert('warn','Este pago no se puede cancelar','Si te equivocas de beneficiario, solo podrás solicitar una devolución voluntaria a esa persona.')}
      <div class="hstack"><div class="btn btn-outline">{ico('edit',18)} Modificar</div><div class="spacer"></div><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary lg">Autorizar pago {ico('lock',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Qué pasará</h3></div>
        <div class="hstack" style="gap:10px"><div style="color:var(--br-orange)">{ico('lock',18)}</div><span class="hint">Te pediremos una <b>autorización adicional</b></span></div>
        <div class="hstack" style="gap:10px"><div style="color:var(--br-orange)">{ico('transfer',18)}</div><span class="hint">El débito y el crédito ocurren en <b>menos de 20 segundos</b></span></div>
        <div class="hstack" style="gap:10px"><div style="color:var(--br-orange)">{ico('bell',18)}</div><span class="hint">Recibirás alerta por push y correo</span></div>
        <div class="hstack" style="gap:10px"><div style="color:var(--br-orange)">{ico('doc',18)}</div><span class="hint">Tendrás un comprobante descargable con referencia única</span></div>
      </div>
      <div class="card stack sm" style="background:var(--br-navy);color:#fff">
        <div class="hstack">{ico('shieldcheck',20)}<b style="font-size:15px">Sesión protegida</b></div>
        <div style="font-size:12.5px;line-height:1.8;color:#C9DCEC">
          Dispositivo de confianza: <b>Chrome · Windows · Santo Domingo</b><br>
          IP: 126.1.28.49 · Riesgo de la operación: <b style="color:#7BE0A8">Bajo</b><br>
          La sesión se cerrará automáticamente tras 5 min de inactividad.
        </div>
      </div>
    </div>
  </div>
</div>"""
    frame("D", "D-06", "Enviar · paso 3 revisión", "3/4", body)

    # D-07 metodo 2FA
    modal = f"""<div class="scrim"><div class="modal">
  <div class="modal-head"><div class="ico" style="width:34px;height:34px;border-radius:10px;background:var(--br-orange-050);color:var(--br-orange);display:flex;align-items:center;justify-content:center">{ico('lock',20)}</div><h3>Autoriza tu pago</h3><div class="x">{ico('x',20)}</div></div>
  <div class="modal-body stack">
    <div class="hint">Elige cómo quieres confirmar el envío de <b>DOP 2,500.00</b> a <b>@mariaperez</b>.</div>
    <div class="rowitem sel"><div class="radio on"></div><div class="ic">{ico('bell',22)}</div><div class="tx"><b>Aprobación en la App TuBanco</b><span>Notificación con huella o Face ID · más seguro</span></div><span class="badge ok" style="margin-left:auto">Recomendado</span></div>
    <div class="rowitem"><div class="radio"></div><div class="ic">{ico('key',22)}</div><div class="tx"><b>Token blando (6 dígitos)</b><span>Genera el código en tu App TuBanco</span></div></div>
    <div class="rowitem"><div class="radio"></div><div class="ic">{ico('phone',22)}</div><div class="tx"><b>Código por SMS</b><span>Al 809-***-1234</span></div></div>
    <div class="rowitem"><div class="radio"></div><div class="ic">{ico('mail',22)}</div><div class="tx"><b>Código por correo</b><span>edw****@correo.com</span></div></div>
    {alert('info','¿Por qué me lo piden?','Toda transferencia a terceros requiere un segundo factor de autenticación, según la normativa de seguridad bancaria.','shieldcheck')}
  </div>
  <div class="modal-foot"><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary">Continuar</div></div>
</div></div>"""
    body = f"""<div class="stack">{page_head("Revisa y confirma tu pago","",["Pago Instantáneo","Enviar pago"])}{stepper(SEND_STEPS,3)}<div style="height:440px"></div></div>"""
    frame("D", "D-07", "Enviar · paso 4 método de autenticación", "4/4 · modal", body, scrim=modal)

    # D-08 OTP
    modal = f"""<div class="scrim"><div class="modal sm">
  <div class="modal-head"><div class="ico" style="width:34px;height:34px;border-radius:10px;background:var(--br-orange-050);color:var(--br-orange);display:flex;align-items:center;justify-content:center">{ico('key',20)}</div><h3>Código de autorización</h3><div class="x">{ico('x',20)}</div></div>
  <div class="modal-body stack">
    <div class="hint">Ingresa el código de 6 dígitos enviado al <b>809-***-1234</b>. El código está ligado a este pago: <b>DOP 2,500.00 → @mariaperez</b>.</div>
    <div class="otp"><div class="b on">9</div><div class="b on">1</div><div class="b on">4</div><div class="b on">0</div><div class="b cursor"></div><div class="b"></div></div>
    <div class="hstack"><span class="badge info">{ico('clock',13,2.4)} 01:12</span><span class="hint">Reenviar código</span></div>
    <div class="hint error">{ico('alert',14,2.6)} Código incorrecto. Te quedan 2 intentos.</div>
    {alert('err','Cuidado con el fraude','Si alguien te llama pidiendo este código, cuelga. Banreservas nunca lo solicita.','shieldcheck')}
  </div>
  <div class="modal-foot"><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary">Autorizar pago</div></div>
</div></div>"""
    body = f"""<div class="stack">{page_head("Revisa y confirma tu pago","",["Pago Instantáneo","Enviar pago"])}{stepper(SEND_STEPS,3)}<div style="height:440px"></div></div>"""
    frame("D", "D-08", "Enviar · OTP con error", "4/4 · modal", body, scrim=modal)

    # D-09 push movil
    mb = f"""
<div class="phone-status"><span>9:41</span><div class="hstack" style="gap:6px">{ico('wifi',15)}<span>100%</span></div></div>
<div style="flex:1;background:linear-gradient(160deg,#00396B,#0A6FB7);padding:22px;display:flex;flex-direction:column;gap:18px;color:#fff">
  <div class="hstack" style="gap:10px">{LOGO}<b style="letter-spacing:.6px">TUBANCO</b><div class="spacer"></div>{ico('bell',20)}</div>
  <div style="background:#fff;border-radius:20px;padding:22px;color:var(--ink);box-shadow:var(--sh-3)">
    <div style="text-align:center">
      <div style="width:64px;height:64px;border-radius:50%;background:var(--br-orange-050);color:var(--br-orange);display:flex;align-items:center;justify-content:center;margin:0 auto 12px">{ico('lock',32)}</div>
      <b style="font-size:18px;color:var(--br-navy)">Autoriza tu pago</b>
      <div class="hint" style="margin-top:4px">Solicitud desde Internet Banking</div>
      <div class="amount" style="font-size:34px;margin:16px 0">DOP 2,500<small>.00</small></div>
    </div>
    <div class="dashed" style="margin:0 -22px 12px"></div>
    {kv([("Para","M**** P***** G*****"),("Alias","@mariaperez"),("Entidad","Banco Popular"),("Concepto","Pago del almuerzo")])}
    <div class="alert warn" style="margin-top:12px;font-size:12.5px"><div class="ai">{ico('alert',18)}</div><div>Si no reconoces esta operación, recházala y llama al 809-960-2000.</div></div>
    <div style="margin-top:16px;display:flex;flex-direction:column;align-items:center;gap:10px">
      <div style="width:76px;height:76px;border-radius:50%;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center">{ico('fingerprint',40)}</div>
      <span class="hint" style="text-align:center">Toca y confirma con tu huella</span>
    </div>
    <div class="btn btn-primary block lg" style="margin-top:14px">Aprobar</div>
    <div class="btn btn-danger block" style="margin-top:8px">Rechazar</div>
    <div class="hint" style="text-align:center;margin-top:10px">Expira en 01:38</div>
  </div>
  <div class="hint" style="color:#BBD9F1;text-align:center;font-size:12px">Dispositivo: iPhone de Edward · Santo Domingo</div>
</div>
<div class="phone-nav">{ico('home',22)}{ico('transfer',22)}{ico('qr',22)}{ico('user',22)}</div>"""
    frame("D", "D-09", "Enviar · aprobación push (App TuBanco)", "390×844 · 2FA", mb, chrome=False, kind="mobile")

    # D-10 procesando
    body = f"""
<div class="stack">
  {page_head("Procesando tu pago","No cierres ni actualices esta ventana.",["Pago Instantáneo","Enviar pago"])}
  <div style="display:flex;justify-content:center;padding-top:30px">
    <div class="card" style="width:700px;text-align:center;padding:48px">
      <div style="width:96px;height:96px;border-radius:50%;border:6px solid #E4EAF1;border-top-color:var(--br-orange);margin:0 auto 22px"></div>
      <h1 class="page" style="font-size:24px">Enviando DOP 2,500.00 a @mariaperez</h1>
      <p class="page-sub">Estamos liquidando la operación en el sistema de pagos inmediatos.</p>
      <div class="stack sm" style="margin-top:26px;text-align:left">
        <div class="hstack"><div style="color:var(--ok)">{ico('check',20,3)}</div><span class="hint">Autenticación verificada</span><span class="spacer"></span><span class="badge ok">Listo</span></div>
        <div class="hstack"><div style="color:var(--ok)">{ico('check',20,3)}</div><span class="hint">Fondos reservados en tu cuenta</span><span class="spacer"></span><span class="badge ok">Listo</span></div>
        <div class="hstack"><div style="color:var(--br-orange)">{ico('refresh',20)}</div><span class="hint">Enviando al banco receptor</span><span class="spacer"></span><span class="badge warn">En curso</span></div>
        <div class="hstack"><div style="color:var(--ink-3)">{ico('clock',20)}</div><span class="hint">Confirmación de acreditación</span><span class="spacer"></span><span class="badge neutral">Pendiente</span></div>
      </div>
      <div class="progress" style="margin-top:24px"><i style="width:62%"></i></div>
      <div class="hint" style="margin-top:10px">Tiempo estimado: 8 segundos</div>
    </div>
  </div>
</div>"""
    frame("D", "D-10", "Enviar · procesando", "estado de sistema", body)

    # D-11 comprobante
    body = f"""
<div class="stack">
  {page_head("Pago completado","",["Pago Instantáneo","Enviar pago","Comprobante"],
   f'<div class="btn btn-outline sm">{ico("print",16)} Imprimir</div><div class="btn btn-outline sm">{ico("download",16)} PDF</div><div class="btn btn-primary sm">{ico("share",16)} Compartir</div>')}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="receipt">
      <div class="rh">
        <div class="ic">{ico('check',36,3)}</div>
        <b style="font-size:20px;color:#0B6438">¡Pago enviado con éxito!</b>
        <div class="amount ok" style="font-size:40px">DOP 2,500<small>.00</small></div>
        <span class="hint" style="color:#0B6438">Acreditado en 6 segundos · 02 de sep. de 2026, 15:12:41</span>
      </div>
      <div class="notch"></div>
      <div class="rb">
        {kv([("Beneficiario","M**** F***** P***** G*****"),("Alias","@mariaperez"),("Entidad receptora","Banco Popular Dominicano"),
             ("Cuenta de origen","Cuenta corriente ****3341"),("Concepto","Pago del almuerzo"),
             ("Monto","DOP 2,500.00"),("Comisión","DOP 0.00"),("Impuesto 0.15%","DOP 3.75"),
             ("Total debitado","<span style='font-size:17px'>DOP 2,503.75</span>"),
             ("Balance disponible","DOP 4,887.08 → DOP 2,383.33"),
             ("Referencia Banreservas","<span style='font-family:monospace'>PI-26-0098231</span>"),
             ("Referencia del sistema","<span style='font-family:monospace'>RD26090215124178</span>"),
             ("Canal","Internet Banking · Chrome/Windows")])}
        <div class="dashed" style="margin:16px -26px"></div>
        <div class="hstack" style="gap:10px;flex-wrap:wrap">
          <div class="btn btn-outline sm">{ico('star',15)} Guardar como favorito</div>
          <div class="btn btn-outline sm">{ico('refresh',15)} Repetir pago</div>
          <div class="btn btn-outline sm">{ico('request',15)} Solicitar devolución</div>
          <div class="btn btn-outline sm">{ico('alert',15)} Reportar problema</div>
        </div>
      </div>
    </div>
    <div class="stack">
      {alert('ok','Ya notificamos al beneficiario','María recibió una alerta en su banco con tu nombre y el concepto.','check')}
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('qr',20)}</div><h3>Comprobante verificable</h3></div>
        <div class="qr-box">{qr(150,3)}</div>
        <div class="hint" style="text-align:center">Escanea para validar la autenticidad del comprobante en banreservas.com/verificar</div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('sliders',20)}</div><h3>Límite restante hoy</h3></div>
        <div class="limit-bar"><div class="lt"><span>Diario</span><b>DOP 45,580 de 50,000</b></div><div class="progress"><i style="width:9%"></i></div></div>
      </div>
      <div class="hstack"><div class="btn btn-outline block">Ir al inicio</div><div class="btn btn-primary block">Hacer otro pago</div></div>
    </div>
  </div>
</div>"""
    frame("D", "D-11", "Enviar · comprobante exitoso", "resultado", body)

    # D-12 errores de resultado
    def errcard(icon, color, title, text, actions, badge):
        return f"""<div class="card stack sm">
      <div class="hstack" style="gap:14px"><div style="width:52px;height:52px;border-radius:50%;background:{color[1]};color:{color[0]};display:flex;align-items:center;justify-content:center;flex:none">{ico(icon,26)}</div>
      <div><b style="font-size:17px;color:var(--br-navy)">{title}</b><div class="hint" style="line-height:1.6;margin-top:3px">{text}</div></div>
      <span class="badge {badge[1]}" style="margin-left:auto">{badge[0]}</span></div>
      <div class="hstack" style="gap:10px;flex-wrap:wrap">{actions}</div></div>"""
    body = f"""
<div class="stack">
  {page_head("Estados de resultado del pago","Casos que el usuario puede encontrar al finalizar.",["Pago Instantáneo","Enviar pago","Estados"])}
  <div class="grid-2">
    {errcard('money',('var(--err)','var(--err-bg)'),'Fondos insuficientes','Tu cuenta corriente ****3341 tiene DOP 2,383.33 y el total a debitar es DOP 2,503.75. No se debitó ningún valor.',f'<div class="btn btn-outline sm">Cambiar de cuenta</div><div class="btn btn-outline sm">Cambiar el monto</div>',('No procesado','err'))}
    {errcard('sliders',('var(--warn)','var(--warn-bg)'),'Límite diario excedido','Este pago supera tu límite diario disponible (DOP 48,080). Puedes ajustar tus límites; el aumento se activa en 24 horas.',f'<div class="btn btn-outline sm">Ajustar límites</div><div class="btn btn-outline sm">Enviar un monto menor</div>',('Bloqueado','warn'))}
    {errcard('bank',('var(--err)','var(--err-bg)'),'Rechazado por el banco receptor','La cuenta del beneficiario no admite depósitos (inactiva o embargada). El débito fue reversado automáticamente a tu cuenta.',f'<div class="btn btn-outline sm">Ver reversa PI-26-0098232</div><div class="btn btn-outline sm">Intentar con otro alias</div>',('Reversado','info'))}
    {errcard('clock',('var(--warn)','var(--warn-bg)'),'Sin confirmación del receptor','La red no confirmó la acreditación en el tiempo esperado. La operación quedó en verificación: si no se acredita en 30 minutos, el monto se devuelve automáticamente.',f'<div class="btn btn-outline sm">Ver estado en Movimientos</div><div class="btn btn-outline sm">{ico("refresh",15)} Actualizar</div>',('En verificación','warn'))}
    {errcard('shield',('var(--err)','var(--err-bg)'),'Retenido por seguridad','El motor antifraude detectó un patrón inusual (monto atípico + beneficiario nuevo + dispositivo reciente). Un analista validará la operación o te llamaremos al 809-***-1234.',f'<div class="btn btn-primary sm">Validar por llamada</div><div class="btn btn-outline sm">Cancelar operación</div>',('Retenido','err'))}
    {errcard('device',('var(--err)','var(--err-bg)'),'Sesión expirada durante la autorización','Por seguridad cerramos la sesión tras 5 minutos de inactividad. El pago no se ejecutó y no se debitó ningún valor.',f'<div class="btn btn-primary sm">Iniciar sesión de nuevo</div>',('No procesado','neutral'))}
  </div>
</div>"""
    frame("D", "D-12", "Enviar · estados de error y excepción", "matriz de errores", body)

    # D-13 step-up beneficiario nuevo
    body = f"""
<div class="stack">
  {page_head("Verificación adicional requerida","Estás pagando a un beneficiario nuevo por un monto alto.",["Pago Instantáneo","Enviar pago"])}
  {stepper(SEND_STEPS,3)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      {alert('warn','Autenticación reforzada (step-up)','Detectamos: beneficiario registrado hace menos de 24 h, monto 8× superior a tu promedio y dispositivo usado por primera vez. Necesitamos confirmar que eres tú.')}
      <div class="stack sm">
        <div class="label">Completa estos dos pasos</div>
        <div class="rowitem"><div class="ic" style="background:var(--ok-bg);color:var(--ok)">{ico('check',22,3)}</div><div class="tx"><b>1. Aprobación en la App TuBanco</b><span>Confirmada con huella a las 15:11</span></div><span class="badge ok" style="margin-left:auto">Listo</span></div>
        <div class="rowitem sel"><div class="ic">{ico('fingerprint',22)}</div><div class="tx"><b>2. Verificación de identidad (selfie)</b><span>Prueba de vida en la App · toma 20 segundos</span></div><span class="badge warn" style="margin-left:auto">Pendiente</span></div>
      </div>
      <div class="dashed" style="margin:6px 0"></div>
      <div class="stack sm">
        <div class="label">Alternativas</div>
        <div class="hstack" style="gap:10px;flex-wrap:wrap">
          <div class="btn btn-outline sm">{ico('clock',15)} Programar para dentro de 24 h</div>
          <div class="btn btn-outline sm">{ico('money',15)} Reducir a DOP 10,000</div>
          <div class="btn btn-outline sm">{ico('phone',15)} Autorizar por Contact Center</div>
        </div>
      </div>
      <div class="hstack"><div class="btn btn-ghost">Cancelar pago</div><div class="spacer"></div><div class="btn btn-primary">Continuar en la App {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('shield',20)}</div><h3>Evaluación de riesgo</h3></div>
        <div class="limit-bar"><div class="lt"><span>Score de la operación</span><b style="color:var(--err)">72 / 100 · Alto</b></div><div class="progress"><i class="err" style="width:72%"></i></div></div>
        <div class="kv"><div class="k">Beneficiario</div><div class="v" style="color:var(--err)">Nuevo (2 h)</div></div>
        <div class="kv"><div class="k">Monto vs. promedio</div><div class="v" style="color:var(--warn)">8.3×</div></div>
        <div class="kv"><div class="k">Dispositivo</div><div class="v" style="color:var(--warn)">Primer uso</div></div>
        <div class="kv"><div class="k">Geolocalización</div><div class="v" style="color:var(--ok)">Habitual</div></div>
        <div class="kv"><div class="k">Horario</div><div class="v" style="color:var(--ok)">Habitual</div></div>
      </div>
      {alert('info','¿Te están presionando para pagar?','Si alguien te apura o te dicta pasos por teléfono, detente. Es el patrón típico de estafa por ingeniería social.','alert')}
    </div>
  </div>
</div>"""
    frame("D", "D-13", "Enviar · autenticación reforzada", "antifraude", body)

# ======================================================== E. SOLICITAR PAGO
REQ_STEPS = ["A quién","Monto y vigencia","Revisión","Compartir"]

def g_solicitar():
    # E-01
    body = f"""
<div class="stack">
  {page_head("Solicitar un pago","Genera un cobro y compártelo por enlace, QR o directamente a un alias.",["Pago Instantáneo","Solicitar pago"])}
  {stepper(REQ_STEPS,0)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="tabs"><div class="tab active">{ico('at',18)} A un alias</div><div class="tab">{ico('star',18)} A un contacto</div><div class="tab">{ico('link',18)} Enlace abierto</div></div>
      {field("Alias de quien te va a pagar", inp("@carlosgm","", "ok", icon="at", suf="Encontrado"))}
      <div class="rowitem" style="background:#F7FBFE;border-color:#BFDDF2"><div class="ic">{ico('user',22)}</div><div class="tx"><b>C***** A***** G***** M*****</b><span>@carlosgm · Banreservas</span></div><span class="badge ok" style="margin-left:auto">Alias verificado</span></div>
      <div class="stack sm">
        <div class="label">O elige un contacto frecuente</div>
        <div class="grid-4">
          {"".join(f'<div class="card flat" style="display:flex;flex-direction:column;align-items:center;gap:8px;padding:16px 10px;text-align:center"><div style="width:44px;height:44px;border-radius:50%;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center;font-weight:800">{i}</div><b style="font-size:13px;color:var(--br-navy)">{n}</b><span class="hint" style="font-size:11.5px">{a}</span></div>' for i,n,a in [("MP","María P.","@mariaperez"),("JR","Juan R.","809-***-4471"),("LS","Luisa S.","luisa***@..."),("PT","Pedro T.","@pedrot")])}
        </div>
      </div>
      {alert('info','¿Enlace abierto?','Genera un cobro sin destinatario: cualquiera que abra el enlace o escanee el QR puede pagarlo. Ideal para grupos y ventas.','link')}
      <div class="hstack"><div class="btn btn-ghost">Cancelar</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('money',20)}</div><h3>Cuenta de abono</h3></div>
        {acct_row("Cuenta corriente","No. ****3341 · alias 809-555-1234","DOP 2,383.33",sel=True,icon="refresh")}
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('shieldcheck',20)}</div><h3>Seguridad del cobro</h3></div>
        <div class="hint" style="line-height:1.7">Una solicitud <b>no mueve dinero por sí sola</b>: quien paga siempre debe autorizar con su propio banco y su doble factor. Nunca pidas a nadie que te dicte un código.</div>
      </div>
    </div>
  </div>
</div>"""
    frame("E", "E-01", "Solicitar · paso 1 destinatario", "1/4", body)

    # E-02
    body = f"""
<div class="stack">
  {page_head("¿Cuánto vas a cobrar?","",["Pago Instantáneo","Solicitar pago"])}
  {stepper(REQ_STEPS,1)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="rowitem" style="background:#F7FBFE;border-color:#BFDDF2"><div class="ic">{ico('user',22)}</div><div class="tx"><b>C***** A***** G***** M*****</b><span>@carlosgm</span></div><div class="btn btn-outline sm" style="margin-left:auto">Cambiar</div></div>
      {field("Monto a cobrar", inp("2,300.00","", "big focus", pre="DOP"))}
      <div class="hstack" style="align-items:flex-start;gap:10px"><div class="check"></div><span style="font-size:13.5px;color:var(--ink-2)">Permitir que el pagador modifique el monto <span class="hint" style="display:inline">(útil para donaciones o propinas)</span></span></div>
      {field("Concepto", inp("Alquiler de septiembre · apto 4B","",suf="30/60"))}
      <div class="grid-2">
        {field("Vence el", inp("07/09/2026","",icon="calendar"))}
        {field("A las", inp("23:59","",icon="clock"))}
      </div>
      <div class="hstack" style="gap:8px">{"".join(f'<div class="btn btn-outline sm">{t}</div>' for t in ["24 horas","3 días","7 días","30 días"])}</div>
      {field("Adjuntar factura <span class='opt'>(opcional)</span>", f'<div class="input" style="height:auto;padding:16px;justify-content:center;border-style:dashed;color:var(--ink-3)">{ico("upload",20)} Arrastra un PDF o imagen (máx. 2 MB)</div>')}
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('bell',20)}</div><h3>Recordatorios</h3></div>
        <div class="hstack"><div class="switch on"><i></i></div><span class="hint">Avisar al pagador 24 h antes del vencimiento</span></div>
        <div class="hstack"><div class="switch on"><i></i></div><span class="hint">Notificarme cuando la paguen</span></div>
        <div class="hstack"><div class="switch"><i></i></div><span class="hint">Reenviar automáticamente si no responde en 48 h</span></div>
      </div>
      {alert('warn','Límite de solicitudes','Puedes tener hasta 20 solicitudes activas. Las vencidas se archivan automáticamente.')}
    </div>
  </div>
</div>"""
    frame("E", "E-02", "Solicitar · paso 2 monto y vigencia", "2/4", body)

    # E-03
    body = f"""
<div class="stack">
  {page_head("Revisa tu solicitud de pago","",["Pago Instantáneo","Solicitar pago"])}
  {stepper(REQ_STEPS,2)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div style="text-align:center;padding:8px 0"><div class="hint">Vas a cobrar</div><div class="amount lg">DOP 2,300<small>.00</small></div></div>
      <div class="dashed"></div>
      {kv([("Para","C***** A***** G***** M*****<small>@carlosgm · Banreservas</small>"),
           ("Concepto","Alquiler de septiembre · apto 4B"),
           ("Cuenta de abono","Cuenta corriente ****3341"),
           ("Monto modificable","No"),
           ("Vence","07 de sep. de 2026, 23:59"),
           ("Recordatorio","24 h antes del vencimiento"),
           ("Costo para ti","DOP 0.00")])}
      {alert('info','La solicitud no debita a nadie','Carlos recibirá una notificación y decidirá si la paga o la rechaza desde su propio banco.')}
      <div class="hstack"><div class="btn btn-outline">{ico('edit',18)} Modificar</div><div class="spacer"></div><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary lg">Crear y enviar</div></div>
    </div>
    <div class="card stack sm" style="align-self:flex-start"><div class="card-head"><div class="ico">{ico('eye',20)}</div><h3>Así lo verá Carlos</h3></div>
      <div class="card flat stack sm" style="background:#F8FAFC">
        <div class="hstack" style="gap:10px">{ico('request',20)}<b style="font-size:14px;color:var(--br-navy)">Nueva solicitud de pago</b></div>
        <div class="hint"><b>E***** F***** S.</b> te solicita</div>
        <div class="amount" style="font-size:28px">DOP 2,300.00</div>
        <div class="hint">Alquiler de septiembre · apto 4B</div>
        <div class="hstack" style="gap:8px"><div class="btn btn-primary sm">Pagar</div><div class="btn btn-outline sm">Rechazar</div></div>
      </div>
    </div>
  </div>
</div>"""
    frame("E", "E-03", "Solicitar · paso 3 revisión", "3/4", body)

    # E-04 compartir
    body = f"""
<div class="stack">
  {page_head("Solicitud creada","Compártela para que te paguen.",["Pago Instantáneo","Solicitar pago"])}
  {stepper(REQ_STEPS,3)}
  <div class="grid-2" style="grid-template-columns:1fr 460px">
    <div class="card stack">
      <div class="hstack" style="gap:14px">
        <div style="width:54px;height:54px;border-radius:50%;background:var(--ok-bg);color:var(--ok);display:flex;align-items:center;justify-content:center">{ico('check',28,3)}</div>
        <div><b style="font-size:19px;color:var(--br-navy)">Enviada a @carlosgm</b><div class="hint">Referencia SP-26-0004410 · vence el 07 sep. 2026, 23:59</div></div>
        <span class="badge warn" style="margin-left:auto">Pendiente de pago</span>
      </div>
      <div class="dashed"></div>
      {field("Enlace de pago", f'<div class="input ro"><span style="font-family:monospace;font-size:13.5px">https://pago.banreservas.com.do/r/SP26-0004410-8KQ2</span><span class="suf" style="color:var(--br-blue-600)">{ico("copy",16)} Copiar</span></div>', "El enlace es de un solo uso y expira con la solicitud.")}
      <div class="stack sm">
        <div class="label">Compartir por</div>
        <div class="grid-4">
          <div class="rowitem" style="justify-content:center;gap:8px">{ico('wa',20)}<b style="font-size:13px">WhatsApp</b></div>
          <div class="rowitem" style="justify-content:center;gap:8px">{ico('mail',20)}<b style="font-size:13px">Correo</b></div>
          <div class="rowitem" style="justify-content:center;gap:8px">{ico('phone',20)}<b style="font-size:13px">SMS</b></div>
          <div class="rowitem" style="justify-content:center;gap:8px">{ico('download',20)}<b style="font-size:13px">Descargar</b></div>
        </div>
      </div>
      {alert('warn','Comparte solo con quien debe pagarte','Cualquiera con el enlace puede pagar esta solicitud; nadie puede cobrarte con él.')}
      <div class="hstack"><div class="btn btn-outline">Ver mis solicitudes</div><div class="spacer"></div><div class="btn btn-primary">Crear otra solicitud</div></div>
    </div>
    <div class="card stack sm" style="align-items:center">
      <div class="card-head" style="width:100%"><div class="ico">{ico('qr',20)}</div><h3>QR de cobro</h3></div>
      <div class="qr-box">{qr(200,11)}</div>
      <b style="font-size:18px;color:var(--br-navy)">DOP 2,300.00</b>
      <span class="hint" style="text-align:center">Alquiler de septiembre · apto 4B<br>Vence en 4 días 8 horas</span>
      <div class="hstack" style="gap:8px"><div class="btn btn-outline sm">{ico('download',15)} PNG</div><div class="btn btn-outline sm">{ico('print',15)} Imprimir</div></div>
    </div>
  </div>
</div>"""
    frame("E", "E-04", "Solicitar · paso 4 compartir", "4/4", body)

    # E-05 bandeja enviadas
    def rrow(ref, who, concept, amount, badge, date):
        return f'<tr><td><b>{who}</b><div class="hint">{concept}</div></td><td>{ref}</td><td>{date}</td><td class="num">DOP {amount}</td><td style="text-align:right">{badge}</td><td style="text-align:right;color:var(--ink-3)">{ico("chevr",18)}</td></tr>'
    body = f"""
<div class="stack">
  {page_head("Mis solicitudes de pago","",["Pago Instantáneo","Solicitudes"],
    f'<div class="btn btn-outline sm">{ico("filter",16)} Filtrar</div><div class="btn btn-primary sm">{ico("plus",16)} Nueva solicitud</div>')}
  <div class="tabs" style="max-width:640px"><div class="tab active">{ico('arrowup',18)} Enviadas (6)</div><div class="tab">{ico('arrowdown',18)} Recibidas (2)</div></div>
  <div class="grid-4">
    <div class="card"><div class="hint">Pendientes</div><div class="amount" style="font-size:30px">4</div><div class="hint">DOP 9,120.00 por cobrar</div></div>
    <div class="card"><div class="hint">Pagadas (30 días)</div><div class="amount ok" style="font-size:30px">11</div><div class="hint">DOP 34,500.00 recibidos</div></div>
    <div class="card"><div class="hint">Vencidas</div><div class="amount" style="font-size:30px;color:var(--ink-3)">3</div><div class="hint">Se archivan a los 90 días</div></div>
    <div class="card"><div class="hint">Rechazadas</div><div class="amount" style="font-size:30px;color:var(--err)">1</div><div class="hint">Con motivo del pagador</div></div>
  </div>
  <div class="card">
    <table class="table">
      <tr><th>Destinatario</th><th>Referencia</th><th>Vence</th><th style="text-align:right">Monto</th><th style="text-align:right">Estado</th><th></th></tr>
      {rrow("SP-26-0004410","@carlosgm","Alquiler de septiembre · apto 4B","2,300.00",'<span class="badge warn">Pendiente</span>',"07 sep. 23:59")}
      {rrow("SP-26-0004398","@mariaperez","División de la cena","850.00",'<span class="badge ok">Pagada</span>',"—")}
      {rrow("SP-26-0004381","Enlace abierto","Rifa del equipo · 12 pagos","500.00",'<span class="badge info">Activa · 7 de 12</span>',"30 sep. 23:59")}
      {rrow("SP-26-0004350","809-***-4471","Reparación del aire","4,800.00",'<span class="badge warn">Pendiente</span>',"04 sep. 18:00")}
      {rrow("SP-26-0004311","@pedrot","Curso de inglés","1,170.00",'<span class="badge err">Rechazada</span>',"—")}
      {rrow("SP-26-0004290","luisa***@correo.com","Aporte cumpleaños","1,000.00",'<span class="badge neutral">Vencida</span>',"28 ago. 23:59")}
    </table>
  </div>
</div>"""
    frame("E", "E-05", "Solicitar · bandeja de enviadas", "gestión", body)

    # E-06 detalle enviada
    modal = f"""<div class="scrim"><div class="modal lg">
  <div class="modal-head"><div class="ico" style="width:34px;height:34px;border-radius:10px;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center">{ico('request',20)}</div><h3>Solicitud SP-26-0004410</h3><span class="badge warn" style="margin-left:12px">Pendiente</span><div class="x">{ico('x',20)}</div></div>
  <div class="modal-body">
    <div class="grid-2" style="grid-template-columns:1fr 220px">
      <div class="stack sm">
        {kv([("Destinatario","C***** G***** M***** · @carlosgm"),("Monto","DOP 2,300.00"),("Concepto","Alquiler de septiembre · apto 4B"),
             ("Cuenta de abono","Cuenta corriente ****3341"),("Creada","02 sep. 2026, 15:22"),("Vence","07 sep. 2026, 23:59 · en 4 días")])}
        <div class="label" style="margin-top:8px">Seguimiento</div>
        <div class="hstack" style="gap:10px"><div style="color:var(--ok)">{ico('check',18,3)}</div><span class="hint">Creada y enviada · 15:22</span></div>
        <div class="hstack" style="gap:10px"><div style="color:var(--ok)">{ico('check',18,3)}</div><span class="hint">Notificación entregada en el banco de Carlos · 15:22</span></div>
        <div class="hstack" style="gap:10px"><div style="color:var(--ok)">{ico('eye',18)}</div><span class="hint">Vista por el destinatario · 16:04</span></div>
        <div class="hstack" style="gap:10px"><div style="color:var(--ink-3)">{ico('clock',18)}</div><span class="hint">Pendiente de pago</span></div>
      </div>
      <div class="stack sm" style="align-items:center"><div class="qr-box" style="padding:10px">{qr(150,11)}</div><div class="hint" style="text-align:center">QR de esta solicitud</div></div>
    </div>
  </div>
  <div class="modal-foot"><div class="btn btn-danger">Cancelar solicitud</div><div class="spacer"></div><div class="btn btn-outline">{ico('copy',16)} Copiar enlace</div><div class="btn btn-primary">{ico('bell',16)} Enviar recordatorio</div></div>
</div></div>"""
    body = f"""<div class="stack">{page_head("Mis solicitudes de pago","",["Pago Instantáneo","Solicitudes"])}<div style="height:520px"></div></div>"""
    frame("E", "E-06", "Solicitar · detalle de enviada", "modal", body)

    # E-07 recibidas
    body = f"""
<div class="stack">
  {page_head("Solicitudes recibidas","Alguien te pidió un pago. Revisa siempre quién y por qué antes de pagar.",["Pago Instantáneo","Solicitudes"])}
  <div class="tabs" style="max-width:640px"><div class="tab">{ico('arrowup',18)} Enviadas (6)</div><div class="tab active">{ico('arrowdown',18)} Recibidas (2)</div></div>
  {alert('warn','Nunca pagues una solicitud que no esperabas','Los estafadores envían cobros con nombres parecidos a comercios o familiares. Confirma por otro medio antes de autorizar.','shieldcheck')}
  <div class="grid-2">
    <div class="card stack sm" style="border:2px solid var(--br-orange)">
      <div class="hstack"><span class="badge orange">NUEVA</span><span class="hint" style="margin-left:auto">Recibida hace 12 min</span></div>
      <div class="hstack" style="gap:14px">
        <div style="width:52px;height:52px;border-radius:50%;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center;font-weight:800">JR</div>
        <div><b style="font-size:16px;color:var(--br-navy)">J*** R***** M*****</b><div class="hint">@juanrm · Banreservas · contacto frecuente</div></div>
      </div>
      <div class="amount" style="font-size:32px">DOP 1,450.00</div>
      <div class="hint">Concepto: <b>Parte del regalo de Luisa</b></div>
      <div class="hint">Vence el 05 de sep. de 2026, 23:59</div>
      <div class="hstack" style="gap:10px;margin-top:6px"><div class="btn btn-primary">Pagar ahora</div><div class="btn btn-outline">Rechazar</div><div class="btn btn-ghost sm">Ver detalle</div></div>
    </div>
    <div class="card stack sm">
      <div class="hstack"><span class="badge neutral">Recibida ayer</span><span class="badge err" style="margin-left:auto">{ico('alert',13,2.6)} Remitente no habitual</span></div>
      <div class="hstack" style="gap:14px">
        <div style="width:52px;height:52px;border-radius:50%;background:var(--err-bg);color:var(--err);display:flex;align-items:center;justify-content:center">{ico('store',24)}</div>
        <div><b style="font-size:16px;color:var(--br-navy)">SERVICIOS EXPRESS RD SRL</b><div class="hint">@servicios.expressrd · Banco Y · primera vez</div></div>
      </div>
      <div class="amount" style="font-size:32px">DOP 8,900.00</div>
      <div class="hint">Concepto: <b>Confirmación de entrega urgente</b></div>
      {alert('err','Verifica antes de pagar','Es la primera vez que este alias te solicita dinero y tiene 3 reportes recientes. Si no reconoces el cobro, recházalo y repórtalo.')}
      <div class="hstack" style="gap:10px"><div class="btn btn-outline">Rechazar</div><div class="btn btn-danger">{ico('alert',16)} Reportar como fraude</div></div>
    </div>
  </div>
</div>"""
    frame("E", "E-07", "Solicitar · bandeja de recibidas", "cobros entrantes", body)

    # E-08 pagar solicitud
    body = f"""
<div class="stack">
  {page_head("Pagar solicitud SP-26-0004455","Los datos vienen prellenados desde la solicitud.",["Pago Instantáneo","Solicitudes","Pagar"])}
  {stepper(["Solicitud","Revisión","Autenticación","Comprobante"],1)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="rowitem" style="background:#F7FBFE;border-color:#BFDDF2"><div class="ic">{ico('user',22)}</div><div class="tx"><b>J*** R***** M*****</b><span>@juanrm · Banreservas · te solicitó el pago</span></div><span class="badge info" style="margin-left:auto">Solicitud verificada</span></div>
      <div style="text-align:center;padding:6px 0"><div class="hint">Vas a pagar</div><div class="amount lg">DOP 1,450<small>.00</small></div><div class="hint">Monto fijado por quien solicita · no editable</div></div>
      <div class="dashed"></div>
      {kv([("Concepto","Parte del regalo de Luisa"),("Referencia de la solicitud","SP-26-0004455"),("Vence","05 sep. 2026, 23:59"),
           ("Cuenta de origen","Cuenta corriente ****3341<small>Balance DOP 2,383.33</small>"),("Comisión","DOP 0.00"),("Impuesto 0.15%","DOP 2.18"),("Total a debitar","<span style='font-size:17px'>DOP 1,452.18</span>")])}
      {alert('warn','El pago es inmediato e irrevocable','Al autorizar, el dinero sale de tu cuenta al instante.')}
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Volver</div><div class="spacer"></div><div class="btn btn-danger">Rechazar</div><div class="btn btn-primary lg">Autorizar pago {ico('lock',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Historial con este alias</h3></div>
        <div class="kv"><div class="k">Pagos previos</div><div class="v">7 en 12 meses</div></div>
        <div class="kv"><div class="k">Último</div><div class="v">14 ago. 2026 · DOP 900.00</div></div>
        <div class="kv"><div class="k">Reportes</div><div class="v" style="color:var(--ok)">Ninguno</div></div>
      </div>
      {alert('info','Puedes cambiar la cuenta de origen','El abono siempre irá a la cuenta que definió quien te solicitó el pago.')}
    </div>
  </div>
</div>"""
    frame("E", "E-08", "Solicitar · pagar una solicitud recibida", "flujo del pagador", body)

    # E-09 rechazar
    modal = f"""<div class="scrim"><div class="modal sm">
  <div class="modal-head"><div class="ico" style="width:34px;height:34px;border-radius:10px;background:var(--err-bg);color:var(--err);display:flex;align-items:center;justify-content:center">{ico('x',20)}</div><h3>Rechazar solicitud</h3><div class="x">{ico('x',20)}</div></div>
  <div class="modal-body stack sm">
    <div class="hint">Le avisaremos a <b>@servicios.expressrd</b> que no pagarás <b>DOP 8,900.00</b>. Cuéntanos por qué (nos ayuda a detectar fraudes):</div>
    <div class="rowitem sel"><div class="radio on"></div><div class="tx"><b>No reconozco este cobro</b></div></div>
    <div class="rowitem"><div class="radio"></div><div class="tx"><b>El monto o el concepto están equivocados</b></div></div>
    <div class="rowitem"><div class="radio"></div><div class="tx"><b>Ya pagué por otro medio</b></div></div>
    <div class="rowitem"><div class="radio"></div><div class="tx"><b>Creo que es un intento de estafa</b></div></div>
    <div class="hstack" style="align-items:flex-start;gap:10px;margin-top:4px"><div class="check on">{ico('check',14,3)}</div><span style="font-size:13px;color:var(--ink-2)">Bloquear solicitudes futuras de este alias</span></div>
  </div>
  <div class="modal-foot"><div class="btn btn-ghost">Volver</div><div class="btn btn-danger">Rechazar y reportar</div></div>
</div></div>"""
    body = f"""<div class="stack">{page_head("Solicitudes recibidas","",["Pago Instantáneo","Solicitudes"])}<div style="height:520px"></div></div>"""
    frame("E", "E-09", "Solicitar · rechazar con motivo", "modal", body)

# ============================================================ F. PAGAR QR
def g_qr():
    # F-01 hub
    body = f"""
<div class="stack">
  {page_head("Pagos con código QR","Paga en comercios o a otras personas y cobra con tu propio código.",["Pago Instantáneo","QR"])}
  <div class="grid-2">
    <div class="card stack" style="border-top:4px solid var(--br-orange)">
      <div class="hstack" style="gap:14px"><div style="width:54px;height:54px;border-radius:16px;background:var(--br-orange-050);color:var(--br-orange);display:flex;align-items:center;justify-content:center">{ico('scan',28)}</div>
      <div><b style="font-size:20px;color:var(--br-navy)">Pagar con QR</b><div class="hint">Escanea el código del comercio o de otra persona.</div></div></div>
      <div class="grid-3">
        <div class="rowitem" style="flex-direction:column;text-align:center;gap:8px;padding:20px 10px"><div class="ic">{ico('camera',22)}</div><b style="font-size:13px;color:var(--br-navy)">Usar la cámara</b></div>
        <div class="rowitem" style="flex-direction:column;text-align:center;gap:8px;padding:20px 10px"><div class="ic">{ico('upload',22)}</div><b style="font-size:13px;color:var(--br-navy)">Subir imagen</b></div>
        <div class="rowitem" style="flex-direction:column;text-align:center;gap:8px;padding:20px 10px"><div class="ic">{ico('copy',22)}</div><b style="font-size:13px;color:var(--br-navy)">Pegar código</b></div>
      </div>
      <div class="btn btn-primary block">Escanear ahora</div>
    </div>
    <div class="card stack" style="border-top:4px solid var(--br-blue)">
      <div class="hstack" style="gap:14px"><div style="width:54px;height:54px;border-radius:16px;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center">{ico('qr',28)}</div>
      <div><b style="font-size:20px;color:var(--br-navy)">Mi QR para cobrar</b><div class="hint">Muéstralo o compártelo y recibe pagos al instante.</div></div></div>
      <div class="hstack" style="gap:18px">
        <div class="qr-box" style="padding:10px">{qr(120,21)}</div>
        <div class="stack sm">
          <div class="hint">Vinculado a</div><b style="font-size:15px;color:var(--br-navy)">809-555-1234</b>
          <span class="badge ok">Alias activo</span>
          <div class="hint">Cuenta corriente ****3341</div>
        </div>
      </div>
      <div class="btn btn-outline block">Ver y compartir mi QR</div>
    </div>
  </div>
  <div class="card"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Pagos con QR recientes</h3><div class="right">Ver todos</div></div>
    <table class="table">
      <tr><th>Comercio</th><th>Fecha</th><th>Tipo de QR</th><th>Referencia</th><th style="text-align:right">Monto</th><th style="text-align:right">Estado</th></tr>
      <tr><td><b>Colmado La Esquina</b><div class="hint">RNC 1-31-***-4</div></td><td>Hoy 09:15</td><td>Estático</td><td>PI-26-0097884</td><td class="num">DOP 420.00</td><td style="text-align:right"><span class="badge ok">Completado</span></td></tr>
      <tr><td><b>Farmacia Carol · Suc. 12</b></td><td>01 sep. 19:22</td><td>Dinámico</td><td>PI-26-0096510</td><td class="num">DOP 1,875.60</td><td style="text-align:right"><span class="badge ok">Completado</span></td></tr>
      <tr><td><b>Parqueo Malecón</b></td><td>30 ago. 21:03</td><td>Dinámico</td><td>PI-26-0094122</td><td class="num">DOP 150.00</td><td style="text-align:right"><span class="badge ok">Completado</span></td></tr>
    </table>
  </div>
</div>"""
    frame("F", "F-01", "QR · hub", "entrada", body)

    # F-02 opciones de lectura
    body = f"""
<div class="stack">
  {page_head("Pagar con QR","Elige cómo quieres leer el código.",["Pago Instantáneo","QR","Pagar"])}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="tabs"><div class="tab active">{ico('camera',18)} Cámara</div><div class="tab">{ico('upload',18)} Subir imagen</div><div class="tab">{ico('copy',18)} Pegar código</div></div>
      <div class="card flat stack sm" style="align-items:center;padding:40px;text-align:center">
        <div style="width:74px;height:74px;border-radius:50%;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center">{ico('camera',36)}</div>
        <b style="font-size:16px;color:var(--br-navy)">Permite el acceso a tu cámara</b>
        <span class="hint" style="max-width:400px">Tu navegador pedirá permiso. La imagen se procesa localmente en tu equipo: Banreservas no almacena video.</span>
        <div class="btn btn-primary" style="margin-top:8px">Activar cámara</div>
      </div>
      <div class="dashed"></div>
      <div class="stack sm">
        <div class="label">Alternativas</div>
        <div class="input ro" style="height:auto;padding:16px;justify-content:center;border-style:dashed;color:var(--ink-3)">{ico('upload',20)} Arrastra aquí la imagen o el PDF del código QR</div>
        {field("O pega el contenido del código EMVCo", inp("00020101021226580014do.com.bcrd.pi...", True, "", suf="Validar"))}
      </div>
    </div>
    <div class="stack">
      {alert('info','QR interoperable','Aceptamos cualquier QR del estándar EMVCo emitido por bancos y billeteras del país, sin importar la entidad del comercio.','qr')}
      {alert('warn','Cuidado con las calcomanías falsas','En el comercio, verifica que el nombre que te mostramos coincida con el negocio. Si no coincide, no pagues.','shieldcheck')}
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('lock',20)}</div><h3>Qué validamos por ti</h3></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Firma y estructura EMVCo del código</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Que el comercio esté activo y afiliado</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Vigencia del código (los dinámicos vencen)</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Que el monto no haya sido alterado</span></div>
      </div>
    </div>
  </div>
</div>"""
    frame("F", "F-02", "QR · opciones de lectura", "1/4", body)

    # F-03 escaneando
    body = f"""
<div class="stack">
  {page_head("Escaneando código","Coloca el QR dentro del recuadro.",["Pago Instantáneo","QR","Pagar"])}
  <div class="grid-2" style="grid-template-columns:1fr 400px">
    <div class="card" style="padding:14px">
      <div class="scanner" style="height:480px">
        <div class="reticle"><i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i><div class="laser"></div></div>
        <div class="cap">Buscando código QR... mantén la cámara estable</div>
      </div>
      <div class="hstack" style="margin-top:14px"><div class="btn btn-outline sm">{ico('refresh',15)} Cambiar cámara</div><div class="btn btn-outline sm">{ico('upload',15)} Subir imagen</div><div class="spacer"></div><div class="btn btn-ghost">Cancelar</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('info',20)}</div><h3>Consejos</h3></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Evita reflejos y sombras sobre el código</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Acércate hasta que el QR llene el recuadro</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Si está impreso y dañado, pide uno nuevo al comercio</span></div>
      </div>
      {alert('info','Nada se graba','La lectura ocurre en tu navegador. No enviamos ni almacenamos imágenes de tu cámara.','lock')}
    </div>
  </div>
</div>"""
    frame("F", "F-03", "QR · escaneando con cámara", "2/4", body)

    # F-04 QR estatico
    TIPS = '<div class="hstack" style="gap:8px">' + "".join(
        '<div class="btn btn-outline sm">%s</div>' % t for t in ["Sin propina","5%","10%","15%","Otro"]) + '</div>'
    body = f"""
<div class="stack">
  {page_head("Código leído · ingresa el monto","Este comercio usa un QR estático: tú digitas cuánto pagar.",["Pago Instantáneo","QR","Pagar"])}
  {stepper(["Leer QR","Monto","Revisión","Autenticación"],1)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="rowitem" style="background:#F6FCF8;border-color:#BFE6CF">
        <div class="ic" style="background:var(--ok-bg);color:var(--ok)">{ico('store',22)}</div>
        <div class="tx"><b style="font-size:17px">COLMADO LA ESQUINA SRL</b><span>RNC 1-31-***-4 · Santo Domingo Este · Banco Y</span></div>
        <span class="badge ok" style="margin-left:auto">{ico('check',13,3)} Comercio verificado</span>
      </div>
      {field("Monto a pagar", inp("420.00","", "big focus", pre="DOP"))}
      {field("Propina <span class='opt'>(opcional)</span>", TIPS)}
      <div class="stack sm"><div class="label">Cuenta de origen</div>{acct_row("Cuenta corriente","No. ****3341","DOP 2,383.33",sel=True,icon="refresh")}</div>
      {field("Concepto <span class='opt'>(opcional)</span>", inp("Compra en colmado", ""))}
      <div class="hstack"><div class="btn btn-outline">{ico('back',18)} Escanear otro</div><div class="spacer"></div><div class="btn btn-primary">Continuar {ico('arrow',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('qr',20)}</div><h3>Datos del código</h3></div>
        {kv([("Tipo","Estático (sin monto)"),("Estándar","EMVCo QR · MPM"),("Alias del comercio","@colmadolaesquina"),("Categoría (MCC)","5411 · Colmados y supermercados"),("Firma del código","Válida"),("Emitido por","Banco Y · 12 mar. 2026")])}
      </div>
      {alert('warn','Verifica el nombre del comercio','Debe coincidir con el negocio donde estás. Si no, detente y avisa al establecimiento.','shieldcheck')}
    </div>
  </div>
</div>"""
    frame("F", "F-04", "QR · estático (digitar monto)", "3/4", body)

    # F-05 QR dinamico
    body = f"""
<div class="stack">
  {page_head("Confirma tu pago","Este código ya trae el monto de la factura.",["Pago Instantáneo","QR","Pagar"])}
  {stepper(["Leer QR","Monto","Revisión","Autenticación"],2)}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="rowitem" style="background:#F6FCF8;border-color:#BFE6CF">
        <div class="ic" style="background:var(--ok-bg);color:var(--ok)">{ico('store',22)}</div>
        <div class="tx"><b style="font-size:17px">FARMACIA CAROL · SUCURSAL 12</b><span>RNC 1-01-***-9 · Caja 3 · Banco Z</span></div>
        <span class="badge ok" style="margin-left:auto">{ico('check',13,3)} Verificado</span>
      </div>
      <div style="text-align:center;padding:8px 0">
        <div class="hint">Total de la factura</div>
        <div class="amount lg">DOP 1,875<small>.60</small></div>
        <span class="badge warn" style="margin-top:8px">{ico('clock',13,2.4)} El código vence en 04:12</span>
      </div>
      <div class="dashed"></div>
      {kv([("Factura","B0100004521"),("Detalle","3 artículos"),("Subtotal","DOP 1,589.49"),("ITBIS 18%","DOP 286.11"),
           ("Monto (no editable)","<span style='font-size:17px'>DOP 1,875.60</span>"),("Cuenta de origen","Cuenta corriente ****3341"),("Comisión","DOP 0.00")])}
      {alert('info','El monto viene firmado en el código','No puede alterarse. Si el total no coincide con tu factura, pide al cajero que genere un código nuevo.','lock')}
      <div class="hstack"><div class="btn btn-outline">Cancelar</div><div class="spacer"></div><div class="btn btn-primary lg">Autorizar pago {ico('lock',18)}</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm" style="align-items:center"><div class="card-head" style="width:100%"><div class="ico">{ico('qr',20)}</div><h3>Código leído</h3></div>
        <div class="qr-box" style="padding:12px">{qr(160,33)}</div>
        <span class="badge info">QR dinámico · un solo uso</span>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('sliders',20)}</div><h3>Límite de compras QR</h3></div>
        <div class="limit-bar"><div class="lt"><span>Diario en comercios</span><b>DOP 2,295 de 30,000</b></div><div class="progress"><i style="width:8%"></i></div></div>
      </div>
    </div>
  </div>
</div>"""
    frame("F", "F-05", "QR · dinámico con monto y vencimiento", "3/4", body)

    # F-06 auth QR
    modal = f"""<div class="scrim"><div class="modal">
  <div class="modal-head"><div class="ico" style="width:34px;height:34px;border-radius:10px;background:var(--br-orange-050);color:var(--br-orange);display:flex;align-items:center;justify-content:center">{ico('lock',20)}</div><h3>Autoriza el pago del QR</h3><div class="x">{ico('x',20)}</div></div>
  <div class="modal-body stack">
    <div class="card flat stack sm" style="text-align:center;background:#F8FAFC">
      <div class="hint">Pagarás a</div><b style="font-size:17px;color:var(--br-navy)">FARMACIA CAROL · SUCURSAL 12</b>
      <div class="amount" style="font-size:34px">DOP 1,875.60</div>
    </div>
    <div class="hstack" style="gap:12px;justify-content:center">
      <div style="width:64px;height:64px;border-radius:50%;background:var(--br-cyan-050);color:var(--br-blue);display:flex;align-items:center;justify-content:center">{ico('fingerprint',32)}</div>
      <div><b style="font-size:15px;color:var(--br-navy)">Aprobación enviada a tu App TuBanco</b><div class="hint">Confirma con huella o Face ID · expira en 01:44</div></div>
    </div>
    <div class="dashed"></div>
    <div class="hint" style="text-align:center">¿No te llegó la notificación? <b style="color:var(--br-blue-600)">Usar código por SMS</b> o <b style="color:var(--br-blue-600)">token blando</b></div>
    {alert('warn','El código QR vence en 03:58','Si expira, pide al comercio que genere uno nuevo; no se debitará nada.','clock')}
  </div>
  <div class="modal-foot"><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary">Esperando aprobación...</div></div>
</div></div>"""
    body = f"""<div class="stack">{page_head("Confirma tu pago","",["Pago Instantáneo","QR","Pagar"])}{stepper(["Leer QR","Monto","Revisión","Autenticación"],3)}<div style="height:440px"></div></div>"""
    frame("F", "F-06", "QR · autenticación", "4/4 · modal", body)

    # F-07 comprobante QR
    body = f"""
<div class="stack">
  {page_head("Pago con QR completado","",["Pago Instantáneo","QR","Comprobante"],
   f'<div class="btn btn-outline sm">{ico("download",16)} PDF</div><div class="btn btn-primary sm">{ico("share",16)} Compartir</div>')}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="receipt">
      <div class="rh"><div class="ic">{ico('check',36,3)}</div>
        <b style="font-size:20px;color:#0B6438">¡Pago realizado!</b>
        <div class="amount ok" style="font-size:38px">DOP 1,875<small>.60</small></div>
        <span class="hint" style="color:#0B6438">02 de sep. de 2026, 15:31:08 · acreditado en 4 segundos</span>
      </div>
      <div class="notch"></div>
      <div class="rb">
        {kv([("Comercio","FARMACIA CAROL · SUCURSAL 12"),("RNC","1-01-***-9"),("Sucursal / caja","Sucursal 12 · Caja 3"),
             ("Factura","B0100004521"),("Tipo de pago","QR dinámico EMVCo"),
             ("Cuenta de origen","Cuenta corriente ****3341"),
             ("Subtotal","DOP 1,589.49"),("ITBIS 18%","DOP 286.11"),("Comisión","DOP 0.00"),
             ("Total debitado","<span style='font-size:17px'>DOP 1,875.60</span>"),
             ("Referencia Banreservas","<span style='font-family:monospace'>PI-26-0098344</span>"),
             ("Autorización del comercio","<span style='font-family:monospace'>A-77120945</span>")])}
        <div class="dashed" style="margin:16px -26px"></div>
        <div class="hstack" style="gap:10px;flex-wrap:wrap">
          <div class="btn btn-outline sm">{ico('doc',15)} Ver factura adjunta</div>
          <div class="btn btn-outline sm">{ico('star',15)} Guardar comercio</div>
          <div class="btn btn-outline sm">{ico('alert',15)} Reportar problema</div>
        </div>
      </div>
    </div>
    <div class="stack">
      {alert('ok','Muestra esta pantalla al cajero','El comercio también recibió la confirmación en su terminal.','check')}
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('money',20)}</div><h3>Tu cuenta</h3></div>
        <div class="kv"><div class="k">Balance anterior</div><div class="v">DOP 4,258.93</div></div>
        <div class="kv"><div class="k">Este pago</div><div class="v" style="color:var(--err)">- DOP 1,875.60</div></div>
        <div class="kv"><div class="k">Balance disponible</div><div class="v" style="font-size:16px">DOP 2,383.33</div></div>
      </div>
      <div class="hstack"><div class="btn btn-outline block">Ir al inicio</div><div class="btn btn-primary block">Escanear otro QR</div></div>
    </div>
  </div>
</div>"""
    frame("F", "F-07", "QR · comprobante", "resultado", body)

    # F-08 Mi QR
    body = f"""
<div class="stack">
  {page_head("Mi QR para cobrar","Compártelo y recibe pagos de cualquier banco al instante.",["Pago Instantáneo","QR","Mi QR"])}
  <div class="grid-2" style="grid-template-columns:520px 1fr">
    <div class="card stack sm" style="align-items:center">
      <div class="tabs" style="width:100%"><div class="tab active">Sin monto</div><div class="tab">Con monto fijo</div></div>
      <div style="background:linear-gradient(160deg,#00396B,#0A6FB7);border-radius:20px;padding:24px;width:100%;display:flex;flex-direction:column;align-items:center;gap:14px;color:#fff">
        <div class="hstack" style="gap:10px">{LOGO}<b style="letter-spacing:.6px">BANRESERVAS</b></div>
        <div class="qr-box" style="padding:14px">{qr(220,21)}</div>
        <div style="text-align:center"><b style="font-size:18px">E***** A***** F***** S.</b>
        <div style="font-size:13px;color:#BBD9F1">@edwardf · 809-555-1234</div></div>
        <span class="badge orange">Pago Instantáneo RD</span>
      </div>
      <div class="hstack" style="gap:8px;flex-wrap:wrap;justify-content:center;margin-top:6px">
        <div class="btn btn-outline sm">{ico('download',15)} PNG</div>
        <div class="btn btn-outline sm">{ico('download',15)} PDF</div>
        <div class="btn btn-outline sm">{ico('print',15)} Imprimir</div>
        <div class="btn btn-primary sm">{ico('share',15)} Compartir</div>
      </div>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('sliders',20)}</div><h3>Configura tu código</h3></div>
        {field("Alias que recibirá los pagos", f'<div class="input"><span>809-555-1234 · Cuenta corriente ****3341</span><span class="suf">{ico("chev",16)}</span></div>')}
        <div class="grid-2">
          {field("Monto fijo <span class='opt'>(opcional)</span>", inp("Sin monto: el pagador lo digita", True, pre="DOP"))}
          {field("Concepto <span class='opt'>(opcional)</span>", inp("Ej. Venta de repostería", True))}
        </div>
        <div class="hstack"><div class="switch on"><i></i></div><span class="hint">Mostrar mi nombre enmascarado en el código</span></div>
        <div class="hstack"><div class="switch"><i></i></div><span class="hint">Código de un solo uso (se invalida tras el primer pago)</span></div>
        <div class="hstack"><div class="switch"><i></i></div><span class="hint">Vencimiento a los 15 minutos (QR dinámico)</span></div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Cobros recibidos por QR</h3><div class="right">Ver todos</div></div>
        <div class="rowitem" style="padding:12px"><div class="ic">{ico('arrowdown',20)}</div><div class="tx"><b>J*** R*****</b><span>Hoy 11:04 · PI-26-0098120</span></div><div class="rt"><b style="color:var(--ok)">+ DOP 750.00</b><span>Acreditado</span></div></div>
        <div class="rowitem" style="padding:12px"><div class="ic">{ico('arrowdown',20)}</div><div class="tx"><b>A**** T*****</b><span>Ayer 20:41 · PI-26-0097322</span></div><div class="rt"><b style="color:var(--ok)">+ DOP 1,200.00</b><span>Acreditado</span></div></div>
      </div>
      {alert('info','Tu QR no expone tus datos','Contiene solo tu alias y tu entidad. Nadie puede debitar tu cuenta con él: solo depositar.','shieldcheck')}
    </div>
  </div>
</div>"""
    frame("F", "F-08", "QR · mi código de cobro", "recibir", body)

    # F-09 errores QR
    def errbox(icon, title, text, actions, badge, color):
        return f"""<div class="card stack sm">
      <div class="hstack" style="gap:14px"><div style="width:52px;height:52px;border-radius:50%;background:{color[1]};color:{color[0]};display:flex;align-items:center;justify-content:center;flex:none">{ico(icon,26)}</div>
      <div><b style="font-size:16px;color:var(--br-navy)">{title}</b><div class="hint" style="margin-top:3px;line-height:1.6">{text}</div></div>
      <span class="badge {badge[1]}" style="margin-left:auto">{badge[0]}</span></div>
      <div class="hstack" style="gap:10px;flex-wrap:wrap">{actions}</div></div>"""
    body = f"""
<div class="stack">
  {page_head("QR · estados de error","",["Pago Instantáneo","QR","Estados"])}
  <div class="grid-2">
    {errbox('clock','El código QR venció','Los códigos dinámicos son válidos por 5 minutos. Pide al comercio que genere uno nuevo. No se debitó ningún valor.',f'<div class="btn btn-primary sm">Escanear de nuevo</div>',('Vencido','warn'),('var(--warn)','var(--warn-bg)'))}
    {errbox('x','Código no reconocido','La imagen no corresponde a un QR de pagos del estándar EMVCo. Verifica que sea un código de cobro y no un enlace o promoción.',f'<div class="btn btn-outline sm">Subir otra imagen</div><div class="btn btn-outline sm">Pegar el código</div>',('Inválido','err'),('var(--err)','var(--err-bg)'))}
    {errbox('store','Comercio no habilitado','El negocio aparece inactivo o suspendido en el sistema de pagos. No es posible completar el pago con este código.',f'<div class="btn btn-outline sm">Pagar con alias</div><div class="btn btn-outline sm">Reportar comercio</div>',('Bloqueado','err'),('var(--err)','var(--err-bg)'))}
    {errbox('alert','Código posiblemente manipulado','La firma del QR no coincide con el comercio que declara. Podría ser una calcomanía falsa sobrepuesta. <b>No pagues</b> y avisa al establecimiento.',f'<div class="btn btn-danger sm">{ico("alert",15)} Reportar fraude</div><div class="btn btn-outline sm">Cancelar</div>',('Riesgo alto','err'),('var(--err)','var(--err-bg)'))}
    {errbox('camera','Sin acceso a la cámara','Tu navegador bloqueó el permiso. Habilítalo en la configuración del sitio o usa otra opción de lectura.',f'<div class="btn btn-outline sm">Cómo habilitarlo</div><div class="btn btn-primary sm">Subir imagen</div>',('Permiso denegado','neutral'),('var(--ink-3)','#EDF1F6'))}
    {errbox('sliders','Supera tu límite de compras','El monto del QR (DOP 32,400.00) excede tu límite diario para comercios (DOP 30,000.00).',f'<div class="btn btn-outline sm">Ajustar límites</div><div class="btn btn-outline sm">Pagar con otro medio</div>',('Bloqueado','warn'),('var(--warn)','var(--warn-bg)'))}
  </div>
</div>"""
    frame("F", "F-09", "QR · errores", "estados negativos", body)

# ================================================ G. SEGURIDAD Y POST-VENTA
def g_seguridad():
    # G-01 panel
    body = f"""
<div class="stack">
  {page_head("Seguridad de tus pagos instantáneos","Controla límites, dispositivos y formas de autorizar.",["Administrar","Seguridad"])}
  <div class="grid-4">
    <div class="card stack sm"><div class="hstack">{ico('sliders',22)}<b style="font-size:15px;color:var(--br-navy)">Límites</b></div><div class="hint">Diario DOP 50,000 · por transacción DOP 25,000</div><div class="btn btn-outline sm block">Configurar</div></div>
    <div class="card stack sm"><div class="hstack">{ico('device',22)}<b style="font-size:15px;color:var(--br-navy)">Dispositivos</b></div><div class="hint">3 dispositivos de confianza activos</div><div class="btn btn-outline sm block">Administrar</div></div>
    <div class="card stack sm"><div class="hstack">{ico('key',22)}<b style="font-size:15px;color:var(--br-navy)">Autenticación</b></div><div class="hint">Push + token blando habilitados</div><div class="btn btn-outline sm block">Configurar</div></div>
    <div class="card stack sm"><div class="hstack">{ico('bell',22)}<b style="font-size:15px;color:var(--br-navy)">Alertas</b></div><div class="hint">Push, correo y SMS activos</div><div class="btn btn-outline sm block">Configurar</div></div>
  </div>
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack sm"><div class="card-head"><div class="ico">{ico('shieldcheck',20)}</div><h3>Estado de tu seguridad</h3><div class="right">Nivel: alto</div></div>
      <div class="limit-bar"><div class="lt"><span>Protección de la cuenta</span><b>85 / 100</b></div><div class="progress"><i style="width:85%;background:var(--ok)"></i></div></div>
      <div class="rowitem"><div class="ic" style="background:var(--ok-bg);color:var(--ok)">{ico('check',20,3)}</div><div class="tx"><b>Doble factor activo</b><span>Aprobación push con biometría</span></div><span class="badge ok" style="margin-left:auto">Listo</span></div>
      <div class="rowitem"><div class="ic" style="background:var(--ok-bg);color:var(--ok)">{ico('check',20,3)}</div><div class="tx"><b>Sello anti-phishing configurado</b><span>"Palmera azul"</span></div><span class="badge ok" style="margin-left:auto">Listo</span></div>
      <div class="rowitem"><div class="ic" style="background:var(--ok-bg);color:var(--ok)">{ico('check',20,3)}</div><div class="tx"><b>Alertas de transacción</b><span>Push + correo en cada pago</span></div><span class="badge ok" style="margin-left:auto">Listo</span></div>
      <div class="rowitem"><div class="ic" style="background:var(--warn-bg);color:var(--warn)">{ico('alert',20)}</div><div class="tx"><b>Límites por encima de tu uso habitual</b><span>Usas en promedio DOP 6,400 al día</span></div><div class="btn btn-outline sm" style="margin-left:auto">Reducir</div></div>
      <div class="rowitem"><div class="ic" style="background:var(--warn-bg);color:var(--warn)">{ico('alert',20)}</div><div class="tx"><b>Contraseña con más de 6 meses</b><span>Último cambio: 22 feb. 2026</span></div><div class="btn btn-outline sm" style="margin-left:auto">Cambiar</div></div>
    </div>
    <div class="stack">
      <div class="card stack sm" style="border:2px solid var(--err)"><div class="card-head"><div class="ico" style="background:var(--err-bg);color:var(--err)">{ico('lock',20)}</div><h3>Modo seguro</h3></div>
        <div class="hint">Bloquea de inmediato todos los pagos instantáneos salientes. Podrás seguir recibiendo dinero. Se desactiva desde la App con biometría.</div>
        <div class="btn btn-danger block">{ico('lock',16)} Bloquear mis pagos</div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Actividad de seguridad</h3></div>
        <div class="kv"><div class="k">Hoy 15:12</div><div class="v">Pago autorizado con push</div></div>
        <div class="kv"><div class="k">Hoy 14:58</div><div class="v">Alias registrado (OTP)</div></div>
        <div class="kv"><div class="k">01 sep. 22:10</div><div class="v" style="color:var(--err)">Intento de OTP fallido (3)</div></div>
        <div class="kv"><div class="k">30 ago. 08:12</div><div class="v">Nuevo dispositivo autorizado</div></div>
      </div>
    </div>
  </div>
</div>"""
    frame("G", "G-01", "Seguridad · panel", "administrar", body, nav="Administrar")

    # G-02 limites
    body = f"""
<div class="stack">
  {page_head("Límites de pagos instantáneos","Define cuánto puedes enviar. Un límite bajo es tu mejor defensa ante un fraude.",["Administrar","Seguridad","Límites"])}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack">
      <div class="stack sm">
        <div class="hstack"><b style="font-size:15px;color:var(--br-navy)">Por transacción</b><span class="spacer"></span><b style="font-size:15px;color:var(--br-navy)">DOP 25,000</b></div>
        <div class="progress"><i style="width:50%"></i></div>
        <div class="hstack"><span class="hint">DOP 1,000</span><span class="spacer"></span><span class="hint">Máximo permitido: DOP 50,000</span></div>
      </div>
      <div class="stack sm">
        <div class="hstack"><b style="font-size:15px;color:var(--br-navy)">Diario</b><span class="spacer"></span><b style="font-size:15px;color:var(--br-navy)">DOP 50,000</b></div>
        <div class="progress"><i style="width:33%"></i></div>
        <div class="hstack"><span class="hint">DOP 5,000</span><span class="spacer"></span><span class="hint">Máximo permitido: DOP 150,000</span></div>
      </div>
      <div class="stack sm">
        <div class="hstack"><b style="font-size:15px;color:var(--br-navy)">Mensual</b><span class="spacer"></span><b style="font-size:15px;color:var(--br-navy)">DOP 400,000</b></div>
        <div class="progress"><i style="width:40%"></i></div>
      </div>
      <div class="dashed"></div>
      <div class="stack sm">
        <div class="label">Reglas adicionales</div>
        <div class="rowitem"><div class="switch on"><i></i></div><div class="tx" style="margin-left:6px"><b>Tope para beneficiarios nuevos</b><span>DOP 10,000 durante las primeras 24 horas</span></div></div>
        <div class="rowitem"><div class="switch on"><i></i></div><div class="tx" style="margin-left:6px"><b>Pedir aprobación en la App sobre DOP 15,000</b><span>Incluso si ya usaste otro factor</span></div></div>
        <div class="rowitem"><div class="switch"><i></i></div><div class="tx" style="margin-left:6px"><b>Bloquear pagos entre 12:00 a.m. y 5:00 a.m.</b><span>Franja de mayor incidencia de fraude</span></div></div>
        <div class="rowitem"><div class="switch on"><i></i></div><div class="tx" style="margin-left:6px"><b>Permitir solo alias en mis frecuentes</b><span>Los demás requerirán verificación adicional</span></div></div>
      </div>
      <div class="hstack"><div class="btn btn-ghost">Cancelar</div><div class="spacer"></div><div class="btn btn-primary">Guardar cambios</div></div>
    </div>
    <div class="stack">
      {alert('warn','Los aumentos tardan 24 horas','Reducir un límite aplica de inmediato; aumentarlo entra en vigor 24 h después y requiere aprobación en la App. Así, un delincuente con tu sesión no puede subirlos y vaciar tu cuenta.','clock')}
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('info',20)}</div><h3>Tu uso real</h3></div>
        <div class="kv"><div class="k">Promedio diario</div><div class="v">DOP 6,400</div></div>
        <div class="kv"><div class="k">Pago más alto (90 días)</div><div class="v">DOP 18,200</div></div>
        <div class="kv"><div class="k">Sugerencia</div><div class="v" style="color:var(--ok)">Diario DOP 25,000</div></div>
        <div class="btn btn-outline sm block">Aplicar sugerencia</div>
      </div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('clock',20)}</div><h3>Cambio programado</h3></div>
        <div class="rowitem"><div class="ic" style="background:var(--warn-bg);color:var(--warn)">{ico('arrowup',20)}</div><div class="tx"><b>Diario: 50,000 → 80,000</b><span>Se activa el 03 sep. a las 15:40</span></div></div>
        <div class="btn btn-danger sm block">Cancelar el aumento</div>
      </div>
    </div>
  </div>
</div>"""
    frame("G", "G-02", "Seguridad · límites", "control", body, nav="Administrar")

    # G-03 dispositivos
    def dev(icon, name, det, badge, cur=False):
        return f"""<div class="rowitem {'sel' if cur else ''}"><div class="ic">{ico(icon,22)}</div>
        <div class="tx"><b>{name}</b><span>{det}</span></div>
        <div style="margin-left:auto" class="hstack">{badge}<div class="btn btn-outline sm">{'Cerrar sesión' if cur else 'Revocar'}</div></div></div>"""
    body = f"""
<div class="stack">
  {page_head("Dispositivos y sesiones","Revisa desde dónde se accede a tu banca. Revoca lo que no reconozcas.",["Administrar","Seguridad","Dispositivos"])}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack sm">
      <div class="card-head"><div class="ico">{ico('device',20)}</div><h3>Dispositivos de confianza</h3><div class="right">3 activos · máx. 5</div></div>
      {dev('device','Chrome · Windows 11','Santo Domingo, RD · IP 126.1.28.49 · sesión activa ahora','<span class="badge ok">Este dispositivo</span>',True)}
      {dev('phone','iPhone 15 · App TuBanco','Santo Domingo, RD · último uso hoy 15:12 · biometría activa','<span class="badge ok">Confiable</span>')}
      {dev('device','Safari · macOS','Santiago, RD · último uso 28 ago. 2026','<span class="badge neutral">Sin uso 5 días</span>')}
      {dev('device','Chrome · Android','Miami, EE. UU. · 01 sep. 22:08 · 3 intentos de OTP fallidos','<span class="badge err">{}</span>'.format('No reconocido'))}
      <div class="hstack" style="margin-top:8px"><div class="btn btn-danger">{ico('lock',16)} Cerrar todas las sesiones</div><div class="spacer"></div><div class="hint">Se te pedirá iniciar sesión de nuevo en todos los dispositivos.</div></div>
    </div>
    <div class="stack">
      {alert('err','Actividad sospechosa detectada','Un dispositivo desde Miami intentó autorizar un pago el 01 de sep. a las 22:08. Lo bloqueamos automáticamente. Si no fuiste tú, cambia tu contraseña.','alert')}
      <div class="hstack" style="gap:10px"><div class="btn btn-primary block">Cambiar contraseña</div></div>
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('shield',20)}</div><h3>Cómo protegemos tu sesión</h3></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Huella del dispositivo y detección de sesión duplicada</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Cierre automático tras 5 minutos de inactividad</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Bloqueo tras 3 intentos fallidos de autenticación</span></div>
        <div class="hstack" style="gap:10px">{ico('check',16,3)}<span class="hint">Alerta inmediata al vincular un dispositivo nuevo</span></div>
      </div>
    </div>
  </div>
</div>"""
    frame("G", "G-03", "Seguridad · dispositivos y sesiones", "control", body, nav="Administrar")

    # G-04 metodos auth + antiphishing
    body = f"""
<div class="stack">
  {page_head("Formas de autorizar tus pagos","",["Administrar","Seguridad","Autenticación"])}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack sm">
      <div class="rowitem sel"><div class="ic">{ico('bell',22)}</div><div class="tx"><b>Aprobación push en la App TuBanco</b><span>Con huella o Face ID · método principal</span></div><div style="margin-left:auto" class="hstack"><span class="badge ok">Activo</span><div class="switch on"><i></i></div></div></div>
      <div class="rowitem"><div class="ic">{ico('key',22)}</div><div class="tx"><b>Token blando</b><span>Código de 6 dígitos que cambia cada 30 s</span></div><div style="margin-left:auto" class="hstack"><span class="badge ok">Activo</span><div class="switch on"><i></i></div></div></div>
      <div class="rowitem"><div class="ic">{ico('phone',22)}</div><div class="tx"><b>Código por SMS</b><span>Solo como respaldo · más vulnerable a suplantación de SIM</span></div><div style="margin-left:auto" class="hstack"><span class="badge warn">Respaldo</span><div class="switch on"><i></i></div></div></div>
      <div class="rowitem"><div class="ic">{ico('mail',22)}</div><div class="tx"><b>Código por correo</b><span>edw****@correo.com</span></div><div style="margin-left:auto" class="hstack"><span class="badge neutral">Inactivo</span><div class="switch"><i></i></div></div></div>
      <div class="rowitem"><div class="ic">{ico('fingerprint',22)}</div><div class="tx"><b>Biometría en el navegador (WebAuthn / passkey)</b><span>Huella o rostro de tu equipo, sin códigos</span></div><div style="margin-left:auto" class="hstack"><span class="badge orange">Nuevo</span><div class="btn btn-outline sm">Activar</div></div></div>
      <div class="dashed" style="margin:8px 0"></div>
      <div class="stack sm">
        <div class="label">Sello anti-phishing</div>
        <div class="rowitem"><div class="ic">{ico('shieldcheck',22)}</div><div class="tx"><b>"Palmera azul"</b><span>Aparece en todos nuestros correos y SMS. Si falta, es fraude.</span></div><div class="btn btn-outline sm" style="margin-left:auto">Cambiar</div></div>
      </div>
    </div>
    <div class="stack">
      {alert('info','¿Por qué el push es más seguro?','Vive en un dispositivo vinculado a ti y exige tu biometría. Un código por SMS puede ser interceptado con un cambio fraudulento de SIM.','shieldcheck')}
      <div class="card stack sm" style="background:var(--br-navy);color:#fff">
        <div class="hstack">{ico('alert',20)}<b style="font-size:15px">Banreservas nunca te pedirá</b></div>
        <div style="font-size:13px;line-height:1.9;color:#C9DCEC">
          <div class="hstack" style="gap:10px">{ico('x',16,3)}<span>Tu contraseña o PIN</span></div>
          <div class="hstack" style="gap:10px">{ico('x',16,3)}<span>Códigos OTP o de token</span></div>
          <div class="hstack" style="gap:10px">{ico('x',16,3)}<span>Que instales apps de acceso remoto</span></div>
          <div class="hstack" style="gap:10px">{ico('x',16,3)}<span>Que hagas un pago "de prueba" para validar algo</span></div>
        </div>
        <div class="btn btn-outline-orange sm block" style="margin-top:8px">Reportar un intento de fraude</div>
      </div>
    </div>
  </div>
</div>"""
    frame("G", "G-04", "Seguridad · métodos de autenticación", "control", body, nav="Administrar")

    # G-05 alertas + G-06 alias reportados combinados en dos frames
    body = f"""
<div class="stack">
  {page_head("Alertas y notificaciones","Entérate al instante de cada movimiento.",["Administrar","Seguridad","Alertas"])}
  <div class="grid-2" style="grid-template-columns:1fr 420px">
    <div class="card stack sm">
      <table class="table">
        <tr><th>Evento</th><th style="text-align:center">Push</th><th style="text-align:center">Correo</th><th style="text-align:center">SMS</th></tr>
        {"".join(f'<tr><td><b>{e}</b><div class="hint">{d}</div></td>'
                 f'<td style="text-align:center"><div class="switch {"on" if p else ""}" style="margin:0 auto"><i></i></div></td>'
                 f'<td style="text-align:center"><div class="switch {"on" if c else ""}" style="margin:0 auto"><i></i></div></td>'
                 f'<td style="text-align:center"><div class="switch {"on" if s else ""}" style="margin:0 auto"><i></i></div></td></tr>'
          for e,d,p,c,s in [
            ("Pago enviado","Cada vez que autorizas un envío",1,1,0),
            ("Pago recibido","Cuando alguien te paga a un alias",1,1,0),
            ("Pago sobre DOP 5,000","Montos altos, en todos los canales",1,1,1),
            ("Solicitud de pago recibida","Alguien te pide dinero",1,0,0),
            ("Alias registrado o modificado","Cambios en tus llaves de cobro",1,1,1),
            ("Cambio de límites","Aumentos o reducciones",1,1,1),
            ("Nuevo dispositivo","Acceso desde un equipo no reconocido",1,1,1),
            ("Intento de autenticación fallido","3 o más fallos seguidos",1,1,0)])}
      </table>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('bell',20)}</div><h3>Vista previa</h3></div>
        <div class="toast" style="width:100%"><div style="color:#7BE0A8">{ico('check',20,3)}</div><div><b>Pago enviado · DOP 2,500.00</b><span>A @mariaperez · hoy 15:12 · ref. PI-26-0098231. ¿No fuiste tú? Toca aquí.</span></div></div>
        <div class="toast" style="width:100%"><div style="color:#FFC48A">{ico('alert',20)}</div><div><b>Nuevo dispositivo detectado</b><span>Chrome · Android desde Miami, EE. UU. Si no fuiste tú, bloquea tu cuenta.</span></div></div>
      </div>
      {alert('warn','No desactives las alertas de seguridad','Las alertas de dispositivo, límites y alias son tu primera señal de que algo va mal.')}
    </div>
  </div>
</div>"""
    frame("G", "G-05", "Seguridad · alertas y notificaciones", "control", body, nav="Administrar")

    body = f"""
<div class="stack">
  {page_head("Alias bloqueados y reportes","Controla quién puede cobrarte y reporta alias fraudulentos.",["Administrar","Seguridad","Alias"])}
  <div class="grid-2" style="grid-template-columns:1fr 460px">
    <div class="card stack sm">
      <div class="card-head"><div class="ico">{ico('lock',20)}</div><h3>Alias bloqueados</h3><div class="right">No pueden solicitarte pagos</div></div>
      <div class="rowitem"><div class="ic" style="background:var(--err-bg);color:var(--err)">{ico('store',22)}</div><div class="tx"><b>@servicios.expressrd</b><span>Bloqueado el 01 sep. 2026 · reportado como fraude</span></div><div class="btn btn-outline sm" style="margin-left:auto">Desbloquear</div></div>
      <div class="rowitem"><div class="ic" style="background:var(--err-bg);color:var(--err)">{ico('at',22)}</div><div class="tx"><b>@premios.rd</b><span>Bloqueado el 18 ago. 2026 · solicitudes no deseadas</span></div><div class="btn btn-outline sm" style="margin-left:auto">Desbloquear</div></div>
      <div class="dashed" style="margin:8px 0"></div>
      <div class="card-head"><div class="ico">{ico('alert',20)}</div><h3>Mis reportes</h3></div>
      <table class="table">
        <tr><th>Alias</th><th>Motivo</th><th>Fecha</th><th style="text-align:right">Estado</th></tr>
        <tr><td><b>@servicios.expressrd</b></td><td>Estafa / suplantación</td><td>01 sep. 2026</td><td style="text-align:right"><span class="badge warn">En análisis</span></td></tr>
        <tr><td><b>@premios.rd</b></td><td>Cobro no solicitado</td><td>18 ago. 2026</td><td style="text-align:right"><span class="badge ok">Confirmado</span></td></tr>
      </table>
    </div>
    <div class="stack">
      <div class="card stack sm"><div class="card-head"><div class="ico">{ico('alert',20)}</div><h3>Reportar un alias</h3></div>
        {field("Alias a reportar", inp("@ejemplo.sospechoso", True, icon="at"))}
        {field("Motivo", f'<div class="input"><span>Selecciona un motivo</span><span class="suf">{ico("chev",16)}</span></div>')}
        {field("Describe lo ocurrido", f'<div class="input" style="height:96px;align-items:flex-start;padding-top:12px"><span class="ph">Cuéntanos qué pasó. No incluyas claves ni códigos.</span></div>')}
        <div class="hstack" style="align-items:flex-start;gap:10px"><div class="check on">{ico('check',14,3)}</div><span style="font-size:13px;color:var(--ink-2)">Bloquear este alias para que no pueda solicitarme pagos</span></div>
        <div class="btn btn-primary block">Enviar reporte</div>
      </div>
      {alert('info','Tus reportes protegen a otros','Se comparten de forma anónima con el motor antifraude del sistema nacional. Un alias con múltiples reportes muestra advertencia a todos los usuarios.','shieldcheck')}
    </div>
  </div>
</div>"""
    frame("G", "G-06", "Seguridad · alias bloqueados y reportes", "antifraude", body, nav="Administrar")

    # G-07 movimientos
    def mrow(fecha, det, sub, ref, monto, signo, badge):
        color = "var(--ok)" if signo == "+" else "var(--err)"
        return (f'<tr><td>{fecha}</td><td><b>{det}</b><div class="hint">{sub}</div></td><td style="font-family:monospace;font-size:12.5px">{ref}</td>'
                f'<td class="num" style="color:{color}">{signo} DOP {monto}</td><td style="text-align:right">{badge}</td><td style="text-align:right;color:var(--ink-3)">{ico("chevr",18)}</td></tr>')
    body = f"""
<div class="stack">
  {page_head("Movimientos de pagos instantáneos","",["Pago Instantáneo","Movimientos"],
   f'<div class="btn btn-outline sm">{ico("download",16)} Exportar</div><div class="btn btn-outline sm">{ico("filter",16)} Filtros</div>')}
  <div class="card">
    <div class="grid-4" style="align-items:end">
      {field("Desde", inp("01/08/2026","",icon="calendar"))}
      {field("Hasta", inp("02/09/2026","",icon="calendar"))}
      {field("Tipo", f'<div class="input"><span>Todos</span><span class="suf">{ico("chev",16)}</span></div>')}
      {field("Estado", f'<div class="input"><span>Todos</span><span class="suf">{ico("chev",16)}</span></div>')}
    </div>
    <div class="hstack" style="margin-top:14px;gap:8px;flex-wrap:wrap">
      <span class="badge info">Enviados (14)</span><span class="badge ok">Recibidos (23)</span><span class="badge orange">QR (9)</span>
      <span class="badge warn">Pendientes (2)</span><span class="badge neutral">Devoluciones (1)</span>
      <div class="spacer"></div><div class="btn btn-outline sm">Limpiar</div><div class="btn btn-blue sm">Aplicar</div>
    </div>
  </div>
  <div class="card">
    <table class="table">
      <tr><th>Fecha</th><th>Detalle</th><th>Referencia</th><th style="text-align:right">Monto</th><th style="text-align:right">Estado</th><th></th></tr>
      {mrow("02 sep. 15:31","FARMACIA CAROL · SUC. 12","Pago con QR dinámico · factura B0100004521","PI-26-0098344","1,875.60","-",'<span class="badge ok">Completado</span>')}
      {mrow("02 sep. 15:12","M**** P***** G*****","Enviado a @mariaperez · Banco Popular","PI-26-0098231","2,500.00","-",'<span class="badge ok">Completado</span>')}
      {mrow("02 sep. 11:04","J*** R***** M*****","Recibido por QR de cobro","PI-26-0098120","750.00","+",'<span class="badge ok">Acreditado</span>')}
      {mrow("02 sep. 09:15","COLMADO LA ESQUINA","Pago con QR estático","PI-26-0097884","420.00","-",'<span class="badge ok">Completado</span>')}
      {mrow("01 sep. 18:40","J*** R***** M*****","Recibido de 809-***-4471","PI-26-0097102","6,800.00","+",'<span class="badge ok">Acreditado</span>')}
      {mrow("01 sep. 16:22","P**** T***** V*****","Enviado a @pedrot · Banco Y","PI-26-0096998","3,200.00","-",'<span class="badge warn">En verificación</span>')}
      {mrow("31 ago. 20:11","SERVI RD SRL","Devolución recibida · ref. original PI-26-0095110","DV-26-0001240","1,100.00","+",'<span class="badge info">Devolución</span>')}
      {mrow("30 ago. 21:03","PARQUEO MALECÓN","Pago con QR dinámico","PI-26-0094122","150.00","-",'<span class="badge ok">Completado</span>')}
      {mrow("29 ago. 14:55","L**** S***** R*****","Enviado a luisa***@correo.com","PI-26-0093004","5,000.00","-",'<span class="badge err">Reversado</span>')}
    </table>
    <div class="hstack" style="margin-top:16px"><span class="hint">Mostrando 9 de 47 movimientos</span><div class="spacer"></div><div class="btn btn-outline sm">Anterior</div><div class="btn btn-outline sm">Siguiente</div></div>
  </div>
</div>"""
    frame("G", "G-07", "Movimientos · historial y filtros", "post-venta", body)

    # G-08 devolucion / reclamacion
    modal = f"""<div class="scrim"><div class="modal lg">
  <div class="modal-head"><div class="ico" style="width:34px;height:34px;border-radius:10px;background:var(--warn-bg);color:var(--warn);display:flex;align-items:center;justify-content:center">{ico('request',20)}</div><h3>Solicitar devolución · PI-26-0098231</h3><div class="x">{ico('x',20)}</div></div>
  <div class="modal-body stack">
    {alert('warn','Los pagos instantáneos no se reversan de forma automática','Enviaremos tu solicitud al beneficiario y a su banco. La devolución depende de que la persona acepte o de que el banco confirme un fraude.')}
    <div class="grid-2" style="grid-template-columns:1fr 1fr">
      <div class="stack sm">
        {kv([("Pago original","DOP 2,500.00 · 02 sep. 15:12"),("Beneficiario","M**** P***** G***** · @mariaperez"),("Entidad","Banco Popular")])}
        <div class="field"><div class="label">Motivo de la devolución</div>
          <div class="rowitem sel"><div class="radio on"></div><div class="tx"><b>Me equivoqué de beneficiario o de monto</b></div></div>
          <div class="rowitem"><div class="radio"></div><div class="tx"><b>No recibí el producto o servicio</b></div></div>
          <div class="rowitem"><div class="radio"></div><div class="tx"><b>Fui víctima de una estafa</b><span>Se abre un caso prioritario con la unidad antifraude</span></div></div>
          <div class="rowitem"><div class="radio"></div><div class="tx"><b>No reconozco esta operación</b><span>Posible acceso no autorizado a tu cuenta</span></div></div>
        </div>
      </div>
      <div class="stack sm">
        {field("Monto a solicitar", inp("2,500.00","",pre="DOP"))}
        {field("Explica lo ocurrido", f'<div class="input" style="height:120px;align-items:flex-start;padding-top:12px"><span class="ph">Describe qué pasó, con fechas y detalles. No incluyas claves ni códigos.</span></div>')}
        {field("Evidencia <span class='opt'>(opcional)</span>", f'<div class="input" style="height:auto;padding:14px;justify-content:center;border-style:dashed;color:var(--ink-3)">{ico("upload",18)} Adjuntar capturas o documentos</div>')}
        <div class="hint">Plazo de respuesta: hasta 10 días hábiles. Recibirás un número de caso y seguimiento por correo.</div>
      </div>
    </div>
  </div>
  <div class="modal-foot"><div class="btn btn-ghost">Cancelar</div><div class="btn btn-primary">Enviar solicitud de devolución</div></div>
</div></div>"""
    body = f"""<div class="stack">{page_head("Detalle del movimiento","",["Pago Instantáneo","Movimientos","PI-26-0098231"])}<div style="height:520px"></div></div>"""
    frame("G", "G-08", "Movimientos · solicitar devolución", "modal · reclamación", body)

    # G-09 sesion por expirar + estados globales
    modal = f"""<div class="scrim"><div class="modal sm">
  <div class="modal-body stack" style="text-align:center;padding:34px">
    <div style="width:72px;height:72px;border-radius:50%;background:var(--warn-bg);color:var(--warn);display:flex;align-items:center;justify-content:center;margin:0 auto">{ico('clock',36)}</div>
    <b style="font-size:19px;color:var(--br-navy)">Tu sesión está por expirar</b>
    <div class="hint">Por tu seguridad cerraremos la sesión en <b style="color:var(--err);font-size:16px">00:47</b> por inactividad. Ningún pago en curso se verá afectado.</div>
    <div class="hstack" style="justify-content:center;margin-top:6px"><div class="btn btn-outline">Cerrar sesión</div><div class="btn btn-primary">Continuar conectado</div></div>
  </div>
</div></div>"""
    body = f"""
<div class="stack">
  {page_head("Estados globales y microcopy","Vacíos, avisos y confirmaciones transversales.",["Sistema","Estados"])}
  <div class="grid-3">
    <div class="card"><div class="empty"><div class="ic">{ico('at',34)}</div><b>Aún no tienes alias</b><span>Registra tu celular, correo o cédula para empezar a recibir pagos al instante.</span><div class="btn btn-primary sm">Registrar mi alias</div></div></div>
    <div class="card"><div class="empty"><div class="ic">{ico('list',34)}</div><b>Sin movimientos en este período</b><span>Prueba ampliando el rango de fechas o quitando filtros.</span><div class="btn btn-outline sm">Limpiar filtros</div></div></div>
    <div class="card"><div class="empty"><div class="ic">{ico('request',34)}</div><b>No tienes solicitudes</b><span>Cuando alguien te pida un pago, aparecerá aquí.</span><div class="btn btn-outline sm">Crear una solicitud</div></div></div>
  </div>
  <div class="grid-2">
    <div class="stack sm"><div class="label">Notificaciones (toasts)</div>
      <div class="toast"><div style="color:#7BE0A8">{ico('check',20,3)}</div><div><b>Alias registrado</b><span>809-555-1234 quedó activo en tu cuenta corriente ****3341.</span></div></div>
      <div class="toast"><div style="color:#8FD4FF">{ico('copy',20)}</div><div><b>Enlace copiado</b><span>Ya puedes pegarlo donde quieras compartirlo.</span></div></div>
      <div class="toast"><div style="color:#FFC48A">{ico('alert',20)}</div><div><b>Conexión inestable</b><span>Reintentando... no cierres esta ventana.</span></div></div>
      <div class="toast"><div style="color:#FF9B9B">{ico('x',20,3)}</div><div><b>No pudimos completar la operación</b><span>Intenta de nuevo en unos minutos. Nada fue debitado.</span></div></div>
    </div>
    <div class="stack sm"><div class="label">Mensajes de validación</div>
      <div class="card flat stack sm">
        <div class="hint error">{ico('alert',14,2.6)} El monto debe ser mayor a DOP 1.00</div>
        <div class="hint error">{ico('alert',14,2.6)} Supera tu límite por transacción (DOP 25,000.00)</div>
        <div class="hint error">{ico('alert',14,2.6)} El alias solo admite letras, números, punto y guion bajo</div>
        <div class="hint error">{ico('alert',14,2.6)} Código incorrecto. Te quedan 2 intentos</div>
        <div class="hint ok">{ico('check',14,3)} Alias disponible</div>
        <div class="hint ok">{ico('check',14,3)} Beneficiario verificado en el directorio nacional</div>
        <div class="hint">{ico('info',14,2.4)} El aumento de límite se activará el 03 sep. a las 15:40</div>
      </div>
      <div class="label" style="margin-top:8px">Principios de redacción</div>
      <div class="card flat"><div class="hint" style="line-height:1.8">Tuteo cercano y claro · el verbo primero ("Confirma el nombre") · nunca culpar al usuario ·
      decir siempre <b>qué pasó, por qué y qué hacer</b> · en errores de dinero, aclarar de inmediato si hubo o no débito.</div></div>
    </div>
  </div>
</div>"""
    frame("G", "G-09", "Sistema · estados vacíos, toasts y microcopy", "transversal", body, scrim=modal)

# ================================================================ ensamblaje
g_fundamentos(); g_entrada(); g_alias(); g_enviar(); g_solicitar(); g_qr(); g_seguridad()

GROUPS = [
  ("A", "Fundamentos", "Portada, design system, componentes y mapa de flujos del producto."),
  ("B", "Entrada al producto", "Cómo llega el cliente al IPS desde el Internet Banking actual."),
  ("C", "Mis Alias", "Registro, verificación, portabilidad y administración de las llaves de cobro."),
  ("D", "Enviar pago", "Flujo completo de envío con confirmación de beneficiario, 2FA y comprobante."),
  ("E", "Solicitar pago", "Cobros con enlace y QR, bandejas de enviadas y recibidas."),
  ("F", "Pagar con QR", "Lectura de QR estático y dinámico, mi QR de cobro y errores."),
  ("G", "Seguridad y post-venta", "Límites, dispositivos, autenticación, alertas, movimientos y devoluciones."),
]

parts = []
for gid, name, desc in GROUPS:
    rows = "".join(h for g, h in FRAMES if g == gid)
    parts.append(f"""<section class="group">
  <div class="group-head"><span class="n">{gid}</span><h2>{name}</h2><p>{desc}</p></div>
  <div class="row">{rows}</div>
</section>""")

n_frames = len(FRAMES)
html = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Banreservas · Pago Instantáneo RD · Kit de pantallas para Figma</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,400;0,6..12,600;0,6..12,700;0,6..12,800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="canvas">
  <header class="canvas-head">
    <h1>Banreservas · <span>Pago Instantáneo RD</span><br>Internet Banking · kit de pantallas</h1>
    <p>Prototipo de alta fidelidad del sistema de pagos inmediatos (IPS) dentro del Internet Banking de Banreservas,
       inspirado en Bre-B (Colombia), Pix (Brasil), DiMo (México) y Transfer 3.0 (Argentina). Incluye los flujos completos de
       registro y administración de alias, envío de pagos, solicitud de pagos, pagos con QR, y los controles de seguridad
       que aplican hoy los bancos a las transferencias: doble factor, confirmación de nombre del beneficiario, límites con
       enfriamiento, dispositivos de confianza y monitoreo antifraude.</p>
    <div class="canvas-meta">
      <em>{n_frames} frames</em><em>1440 px · desktop</em><em>Listo para html.to.design</em>
      <em>Tokens de color y tipografía</em><em>Iconografía SVG editable</em><em>Español · RD</em>
    </div>
  </header>
  {"".join(parts)}
</div>
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"OK · {n_frames} frames · {len(html)/1024:.0f} KB → {OUT}")
