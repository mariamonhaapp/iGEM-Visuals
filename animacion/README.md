# NEUMA · Human Practices in 60 s

- `NEUMA_HP_60s.mp4`: final video (1920×1080, 30 fps, 60 s, no audio).
- `index.html`: the animation (open it in a browser to play and scrub).
- `render.js`: re-exports the MP4 → `node animacion/render.js animacion/NEUMA_HP_60s.mp4`.

Script: `../script_HP_NEUMIS.md` (content from the "HP Wiki NEUMA" document).

## Swap in the real NEUMIS
In `index.html`, inside `CAST`, set `img` to the PNG path (transparent background, full body),
e.g. `img: "neumis/mafe.png"`, save the image in `animacion/neumis/`, and re-export.

## Swap in the wiki colors
The provisional colors are at the top of `<style>` (`:root`) and in each NEUMI's `color` in `CAST`.
