const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
const p=await b.newPage({viewport:{width:1200,height:630},deviceScaleFactor:2});
await p.goto('https://jamilahmed.com/contact/',{waitUntil:'networkidle'});
await p.evaluate(()=>{document.head.querySelectorAll('link[rel=stylesheet],style').forEach(e=>{if(!/fonts/i.test(e.href||'')&&!/font-face/i.test(e.textContent||''))e.remove()});
document.body.className='';document.body.innerHTML=`
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:1200px;height:630px;background:#141312;color:#F4F3F1;font-family:"IBM Plex Sans",system-ui,sans-serif;overflow:hidden}
.w{position:relative;width:1200px;height:630px;padding:64px 72px;display:grid;grid-template-columns:1fr 400px;column-gap:64px;border-top:8px solid #AF824B}
h1{font-family:Oswald,"Arial Narrow",sans-serif;font-weight:500;text-transform:uppercase;font-size:84px;line-height:1.02;letter-spacing:.005em}
h1 em{font-style:normal;color:#CDA56F}
.sub{margin-top:28px;font-size:27px;line-height:1.4;color:#B3ADA5;max-width:560px}
.by{position:absolute;left:72px;bottom:56px;font-family:"IBM Plex Mono",monospace;font-size:17px;letter-spacing:.14em;text-transform:uppercase;color:#B3ADA5}
.by b{color:#F4F3F1;font-weight:500}
.card{align-self:center;background:#1F1D1B;border:1px solid rgba(205,165,111,.35);border-top:3px solid #AF824B;padding:30px 28px 26px}
.q{font-family:"IBM Plex Mono",monospace;font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:#CDA56F;margin-bottom:20px}
.l{height:12px;background:rgba(244,243,241,.2);margin-bottom:14px}
.l.s{width:62%}.l.m{width:84%}
.r{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.r .l{margin:0;flex:1}
.c{flex:none;width:30px;height:24px;border:1px solid #AF824B;color:#CDA56F;font-family:"IBM Plex Mono",monospace;font-size:13px;display:flex;align-items:center;justify-content:center}
.src{margin-top:24px;padding-top:18px;border-top:1px solid rgba(244,243,241,.14);display:grid;gap:10px}
.s1{display:flex;gap:12px;align-items:center;font-size:17px;color:#B3ADA5}
.s1.you{color:#F4F3F1;font-weight:600}
.s1.you .c{background:#AF824B;color:#141312;font-weight:600}
</style>
<div class="w"><div><h1>Generative Engine Optimization <em>(GEO)</em></h1><p class="sub">How to get cited in AI answers, and what the research says works.</p></div>
<div class="card"><p class="q">AI answer</p><div class="l"></div><div class="r"><div class="l"></div><span class="c">1</span></div><div class="l m"></div><div class="r"><div class="l"></div><span class="c">2</span></div><div class="l s"></div>
<div class="src"><div class="s1 you"><span class="c">1</span>Your page</div><div class="s1"><span class="c">2</span>Another source</div></div></div>
<p class="by"><b>Jamil Ahmed</b> &nbsp;/&nbsp; SEO &amp; AI Search Consultant</p></div>`});
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
console.log(await p.evaluate(()=>[document.fonts.check('500 84px Oswald'),document.fonts.check('17px "IBM Plex Mono"')]));
await p.screenshot({path:'geo-2x.png',clip:{x:0,y:0,width:1200,height:630}});await b.close()})();
