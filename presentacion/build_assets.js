// Renders the deck's figures (map, chip surface, plasmid maps, icons) to transparent PNGs in assets/.
// Usage: node presentacion/build_assets.js
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const A = path.join(__dirname, "assets");
const FONTS = path.join(__dirname, "..", "animacion", "fonts");
const C = {
  maroonDark: "#59181E", maroon: "#732231", crimson: "#750E1E", navy: "#152340", navy2: "#1D2C40",
  deep: "#001A3B", teal: "#014040", amber: "#FDAF36", cream: "#F2EED8", cream2: "#EDE9C2",
};
// fonts are inlined: pages built with setContent cannot load file:// URLs
const font = f => `url(data:font/woff2;base64,${fs.readFileSync(path.join(FONTS, f)).toString("base64")})`;
const css = `
  @font-face { font-family: "Bebas Neue"; src: ${font("bebas-neue-latin-400-normal.woff2")}; }
  @font-face { font-family: "Source Sans Pro"; font-weight: 700; src: ${font("source-sans-pro-latin-700-normal.woff2")}; }
  html, body { margin: 0; background: transparent; }
  text { font-family: "Source Sans Pro"; font-weight: 700; }
  .bebas { font-family: "Bebas Neue"; font-weight: 400; letter-spacing: 1px; }`;

// ---------- map: Mexico with Puebla highlighted, and a Puebla city inset with the two hospitals ----------
function mapSvg() {
  const src = fs.readFileSync(path.join(A, "mexico.svg"), "utf8");
  const paths = [...src.matchAll(/<path\s+id="(\w+)"[\s\S]*?d="([^"]+)"/g)].map(([, id, d]) =>
    `<path id="${id}" d="${d}" fill="${id === "pue" ? C.maroon : C.navy2}" stroke="${id === "pue" ? C.amber : C.cream2}"
      stroke-opacity="${id === "pue" ? 1 : 0.35}" stroke-width="${id === "pue" ? 1.6 : 0.6}"/>`).join("");
  const pin = (x, y, col) => `<g transform="translate(${x},${y})"><path d="M0 0 C-26 -34 -30 -48 -30 -60 A30 30 0 1 1 30 -60 C30 -48 26 -34 0 0 Z" fill="${col}" stroke="${C.deep}" stroke-width="5"/><circle cy="-60" r="11" fill="${C.deep}"/></g>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="1500" viewBox="0 0 1500 1500">
    <g id="mx" transform="translate(-30,20) scale(1.95)">${paths}</g>
    <g id="leader"></g>
    <g transform="translate(860,1150)">
      <circle r="300" fill="${C.navy}" stroke="${C.cream2}" stroke-width="5"/>
      <g stroke="${C.cream2}" stroke-opacity=".18" stroke-width="10" fill="none" stroke-linecap="round">
        <path d="M-280 -40 C-120 -60 60 -20 280 -70"/><path d="M-60 -290 C-40 -120 -70 80 -40 290"/>
        <path d="M-230 170 C-80 110 90 140 230 190"/><path d="M90 -270 C120 -120 160 20 210 160"/>
        <circle r="120" stroke-opacity=".12"/>
      </g>
      ${pin(150, -40, C.amber)}${pin(-40, 150, C.cream)}
      <text x="110" y="40" font-size="34" fill="${C.amber}" text-anchor="middle">HGZ No. 20 “La Margarita”</text>
      <text x="110" y="78" font-size="28" fill="${C.cream2}" text-anchor="middle">IMSS</text>
      <text x="-40" y="200" font-size="34" fill="${C.cream}" text-anchor="middle">Hospital Regional</text>
      <text x="-40" y="238" font-size="28" fill="${C.cream2}" text-anchor="middle">ISSSTE Puebla</text>
      <text class="bebas" x="0" y="-205" font-size="60" fill="${C.cream}" text-anchor="middle">Puebla city</text>
      <text x="0" y="-165" font-size="24" fill="${C.cream2}" fill-opacity=".7" text-anchor="middle">schematic · not to scale</text>
    </g>
  </svg>`;
}

