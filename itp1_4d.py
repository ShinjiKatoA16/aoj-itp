#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

print(min(x), max(x), sum(x))
