#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

SUITS = ('S', 'H', 'C', 'D')
cards = dict()

for key in SUITS:
    cards[key] = [False for i in range(14)]

n = int(sys.stdin.readline())
for i in range(n):
    suit, rank_s = sys.stdin.readline().split()
    rank = int(rank_s)

    cards[suit][rank] = True

for suit in SUITS:
    for rank in range(1, 14):
        if cards[suit][rank] == False:
            print(suit, rank)
