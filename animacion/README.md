# NEUMA · Human Practices in 60 s

- `NEUMA_HP_60s.mp4`: final video (1920×1080, 30 fps, 60 s, no audio).
- `index.html`: the animation (open it in a browser to play and scrub).
- `render.js`: re-exports the MP4 → `node animacion/render.js animacion/NEUMA_HP_60s.mp4`.

Script: `../script_HP_NEUMIS.md` (content from the "HP Wiki NEUMA" document).

## NEUMIS
The character renders are in `animacion/neumis/` (sal, sus, mafe, ann). To replace one, overwrite its PNG
(transparent background, cropped to the character), update its `ar` (width / height) in `CAST` in `index.html`, and re-export.

## Brand
- Logo: `animacion/logo.png` (iGEM Puebla).
- Palette: #59181E, #732231, #750E1E, #152340, #1D2C40, #001A3B, #014040, #FDAF36, #F2EED8, #EDE9C2 (listed in `:root` in `index.html`).
- Typography: Bebas Neue (titles, names) and Source Sans Pro Bold (subtitles, body), in `animacion/fonts/`.
