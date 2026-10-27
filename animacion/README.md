# NEUMA · Human Practices in 60 s

- `NEUMA_HP_60s.mp4`: final video (1920×1080, 30 fps, 60 s, no audio).
- `index.html`: the animation (open it in a browser to play and scrub).
- `render.js`: re-exports the MP4 → `node animacion/render.js animacion/NEUMA_HP_60s.mp4`.

Script: `../script_HP_NEUMIS.md` (content from the "HP Wiki NEUMA" document).

## NEUMIS
The character renders are in `animacion/neumis/` (sal, sus, mafe, ann). To replace one, overwrite its PNG
(transparent background, cropped to the character), update its `ar` (width / height) in `CAST` in `index.html`, and re-export.

## Swap in the wiki colors
The provisional colors are at the top of `<style>` (`:root`) and in each NEUMI's `color` in `CAST`.
