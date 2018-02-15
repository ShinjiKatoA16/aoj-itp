#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import math

a, b, c = map(float, sys.stdin.readline().split())
radian = c*math.pi / 180

height = abs(b * math.sin(radian))
pos_x = b * math.cos(radian)
edge_x = (height**2 + (pos_x-a)**2) ** 0.5

print(round(a * height / 2, 6))
print(round(a + b + edge_x, 6))
print(round(height, 6))
