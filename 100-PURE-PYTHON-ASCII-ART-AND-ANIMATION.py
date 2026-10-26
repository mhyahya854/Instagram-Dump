#!/usr/bin/env python3
"""Pure-Python ASCII art: heart, sine waves and animated plasma (stdlib only).

No image model, Pillow, graphics library, network, or files are required.
Examples:
    python 100-PURE-PYTHON-ASCII-ART-AND-ANIMATION.py --mode heart
    python 100-PURE-PYTHON-ASCII-ART-AND-ANIMATION.py --mode waves
    python 100-PURE-PYTHON-ASCII-ART-AND-ANIMATION.py --mode plasma --frames 60 --fps 15
"""
import argparse
import math
import sys
import time

DENSITY = " .:-=+*#%@"


def pixel(mode: str, x: float, y: float, t: float) -> str:
    """Return one ASCII character for normalized coordinates."""
    if mode == "heart":
        # x, y in approximately [-1.5, 1.5]. 2:1 terminal glyph proportions
        xx, yy = x * 1.25, y * 1.10
        inside = (xx * xx + yy * yy - 1) ** 3 - (xx * xx) * (yy ** 3) <= 0
        if not inside:
            return " "
        brightness = 0.5 + 0.5 * math.sin(10 * xx + 5 * yy + t * 2)
        return DENSITY[4 + min(5, int(brightness * 5))]
    if mode == "waves":
        wave = math.sin(8 * x + t * 2.4) * 0.34 + math.cos(5 * x - t) * 0.12
        distance = abs(y - wave)
        if distance < 0.055:
            return "@"
        if distance < 0.12:
            return "+"
        return " "
    if mode == "plasma":
        value = (
            math.sin(5 * x + t)
            + math.sin(4 * y - t * 0.7)
            + math.sin(4 * (x + y) + t * 0.6)
        ) / 3
        index = round((value + 1) / 2 * (len(DENSITY) - 1))
        return DENSITY[max(0, min(index, len(DENSITY) - 1))]
    raise ValueError("Unsupported mode")


def render(mode: str, width: int, height: int, t: float) -> str:
    lines = []
    for row in range(height):
        y = (0.5 - (row + 0.5) / height) * 2.6
        chars = []
        for col in range(width):
            x = ((col + 0.5) / width - 0.5) * 3.0
            chars.append(pixel(mode, x, y, t))
        lines.append("".join(chars).rstrip())
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", choices=("heart", "waves", "plasma"), default="heart")
    ap.add_argument("--width", type=int, default=72)
    ap.add_argument("--height", type=int, default=28)
    ap.add_argument("--frames", type=int, default=1)
    ap.add_argument("--fps", type=float, default=15)
    args = ap.parse_args()
    if not (10 <= args.width <= 200 and 6 <= args.height <= 70):
        ap.error("width must be 10..200 and height 6..70")
    if not (1 <= args.frames <= 1000 and 1 <= args.fps <= 60):
        ap.error("frames must be 1..1000 and fps 1..60")
    animated_terminal = args.frames > 1 and sys.stdout.isatty()
    try:
        for frame in range(args.frames):
            picture = render(args.mode, args.width, args.height, frame / args.fps)
            if animated_terminal:
                sys.stdout.write("\x1b[H\x1b[2J")  # terminal-only ANSI clear
            elif frame:
                sys.stdout.write("\n--- FRAME %d ---\n" % (frame + 1))
            sys.stdout.write(picture)
            sys.stdout.flush()
            if frame + 1 < args.frames:
                time.sleep(1 / args.fps)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
