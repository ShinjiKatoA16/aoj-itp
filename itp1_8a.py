#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from string import ascii_lowercase as asc_l, ascii_uppercase as asc_u

table = str.maketrans(asc_l+asc_u, asc_u+asc_l)

s = sys.stdin.readline()
print(s.translate(table), end='')
