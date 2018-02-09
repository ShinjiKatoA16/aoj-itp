#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

tenant = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

n = int(sys.stdin.readline())
for i in range(n):
    b, f, r, v = map(int, sys.stdin.readline().split())
    tenant[b-1][f-1][r-1] += v

separator = '#' * 20
for b in range(4):
    for f in range(3):
        for r in range(10):
            print(' ', tenant[b][f][r], sep='', end='')
        print()
    if b != 3:
        print(separator)
