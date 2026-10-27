"""Split each NEUMI render into animatable layers.

For every character it writes, next to the source PNG:
  <name>_body.png   the render with the arms removed and the face erased from the screen
  <name>_arm<i>.png one full-size layer per arm (with the prop it holds)
and rig.json with the screen geometry and arm pivots used by index.html.

Usage: python3 animacion/tools/rig.py
"""
import json
from pathlib import Path

import cv2
import numpy as np

NEUMIS = Path(__file__).resolve().parent.parent / "neumis"

# Arm polygons and shoulder pivots, in source-image pixels (see neumis/<name>.png).
ARMS = {
    "sal": [
        {"poly": [(672, 0), (919, 0), (919, 170), (800, 255), (735, 255), (688, 245), (672, 200)], "pivot": (700, 232)},
        {"poly": [(0, 505), (40, 492), (100, 498), (132, 540), (137, 712), (0, 712)], "pivot": (128, 565)},
    ],
    "mafe": [
        {"poly": [(0, 340), (170, 360), (292, 412), (300, 530), (200, 592), (0, 640)], "pivot": (288, 470)},
        {"poly": [(835, 20), (1017, 20), (1017, 215), (912, 272), (862, 266), (858, 150), (845, 110)], "pivot": (872, 232)},
    ],
    "ann": [
        {"poly": [(0, 0), (198, 0), (284, 196), (288, 276), (160, 280), (0, 225)], "pivot": (282, 238)},
        {"poly": [(806, 368), (1015, 368), (1015, 565), (858, 525), (802, 462)], "pivot": (812, 422)},
    ],
    "sus": [
        {"poly": [(0, 438), (163, 438), (168, 602), (0, 602)], "pivot": (160, 560)},
    ],
}


def screen_geometry(rgba):
    rgb, alpha = rgba[..., :3].astype(int), rgba[..., 3]
    dark = ((rgb.max(axis=2) < 45) & (alpha > 200)).astype(np.uint8)
    n, labels, stats, _ = cv2.connectedComponentsWithStats(dark, 8)
    big = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    comp = (labels == big).astype(np.uint8)
    contours, _ = cv2.findContours(comp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt = max(contours, key=cv2.contourArea)
    mask = np.zeros_like(comp)
    cv2.drawContours(mask, [cnt], -1, 1, -1)
    (cx, cy), (w, h), ang = cv2.minAreaRect(cnt)
    if w < h:  # keep the long side horizontal
        w, h, ang = h, w, ang + 90
    if ang > 45:
        ang -= 180
    if ang < -45:
        ang += 180
    return mask, {"cx": cx, "cy": cy, "w": w, "h": h, "angle": ang}


def main():
    rig = {}
    for name, arms in ARMS.items():
        src = cv2.imread(str(NEUMIS / f"{name}.png"), cv2.IMREAD_UNCHANGED)
        H, W = src.shape[:2]
        screen_mask, screen = screen_geometry(src)

        # erase the drawn face: bright pixels inside the (slightly shrunk) screen
        inner = cv2.erode(screen_mask, np.ones((15, 15), np.uint8))
        bright = (src[..., :3].max(axis=2) > 45).astype(np.uint8) & inner
        bright = cv2.dilate(bright, np.ones((15, 15), np.uint8)) & inner
        body = src.copy()
        body[..., :3] = cv2.inpaint(np.ascontiguousarray(src[..., :3]), bright, 7, cv2.INPAINT_TELEA)
        # pull the patched area back to the screen black so no ghost of the old face shows
        soft = cv2.GaussianBlur(bright.astype(np.float32), (21, 21), 0)[..., None]
        body[..., :3] = (body[..., :3] * (1 - 0.85 * soft)).astype(np.uint8)

        entries = []
        for i, arm in enumerate(arms):
            m = np.zeros((H, W), np.uint8)
            cv2.fillPoly(m, [np.array(arm["poly"], np.int32)], 1)
            layer = np.zeros_like(src)
            layer[m == 1] = src[m == 1]
            body[m == 1, 3] = 0
            cv2.imwrite(str(NEUMIS / f"{name}_arm{i}.png"), layer)
            entries.append({"src": f"neumis/{name}_arm{i}.png", "px": arm["pivot"][0], "py": arm["pivot"][1]})
        cv2.imwrite(str(NEUMIS / f"{name}_body.png"), body)
        rig[name] = {"w": W, "h": H, "body": f"neumis/{name}_body.png", "arms": entries,
                     "screen": {k: round(float(v), 1) for k, v in screen.items()}}
        print(name, rig[name]["screen"])
    (NEUMIS / "rig.json").write_text(json.dumps(rig, indent=2))


if __name__ == "__main__":
    main()
