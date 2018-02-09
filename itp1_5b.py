#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    h, w = map(int, sys.stdin.readline().split())
    if h == 0  and w == 0:
        break

    top_btm = '#' * w
    mid = '#' + ('.' * (w-2)) + '#'
    print(top_btm)
    for row in range(h-2):
        print(mid)
    print(top_btm)
    print()
