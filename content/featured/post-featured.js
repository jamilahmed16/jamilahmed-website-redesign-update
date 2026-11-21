const {chromium}=require('playwright');const fs=require('fs');
const posts=JSON.parse(fs.readFileSync('visible.json')).filter(p=>p[0]!==876);
const catName={'List Posts':'Tools','Search Engine Optimization':'SEO'};
(async()=>{const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});const p=await b.newPage({viewport:{width:1200,height:630},deviceScaleFactor:2});
await p.goto('https://jamilahmed.com/contact/',{waitUntil:'networkidle'});
await p.evaluate(()=>{document.head.querySelectorAll('link[rel=stylesheet],style').forEach(e=>{if(!/fonts/i.test(e.href||'')&&!/font-face/i.test(e.textContent||''))e.remove()});document.body.className='';});
for(const [id,slug,title,cat] of posts){
 await p.evaluate(({title,cat})=>{const t=title.replace(/ /g,' ');const len=t.length;const fs=len>60?66:len>42?76:88;
 document.body.innerHTML=`<style>*{box-sizing:border-box;margin:0;padding:0}body{width:1200px;height:630px;background:#141312;overflow:hidden;font-family:"IBM Plex Sans",sans-serif}
 .w{position:relative;width:1200px;height:630px;padding:84px 80px 0;border-top:8px solid #AF824B}

 h1{font-family:Oswald,"Arial Narrow",sans-serif;font-weight:500;text-transform:uppercase;color:#F4F3F1;font-size:${fs}px;line-height:1.04;max-width:900px;letter-spacing:.005em}
 .f{position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;align-items:center;padding-top:26px;border-top:1px solid rgba(244,243,241,.16);font-family:"IBM Plex Mono",monospace;font-size:17px;letter-spacing:.14em;text-transform:uppercase;color:#B3ADA5}
 .f b{color:#F4F3F1;font-weight:500}.f i{font-style:normal;color:#CDA56F}</style>
 <div class="w"><h1>${t.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</h1><div class="f"><span><b>Jamil Ahmed</b> &nbsp;/&nbsp; SEO &amp; AI Search Consultant</span><i>${cat}</i></div></div>`},{title,cat:catName[cat]||cat});
 await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
 const over=await p.evaluate(()=>{const h=document.querySelector('h1').getBoundingClientRect();return h.bottom>520});
 await p.screenshot({path:`feat/${slug}.png`,clip:{x:0,y:0,width:1200,height:630}});console.log(slug,over?'OVERFLOW':'ok');}
await b.close()})();
