#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

w = sys.stdin.readline().strip().lower()

words = list()

while True:
    s = sys.stdin.readline().strip()
    if s == 'END_OF_TEXT':
        break
    words.extend(s.lower().split())

print(words.count(w))
