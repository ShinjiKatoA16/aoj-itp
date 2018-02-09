#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

a, b, c = map(int, sys.stdin.readline().split())

if a < b and b < c:
    print('Yes')
else:
    print('No')
