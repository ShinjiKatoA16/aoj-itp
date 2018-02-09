#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    n, x = map(int, sys.stdin.readline().split())
    if n == 0 and x == 0:
        break

    combi = 0
    for a in range(1, n-1):
        for b in range(a+1, n): # b > a
            c = x - a - b
            if c <= b:  # c must be > b
                break
            if c > n:
                continue
            # print(a, b, c)
            combi += 1

    print(combi)

