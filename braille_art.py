#!/usr/bin/env python3
"""Convert text to Braille unicode."""
import sys

BRAILLE = {
    'a':'⠁','b':'⠃','c':'⠉','d':'⠙','e':'⠑','f':'⠋','g':'⠛','h':'⠓','i':'⠊','j':'⠚',
    'k':'⠅','l':'⠇','m':'⠍','n':'⠝','o':'⠕','p':'⠏','q':'⠟','r':'⠗','s':'⠎','t':'⠞',
    'u':'⠥','v':'⠧','w':'⠺','x':'⠭','y':'⠽','z':'⠵',
    '1':'⠂','2':'⠆','3':'⠒','4':'⠲','5':'⠢','6':'⠖','7':'⠶','8':'⠦','9':'⠔','0':'⠴',
    ' ':'⠀','.':'⠨',',':'⠠','!':'⠮','?':'⠹','-':'⠤'
}

def to_braille(text):
    return ''.join(BRAILLE.get(c, c) for c in text.lower())

def from_braille(text):
    rev = {v: k for k, v in BRAILLE.items()}
    return ''.join(rev.get(c, c) for c in text)

if __name__ == '__main__':
    if len(sys.argv) < 2: print("Usage: braille_art.py [--decode] <text>"); sys.exit(1)
    if sys.argv[1] == '--decode':
        print(from_braille(' '.join(sys.argv[2:])))
    else:
        print(to_braille(' '.join(sys.argv[1:])))
