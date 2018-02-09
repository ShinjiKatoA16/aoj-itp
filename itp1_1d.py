#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

s = int(sys.stdin.readline())
second = s % 60
minutes = (s // 60) % 60
hour = s // 3600

print(hour, minutes, second, sep=':')
