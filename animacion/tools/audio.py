"""Build the voice track and the timeline that index.html follows.

Each clip is trimmed of edge silence, sped up by TEMPO (pitch kept), and loudness-normalized,
then laid out one after another. Writes:
  audio/NN_<who>.wav   processed clips
  audio/voices.wav     the full voice track for the video
  audio/timeline.json  scene bounds, subtitle times and a per-frame loudness envelope (mouth sync)

Usage: python3 animacion/tools/audio.py <clip1> <clip2> ... (in scene order, see CLIPS)
"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "audio"
TEMPO = 1.1
RATE = 48000
FPS = 30
LEAD, GAP, OUTRO = 0.5, 0.25, 2.2

# One entry per clip, in scene order. `lines` splits a clip into subtitles at a pause
# (seconds into the original clip, before trimming and speed-up).
CLIPS = [
    {"who": "Mafe", "lines": [(None, "NEUMA means breath. And Human Practices is the heart of our project.")]},
    {"who": "Sal", "lines": [(None, "We interviewed 25 specialists at two public hospitals in Puebla: IMSS’s La Margarita and ISSSTE.")]},
    {"who": "Sus", "lines": [(5.5, "We heard the same thing again and again: lung cancer is found late."),
                             (None, "A “little cough” nobody suspects, months of waiting…")]},
    {"who": "Ann", "lines": [(None, "…and someone who puts off the doctor because if they don’t work, their family doesn’t eat.")]},
    {"who": "Mafe", "lines": [(5.7, "It’s not that people don’t care: a system fails them long before they reach a hospital."),
                              (None, "We call this the diagnosis culture.")]},
    {"who": "Sal", "lines": [(7.9, "That’s why NEUMA is triage, not a verdict: a questionnaire screens first, and the test is ordered at the second level."),
                             (None, "The result comes with clear next steps, careful words and family by your side.")]},
    {"who": "All", "lines": [(None, "This is not our final breath. Because in lung cancer, every hour counts.")]},
]


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


def lead_silence(path):
    """Seconds of silence at the start of a clip."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(path), "-af", "silencedetect=noise=-40dB:d=0.05", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    starts = [float(l.split("silence_start: ")[1]) for l in r.splitlines() if "silence_start" in l]
    ends = [float(l.split("silence_end: ")[1].split()[0]) for l in r.splitlines() if "silence_end" in l]
    return ends[0] if starts and starts[0] < 0.01 and ends else 0.0


def read_wav(path):
    with wave.open(str(path)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768


def main(files):
    assert len(files) == len(CLIPS), f"expected {len(CLIPS)} clips"
    OUT.mkdir(exist_ok=True)
    trim = "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,areverse," \
           "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,areverse"
    t, scenes, lines, placed = LEAD, [], [], []
    for i, (src, clip) in enumerate(zip(files, CLIPS)):
        cut = lead_silence(src)
        dst = OUT / f"{i + 1:02d}_{clip['who'].lower()}.wav"
        ffmpeg("-i", src, "-af", f"{trim},atempo={TEMPO},loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(RATE), "-ac", "1", str(dst))
        dur = len(read_wav(dst)) / RATE
        start, end = t, t + dur
        scenes.append([0 if i == 0 else round(start - GAP, 3), round(end + GAP, 3)])
        prev = start
        for split, text in clip["lines"]:
            stop = end if split is None else start + max(0.0, split - cut) / TEMPO
            lines.append({"who": clip["who"], "a": round(prev, 3), "b": round(stop, 3), "text": text})
            prev = stop
        placed.append((dst, start))
        t = end + 2 * GAP
    duration = round(placed[-1][1] + len(read_wav(placed[-1][0])) / RATE + OUTRO, 3)
    scenes[-1][1] = duration

    track = np.zeros(int(duration * RATE), np.float32)
    for dst, start in placed:
        x = read_wav(dst)
        i0 = int(start * RATE)
        track[i0:i0 + len(x)] += x[: len(track) - i0]
    with wave.open(str(OUT / "voices.wav"), "wb") as w:
        w.setnchannels(1), w.setsampwidth(2), w.setframerate(RATE)
        w.writeframes((np.clip(track, -1, 1) * 32767).astype(np.int16).tobytes())

    hop = RATE // FPS
    rms = np.sqrt(np.convolve(track ** 2, np.ones(hop) / hop, "same"))[::hop]
    env = np.clip(rms / (np.percentile(rms[rms > 0.01], 90) + 1e-6), 0, 1)
    timeline = {"duration": duration, "fps": FPS, "scenes": scenes, "lines": lines,
                "speechEnd": round(placed[-1][1] + len(read_wav(placed[-1][0])) / RATE, 3),
                "env": [round(float(v), 2) for v in env]}
    (OUT / "timeline.json").write_text(json.dumps(timeline, ensure_ascii=False))
    print(json.dumps({k: v for k, v in timeline.items() if k != "env"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
