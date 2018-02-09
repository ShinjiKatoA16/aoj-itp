#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

num = 0
while True:
    s = sys.stdin.readline().strip()
    if s == '0':
        break
    num += 1
    print('Case ', num, ': ', s, sep='')
