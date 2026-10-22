// Screenshot each HTML page at its body size. Usage: node shoot.mjs out_dir page1.html ...
import { chromium } from 'playwright';
import fs from 'fs'; import path from 'path';
const [outDir, ...files] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const b = await chromium.launch(); const p = await b.newPage();
for (const f of files) {
  await p.goto('file://' + path.resolve(f)); await p.evaluate(() => document.fonts.ready);
  const { w, h } = await p.evaluate(() => ({ w: document.body.offsetWidth, h: document.body.offsetHeight }));
  await p.setViewportSize({ width: w, height: h });
  await p.screenshot({ path: path.join(outDir, path.basename(f, '.html') + '.png') });
}
await b.close();
