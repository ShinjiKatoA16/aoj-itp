#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    n = int(sys.stdint.readline())
    if n == 0:
        break

    score = list(map(int, sys.stdin.readline().split()))
    ave = sum(score) / len(score)

    s2 = 0
    for v in score:
        s2 += (score-ave) ** 2
    print(s2 ** 0.5)