// ---------- chip surface: before / after ----------
function chipSvg() {
  const dcas9 = (x, y, rot, label = true) => `<g transform="translate(${x},${y}) rotate(${rot})">
      <path d="M-62 -10 C-70 -90 -20 -140 20 -130 C70 -120 80 -60 62 -10 C50 20 -50 20 -62 -10 Z" fill="${C.teal}" stroke="${C.deep}" stroke-width="4"/>
      ${label ? `<text x="2" y="-58" font-size="30" fill="${C.cream}" text-anchor="middle">dCas9</text>` : ""}</g>`;
  const gold = (x, w) => `<rect x="${x}" y="560" width="${w}" height="70" rx="10" fill="#D9A23A" stroke="${C.maroonDark}" stroke-width="4"/>
      <rect x="${x}" y="630" width="${w}" height="60" rx="10" fill="${C.navy2}" fill-opacity=".25"/>`;
  let s = `<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="820" viewBox="0 0 1800 820">`;
  // before
  s += `<text class="bebas" x="400" y="70" font-size="64" fill="${C.deep}" text-anchor="middle">Before · cysteine anchoring</text>`;
  s += gold(60, 680);
  [[180, 470, -18], [400, 455, 12], [610, 480, -35]].forEach(([x, y, r]) => {
    s += dcas9(x, y, r);
    s += `<line x1="${x}" y1="${y + 8}" x2="${x}" y2="560" stroke="${C.maroon}" stroke-width="7" stroke-dasharray="10 8"/>`;
    s += `<text x="${x + 14}" y="545" font-size="22" fill="${C.maroon}">S–Au</text>`;
  });
  s += `<text x="400" y="735" font-size="30" fill="${C.deep}" text-anchor="middle">Gold surface · random orientation</text>`;
  // arrow
  s += `<path d="M830 400 H950" stroke="${C.amber}" stroke-width="22" stroke-linecap="round"/><path d="M945 360 L1000 400 L945 440 Z" fill="${C.amber}"/>`;
  // after
  s += `<text class="bebas" x="1400" y="70" font-size="64" fill="${C.deep}" text-anchor="middle">After · AviTag–biotin / streptavidin</text>`;
  s += gold(1060, 680);
  for (let i = 0; i < 6; i++) s += `<rect x="${1080 + i * 108}" y="500" width="92" height="56" rx="18" fill="${C.maroon}" stroke="${C.maroonDark}" stroke-width="4"/><text x="${1126 + i * 108}" y="538" font-size="24" fill="${C.cream}" text-anchor="middle">SA</text>`;
  [1180, 1400, 1620].forEach(x => {
    s += `<circle cx="${x}" cy="492" r="13" fill="${C.amber}" stroke="${C.deep}" stroke-width="3"/>`;
    s += `<rect x="${x - 9}" y="430" width="18" height="52" rx="6" fill="${C.crimson}"/>`;
    s += dcas9(x, 428, 0);
  });
  s += `<text x="1700" y="470" font-size="22" fill="${C.deep}" text-anchor="start">AviTag</text>`;
  s += `<text x="1060" y="462" font-size="22" fill="${C.deep}">biotin</text>`;
  s += `<text x="1400" y="735" font-size="30" fill="${C.deep}" text-anchor="middle">Streptavidin SPR chip · oriented dCas9</text>`;
  return s + `</svg>`;
}

