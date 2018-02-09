#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    h, w = map(int, sys.stdin.readline().split())
    if h == 0  and w == 0:
        break

    line = '#' * w
    for row in range(h):
        print(line)
    print()
