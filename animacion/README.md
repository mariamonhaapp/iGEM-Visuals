# NEUMA · Human Practices en 60 s

- `NEUMA_HP_60s.mp4`: video final (1920×1080, 30 fps, 60 s, sin audio).
- `index.html`: la animación (ábrela en el navegador para verla y moverte con la barra de tiempo).
- `render.js`: vuelve a exportar el MP4 → `node animacion/render.js animacion/NEUMA_HP_60s.mp4`.

Guion: `../guion_HP_NEUMIS.md` (contenido del documento "HP Wiki NEUMA").

## Cambiar a los NEUMIS reales
En `index.html`, dentro de `CAST`, pon la ruta del PNG (fondo transparente, de cuerpo completo) en `img`,
por ejemplo `img: "neumis/mafe.png"`, guarda la imagen en `animacion/neumis/` y vuelve a exportar.

## Cambiar a los colores del wiki
Los colores provisionales están al inicio del `<style>` (`:root`) y en el `color` de cada NEUMI en `CAST`.
