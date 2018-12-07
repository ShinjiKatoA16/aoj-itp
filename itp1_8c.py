#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from string import ascii_lowercase
from collections import Counter

in_lines = ''.join(sys.stdin.readlines())
counts = Counter(in_lines.lower())

for key in ascii_lowercase:
    print(key, ':', counts[key])
