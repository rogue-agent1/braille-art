#!/usr/bin/env python3
"""braille_art - Convert text to Braille Unicode patterns."""
import argparse, sys

BRAILLE_BASE = 0x2800
DOT_MAP = [(0,0,0x01),(0,1,0x08),(1,0,0x02),(1,1,0x10),(2,0,0x04),(2,1,0x20),(3,0,0x40),(3,1,0x80)]

def text_to_braille_dots(text):
    """Simple text-to-braille: each char maps to a braille cell."""
    result = ""
    for ch in text:
        o = ord(ch.lower())
        if ch == " ": result += chr(BRAILLE_BASE); continue
        if ord("a") <= o <= ord("z"):
            idx = o - ord("a")
            # Use first 6 dots for letter encoding (simplified)
            val = (idx + 1) & 0x3F
            result += chr(BRAILLE_BASE + val)
        else:
            result += ch
    return result

def matrix_to_braille(matrix, w, h):
    """Convert boolean matrix to braille characters."""
    lines = []
    for by in range(0, h, 4):
        line = ""
        for bx in range(0, w, 2):
            val = 0
            for dy, dx, bit in DOT_MAP:
                y, x = by + dy, bx + dx
                if y < h and x < w and matrix[y][x]:
                    val |= bit
            line += chr(BRAILLE_BASE + val)
        lines.append(line)
    return "\n".join(lines)

def wave_pattern(w, h):
    import math
    m = [[False]*w for _ in range(h)]
    for x in range(w):
        y = int((math.sin(x * 0.3) + 1) * (h - 1) / 2)
        if 0 <= y < h: m[y][x] = True
    return m

def main():
    p = argparse.ArgumentParser(description="Braille Unicode art")
    sub = p.add_subparsers(dest="cmd")
    t = sub.add_parser("text"); t.add_argument("text", nargs="+")
    w = sub.add_parser("wave"); w.add_argument("-W","--width",type=int,default=80); w.add_argument("-H","--height",type=int,default=24)
    a = p.parse_args()
    if a.cmd == "text": print(text_to_braille_dots(" ".join(a.text)))
    elif a.cmd == "wave": print(matrix_to_braille(wave_pattern(a.width,a.height),a.width,a.height))
    else: p.print_help()

if __name__ == "__main__": main()
