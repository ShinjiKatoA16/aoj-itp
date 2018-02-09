#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

a, b = map(int, sys.stdin.readline().split())

if a == b:
    print('a == b')
elif a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    raise Exception('logic error')
