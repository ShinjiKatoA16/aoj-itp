#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import math

r = float(sys.stdin.readline())
area = round(math.pi * (r**2), 6)
circum = round(2 * r * math.pi, 6)
print(area, circum)
