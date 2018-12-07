#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    s = sys.stdin.readline().strip()
    if s == '0':
        break
    print(sum(map(int, s)))
