// Render SVGs to transparent PNGs. Usage: node render.mjs out_dir width file1.svg file2.svg ...
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const [outDir, width, ...files] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage();
for (const f of files) {
  const src = fs.readFileSync(f, 'utf8');
  const m = src.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
  const [vw, vh] = [parseFloat(m[1]), parseFloat(m[2])];
  const w = parseInt(width), h = Math.round(w * vh / vw);
  await page.setViewportSize({ width: w, height: h });
  const sized = src.replace(/width="[\d.]+" height="[\d.]+"/, `width="${w}" height="${h}"`);
  await page.setContent(`<html><body style="margin:0;background:transparent">${sized}</body></html>`);
  const name = path.basename(f, '.svg') + (process.env.SUFFIX ?? '') + '.png';
  await page.screenshot({ path: path.join(outDir, name), omitBackground: true, clip: { x: 0, y: 0, width: w, height: h } });
}
await browser.close();
