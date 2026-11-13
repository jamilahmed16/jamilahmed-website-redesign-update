// Screenshot draft pages while logged in, using a one-time Novamira admin access link.
// Usage: node tools/shoot.js <outdir> <page_id>[,<page_id>...] [widths=1440,390]
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');
const fs = require('fs');

const [outdir, ids, widthsArg] = process.argv.slice(2);
const widths = (widthsArg || '1440,390').split(',').map(Number);
const env = { ...process.env, NODE_USE_ENV_PROXY: '1', NODE_NO_WARNINGS: '1' };

function accessLink() {
  const raw = execFileSync('novamira', ['--site', 'jamilahmed.com', 'run', 'novamira/create-admin-access-link',
    '--input', '{"expires_in":120,"session_expires_in":1800,"admin_path":""}', '--json', '--yes'], { env, encoding: 'utf8' });
  return JSON.parse(raw).data;
}

(async () => {
  fs.mkdirSync(outdir, { recursive: true });
  const a = accessLink();
  const res = await fetch(a.exchange_url, { method: 'POST', headers: { [a.token_header]: a.access_token, [a.nonce_header]: a.access_nonce } });
  const body = await res.json();
  const loginUrl = body.url || body.login_url || body.data?.url;
  if (!loginUrl) throw new Error('No login URL returned: ' + JSON.stringify(Object.keys(body)));
  const browser = await chromium.launch(process.env.HTTPS_PROXY ? { proxy: { server: process.env.HTTPS_PROXY } } : {});
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  await page.goto(loginUrl, { waitUntil: 'domcontentloaded' });
  for (const id of ids.split(',')) {
    for (const w of widths) {
      await page.setViewportSize({ width: w, height: w < 600 ? 844 : 900 });
      await page.goto(`https://jamilahmed.com/?page_id=${id}&preview=true`, { waitUntil: 'networkidle' });
      await page.addStyleTag({ content: '#wpadminbar{display:none!important} html{margin-top:0!important}' });
      await page.evaluate(() => document.fonts.ready);
      await page.screenshot({ path: `${outdir}/p${id}-${w}.png`, fullPage: true });
      await page.screenshot({ path: `${outdir}/p${id}-${w}-fold.png`, fullPage: false });
      const errs = await page.evaluate(() => ({ title: document.title, hasRoot: !!document.querySelector('.ja26-root'), h1: document.querySelector('h1')?.innerText }));
      console.log(id, w, JSON.stringify(errs));
    }
  }
  await browser.close();
})().catch(e => { console.error(e.message); process.exit(1); });
