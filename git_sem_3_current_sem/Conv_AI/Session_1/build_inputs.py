"""Build notes_input/part_XX.md (+ slide images) from the lecture MP4 and VTT."""
import os
import re
import glob
import textwrap
import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VIDEO = glob.glob(os.path.join(HERE, "*.mp4"))[0]
VTT = glob.glob(os.path.join(HERE, "*.vtt"))[0]
OUT = os.path.join(HERE, "notes_input")
SLIDES = os.path.join(OUT, "slides")
SAMPLE_SEC = 2.0
DIFF_THRESH = 6.0      # mean abs diff (0-255) on 160x90 gray to call a slide change
MIN_SEG_SEC = 20       # shorter segments are merged into the previous one
PART_SEC = 15 * 60     # target length of one part


def fmt(t):
    t = int(t)
    return f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"


def parse_vtt():
    cues = []
    text = open(VTT, encoding="utf-8").read()
    pat = re.compile(r"(\d+):(\d+):(\d+\.\d+) --> [\d:.]+\s*\n(.*?)(?:\n\n|\Z)", re.S)
    for m in pat.finditer(text):
        start = int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])
        body = m[4]
        sp = re.search(r"<v ([^>]*)>", body)
        speaker = sp[1].strip(" .") if sp else ""
        line = re.sub(r"</?v[^>]*>", "", body).replace("\n", " ").strip()
        cues.append((start, speaker, line))
    cues.sort(key=lambda c: c[0])
    return cues


def detect_segments():
    cap = cv2.VideoCapture(VIDEO)
    fps = cap.get(cv2.CAP_PROP_FPS)
    step = int(round(fps * SAMPLE_SEC))
    idx, prev, seg_start = 0, None, 0.0
    segs, last_frame = [], None
    while True:
        ok = cap.grab()
        if not ok:
            break
        if idx % step == 0:
            ok, frame = cap.retrieve()
            if not ok:
                break
            t = idx / fps
            small = cv2.cvtColor(cv2.resize(frame, (160, 90)), cv2.COLOR_BGR2GRAY).astype(np.float32)
            if prev is not None and np.mean(np.abs(small - prev)) > DIFF_THRESH:
                segs.append([seg_start, t, last_frame])
                seg_start = t
            prev, last_frame = small, frame
        idx += 1
    segs.append([seg_start, idx / fps, last_frame])
    cap.release()

    merged = []
    for s in segs:
        if merged and s[1] - s[0] < MIN_SEG_SEC:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    return merged


def main():
    os.makedirs(SLIDES, exist_ok=True)
    cues = parse_vtt()
    segs = detect_segments()

    parts, cur, cur_start = [], [], None
    for i, (s, e, frame) in enumerate(segs, 1):
        name = f"slide_{i:03d}.jpg"
        cv2.imwrite(os.path.join(SLIDES, name), cv2.resize(frame, (1280, 720)), [cv2.IMWRITE_JPEG_QUALITY, 85])
        if cur_start is None:
            cur_start = s
        cur.append((i, s, e, name))
        if e - cur_start >= PART_SEC:
            parts.append(cur)
            cur, cur_start = [], None
    if cur:
        parts.append(cur)

    for p, segs_in_part in enumerate(parts, 1):
        lines = [f"# Part {p:02d}  [{fmt(segs_in_part[0][1])} - {fmt(segs_in_part[-1][2])}]\n"]
        for i, s, e, name in segs_in_part:
            lines.append(f"## Segment {i:03d}  [{fmt(s)} - {fmt(e)}]")
            lines.append(f"Slide: slides/{name}\n")
            last_sp = None
            buf = []
            for t, sp, txt in cues:
                if s <= t < e:
                    if sp != last_sp:
                        if buf:
                            lines.append(textwrap.fill(" ".join(buf), 400) + "\n")
                        buf = [f"**{sp}** [{fmt(t)}]:"]
                        last_sp = sp
                    buf.append(txt)
            if buf:
                lines.append(textwrap.fill(" ".join(buf), 400) + "\n")
        with open(os.path.join(OUT, f"part_{p:02d}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    print(f"{len(segs)} segments, {len(parts)} parts")


if __name__ == "__main__":
    main()
