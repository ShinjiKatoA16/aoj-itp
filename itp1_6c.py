#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

tenant = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

n = int(sys.stdin.readline())
for i in range(n):
    b, f, r, v = map(int, sys.stdin.readline().split())
    tenant[b-1][f-1][r-1] += v

ROOM_STR = '{:2}' * 10  # width:2 10 rooms
separator = '#' * 20
for b in range(4):
    for f in range(3):
        print(ROOM_STR.format(*tenant[b][f]))  # unpack list of 10 elements
    if b != 3:
        print(separator)
