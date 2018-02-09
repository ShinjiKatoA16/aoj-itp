#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
str_num = list(map(str, numbers))

print(' '.join(str_num))
