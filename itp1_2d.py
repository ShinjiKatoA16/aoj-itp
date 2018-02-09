#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

w, h, x, y, r = map(int, sys.stdin.readline().split())

if x < r or (x+r) > w:
    print('No')
elif y < r or (y+r) > h:
    print('No')
else:
    print('Yes')