// ---------- plasmid maps: one bicistronic vector → two separate vectors ----------
function arc(cx, cy, r, a1, a2, color, w, arrow = true) {
  const P = a => [cx + r * Math.sin(a * Math.PI / 180), cy - r * Math.cos(a * Math.PI / 180)];
  const [x1, y1] = P(a1), [x2, y2] = P(arrow ? a2 - 6 : a2), large = (a2 - a1) > 180 ? 1 : 0;
  let s = `<path d="M${x1} ${y1} A${r} ${r} 0 ${large} 1 ${x2} ${y2}" fill="none" stroke="${color}" stroke-width="${w}"/>`;
  if (arrow) {
    const [ox, oy] = [cx + (r + w * .8) * Math.sin((a2 - 6) * Math.PI / 180), cy - (r + w * .8) * Math.cos((a2 - 6) * Math.PI / 180)];
    const [ix, iy] = [cx + (r - w * .8) * Math.sin((a2 - 6) * Math.PI / 180), cy - (r - w * .8) * Math.cos((a2 - 6) * Math.PI / 180)];
    const [tx, ty] = P(a2);
    s += `<path d="M${ox} ${oy} L${tx} ${ty} L${ix} ${iy} Z" fill="${color}"/>`;
  }
  return s;
}
function label(cx, cy, r, a, text, color = C.deep, size = 28) {
  const x = cx + r * Math.sin(a * Math.PI / 180), y = cy - r * Math.cos(a * Math.PI / 180);
  const anchor = Math.abs(Math.sin(a * Math.PI / 180)) < .25 ? "middle" : (Math.sin(a * Math.PI / 180) > 0 ? "start" : "end");
  return `<text x="${x}" y="${y + size * .35}" font-size="${size}" fill="${color}" text-anchor="${anchor}">${text}</text>`;
}
function plasmid(cx, cy, r, title, parts) {
  let s = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${C.navy2}" stroke-opacity=".3" stroke-width="16"/>`;
  for (const p of parts) {
    s += arc(cx, cy, r, p.a1, p.a2, p.color, 30, p.arrow !== false);
    s += label(cx, cy, r + 46, (p.a1 + p.a2) / 2, p.name, p.color === C.amber ? C.maroonDark : p.color);
  }
  s += `<text class="bebas" x="${cx}" y="${cy - 8}" font-size="46" fill="${C.deep}" text-anchor="middle">${title[0]}</text>`;
  s += `<text x="${cx}" y="${cy + 32}" font-size="26" fill="${C.deep}" fill-opacity=".7" text-anchor="middle">${title[1]}</text>`;
  return s;
}
function plasmidSvg() {
  let s = `<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="820" viewBox="0 0 1800 820">`;
  s += `<text class="bebas" x="390" y="70" font-size="64" fill="${C.deep}" text-anchor="middle">Before · one bicistronic vector</text>`;
  s += plasmid(390, 450, 230, ["Bicistronic", "dCas9-AviTag / BirA"], [
    { name: "promoter", a1: 330, a2: 352, color: C.amber },
    { name: "dCas9", a1: 356, a2: 470, color: C.teal },
    { name: "AviTag", a1: 112, a2: 130, color: C.crimson, arrow: false },
    { name: "RBS", a1: 136, a2: 146, color: C.navy, arrow: false },
    { name: "BirA", a1: 150, a2: 210, color: C.maroon },
    { name: "terminator", a1: 214, a2: 224, color: C.navy, arrow: false },
  ]);
  s += `<path d="M770 450 H880" stroke="${C.amber}" stroke-width="22" stroke-linecap="round"/><path d="M875 410 L930 450 L875 490 Z" fill="${C.amber}"/>`;
  s += `<text class="bebas" x="1370" y="70" font-size="64" fill="${C.deep}" text-anchor="middle">After · two separate vectors</text>`;
  s += plasmid(1110, 470, 170, ["Vector 1", "dCas9-AviTag"], [
    { name: "promoter", a1: 330, a2: 352, color: C.amber },
    { name: "dCas9", a1: 356, a2: 470, color: C.teal },
    { name: "AviTag", a1: 114, a2: 134, color: C.crimson, arrow: false },
    { name: "term.", a1: 140, a2: 152, color: C.navy, arrow: false },
  ]);
  s += plasmid(1510, 470, 140, ["Vector 2", "BirA"], [
    { name: "promoter", a1: 330, a2: 352, color: C.amber },
    { name: "BirA", a1: 356, a2: 440, color: C.maroon },
    { name: "term.", a1: 86, a2: 98, color: C.navy, arrow: false },
  ]);
  s += `<text x="900" y="790" font-size="26" fill="${C.deep}" fill-opacity=".7" text-anchor="middle">Schematic · not to scale · backbone elements omitted</text>`;
  return s + `</svg>`;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  async function render(svg, out, w, h) {
    await page.setViewportSize({ width: w, height: h });
    await page.setContent(`<style>${css}</style>${svg}`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(A, out), omitBackground: true, clip: { x: 0, y: 0, width: w, height: h } });
  }
  // map: draw a leader line from Puebla's centre to the inset after layout
  await page.setViewportSize({ width: 1500, height: 1500 });
  await page.setContent(`<style>${css}</style>${mapSvg()}`);
  await page.evaluate(C => {
    const pue = document.getElementById("pue"), mx = document.getElementById("mx");
    const b = pue.getBBox(), m = mx.getCTM();
    const x = m.a * (b.x + b.width / 2) + m.e, y = m.d * (b.y + b.height / 2) + m.f;
    document.getElementById("leader").innerHTML =
      `<line x1="${x}" y1="${y}" x2="860" y2="850" stroke="${C.amber}" stroke-width="5" stroke-dasharray="14 10"/>
       <circle cx="${x}" cy="${y}" r="12" fill="${C.amber}"/>`;
  }, C);
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(A, "map.png"), omitBackground: true });
  await render(chipSvg(), "chip.png", 1800, 820);
  await render(plasmidSvg(), "plasmids.png", 1800, 820);
  for (const f of fs.readdirSync(path.join(A, "icons")).filter(f => f.endsWith(".svg"))) {
    const svg = fs.readFileSync(path.join(A, "icons", f), "utf8").replace(/<!--.*?-->/s, "");
    for (const [name, col] of [["cream", C.cream], ["navy", C.deep], ["amber", C.amber], ["maroon", C.maroon]]) {
      await render(svg.replace('width="24"', 'width="256"').replace('height="24"', 'height="256"').replace('stroke="currentColor"', `stroke="${col}"`),
        `icons/${f.replace(".svg", "")}-${name}.png`, 256, 256);
    }
  }
  await browser.close();
  console.log("assets ready");
})();
