#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

a, b = map(int, sys.stdin.readline().split())
print(a//b, a%b, round(a/b, 6))
