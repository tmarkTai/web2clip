// Lớp hiệu ứng tiêm vào trang: viền sáng, phụ đề, khung tiêu đề, con trỏ ảo, nhấp nháy.
(()=>{if(window.__ov)return;window.__ov=1;
const st=document.createElement('style');st.textContent=`
#__hl{position:fixed;border:4px solid #F6D34B;border-radius:14px;box-shadow:0 0 0 9999px rgba(15,27,61,.35),0 0 24px #F6D34B;z-index:99999;pointer-events:none;transition:all .45s ease;opacity:0}
#__cap{pointer-events:none;position:fixed;left:4%;right:4%;bottom:5%;z-index:100003;background:rgba(15,27,61,.92);color:#fff;font:700 20px/1.35 "Be Vietnam Pro",system-ui,sans-serif;padding:12px 16px;border-radius:14px;border-left:5px solid #F6D34B;opacity:0;transition:opacity .3s;text-align:left}
#__tc{position:fixed;inset:0;z-index:100001;background:#0F1B3D;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;font-family:"Be Vietnam Pro",system-ui,sans-serif;opacity:0;transition:opacity .5s;pointer-events:none;text-align:center;padding:30px}
#__tc img{width:200px;height:200px;border-radius:50%;background:#fff;box-shadow:0 0 0 10px rgba(201,162,74,.35)}
#__tc small{color:#C9A24A;font-weight:800;font-size:18px}#__tc h1{margin:0;font-size:34px;line-height:1.2}#__tc p{margin:0;color:#C8D0E6;font-size:17px}
#__tc .who{background:#17264F;border:1px solid rgba(201,162,74,.5);border-radius:999px;padding:6px 16px;font-weight:700;color:#F3E6C4}
#__cur{position:fixed;width:26px;height:26px;border-radius:50%;background:rgba(245,51,63,.85);border:3px solid #fff;z-index:100002;pointer-events:none;transition:all .6s ease;left:50%;top:50%;opacity:0;box-shadow:0 2px 8px rgba(0,0,0,.3)}
#__cur.tap{transform:scale(.7)}
@keyframes __pulse{0%,100%{box-shadow:0 0 0 9999px rgba(15,27,61,.35),0 0 10px #F6D34B}50%{box-shadow:0 0 0 9999px rgba(15,27,61,.35),0 0 34px #F6D34B}}
#__hl.on{animation:__pulse 1.2s infinite}
.__flash{animation:__fl .6s 3}@keyframes __fl{50%{background:#F6D34B!important;color:#0F1B3D!important}}`;
document.head.appendChild(st);
for(const id of['__hl','__cap','__tc','__cur']){const d=document.createElement('div');d.id=id;document.body.appendChild(d);}
window.__hlOn=(sel,pad=8)=>{const e=document.querySelector(sel);if(!e)return false;e.scrollIntoView({block:'center',behavior:'instant'});const r=e.getBoundingClientRect(),h=document.getElementById('__hl');Object.assign(h.style,{left:(r.left-pad)+'px',top:(r.top-pad)+'px',width:(r.width+2*pad)+'px',height:(r.height+2*pad)+'px',opacity:1});h.classList.add('on');return true;};
window.__hlOff=()=>{const h=document.getElementById('__hl');h.style.opacity=0;h.classList.remove('on');};
window.__cap=t=>{const c=document.getElementById('__cap');if(!t){c.style.opacity=0;return;}c.textContent=t;c.style.opacity=1;};
window.__tc=(html)=>{const c=document.getElementById('__tc');if(!html){c.style.opacity=0;return;}c.innerHTML=html;c.style.opacity=1;};
window.__cur=(sel,tap)=>{const e=document.querySelector(sel),c=document.getElementById('__cur');if(!e)return;const r=e.getBoundingClientRect();c.style.left=(r.left+r.width/2-13)+'px';c.style.top=(r.top+r.height/2-13)+'px';c.style.opacity=1;if(tap){setTimeout(()=>{c.classList.add('tap');setTimeout(()=>c.classList.remove('tap'),250)},650);}};
window.__hlText=(t,pad=6)=>{const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n,best=null;while(n=w.nextNode()){if(n.textContent.includes(t)){let e=n.parentElement;if(e.offsetParent!==null){best=e;break;}}}if(!best)return false;best.id=best.id||('__t'+Math.random().toString(36).slice(2));return window.__hlOn('#'+best.id,pad);};
window.__flash=sel=>{const e=document.querySelector(sel);if(e){e.classList.remove('__flash');void e.offsetWidth;e.classList.add('__flash');}};
})();
