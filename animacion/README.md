# NEUMA · Human Practices in 60 s

- `NEUMA_HP_60s.mp4`: final video (1920×1080, 30 fps, 59.9 s, with voices).
- `index.html`: the animation (open it in a browser to play and scrub).
- `render.js`: re-exports the MP4 → `node animacion/render.js animacion/NEUMA_HP_60s.mp4`.

Script: `../script_HP_NEUMIS.md` (content from the "HP Wiki NEUMA" document).

## NEUMIS
The character renders are in `animacion/neumis/` (sal, sus, mafe, ann). `tools/rig.py` splits each one into
a body layer (face erased from the screen, arms removed) and one layer per arm, and writes `neumis/rig.json`
with the screen position and shoulder pivots. `index.html` redraws each face so it blinks and talks, swings the
arms from the shoulders, and squashes the body while speaking.

To replace a NEUMI: overwrite its PNG (transparent background, cropped to the character), adjust its arm polygons
and pivots in `tools/rig.py`, run `python3 animacion/tools/rig.py` (needs numpy and opencv), paste the new
`rig.json` into `const RIG` in `index.html`, and re-export.

## Brand
- Logo: `animacion/logo.png` (iGEM Puebla).
- Palette: #59181E, #732231, #750E1E, #152340, #1D2C40, #001A3B, #014040, #FDAF36, #F2EED8, #EDE9C2 (listed in `:root` in `index.html`).
- Typography: Bebas Neue (titles, names) and Source Sans Pro Bold (subtitles, body), in `animacion/fonts/`.

## Voices
`tools/audio.py` takes the 7 voice clips in scene order (Mafe, Sal, Sus, Ann, Mafe, Sal, All), trims edge silence,
speeds them up 10% (pitch kept) so the video stays under a minute, normalizes loudness, and writes `audio/voices.wav`
plus `audio/timeline.json` (scene bounds, subtitle times, and a loudness envelope that drives the mouths).
After re-running it, paste `timeline.json` into `const TIMELINE` in `index.html` and re-export.
Where a clip holds two subtitles, the split point is set by hand in `CLIPS` in `tools/audio.py`.
