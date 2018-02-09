#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    a, op, b = sys.stdin.readline().split()
    ai = int(a)
    bi = int(b)
    if op == '?':
        break
    elif op == '+':
        print(ai + bi)
    elif op == '-':
        print(ai - bi)
    elif op == '*':
        print(ai * bi)
    elif op == '/':
        print(ai // bi)
    else:
        raise ValueError


