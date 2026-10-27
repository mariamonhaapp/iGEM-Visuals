// Exports the animation to MP4 (1920x1080, 30 fps) with the voice track from audio/voices.wav.
// Usage: node animacion/render.js [out.mp4] [fps]
// Single frames for review: node animacion/render.js --stills 3,10,20 [outDir]
const { chromium } = require("playwright");
const { spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto("file://" + path.join(__dirname, "index.html") + "?capture=1");
  await page.evaluate(() => Promise.all([document.fonts.ready, window.assetsReady]));
  // warm-up pass so every layer has been drawn once before frames are captured
  for (let t = 0; t < 60; t += 2) await page.evaluate(t => window.renderAt(t), t);
  const stage = await page.$("#wrap");
  const DURATION = await page.evaluate(() => DURATION);

  if (args[0] === "--stills") {
    const out = args[2] || path.join(__dirname, "stills");
    fs.mkdirSync(out, { recursive: true });
    for (const s of args[1].split(",").map(Number)) {
      await page.evaluate(t => window.renderAt(t), s);
      await stage.screenshot({ path: path.join(out, `t${String(s).padStart(5, "0")}.png`) });
    }
    await browser.close();
    return;
  }

  const outFile = path.resolve(args[0] || path.join(__dirname, "NEUMA_HP_60s.mp4"));
  const fps = Number(args[1] || 30);
  const frames = fs.mkdtempSync(path.join(require("os").tmpdir(), "neuma-frames-"));
  const total = Math.round(DURATION * fps);
  for (let i = 0; i < total; i++) {
    await page.evaluate(t => window.renderAt(t), i / fps);
    await stage.screenshot({ path: path.join(frames, `${String(i).padStart(5, "0")}.jpg`), type: "jpeg", quality: 92 });
    if (i % (fps * 5) === 0) console.log(`frame ${i}/${total}`);
  }
  await browser.close();
  const voice = path.join(__dirname, "audio", "voices.wav");
  const audioIn = fs.existsSync(voice) ? ["-i", voice, "-c:a", "aac", "-b:a", "192k"] : [];
  const r = spawnSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(fps), "-i", path.join(frames, "%05d.jpg"),
    ...audioIn, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", "-shortest", outFile], { stdio: "inherit" });
  fs.rmSync(frames, { recursive: true, force: true });
  if (r.status !== 0) process.exit(r.status);
  console.log("Done:", outFile);
})();
