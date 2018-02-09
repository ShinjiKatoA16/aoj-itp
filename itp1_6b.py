#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class suits():
    def __init__(self, symbol):
        self.exist = [False for i in range(14)]
        self.symbol = symbol

    def mark_exist(self, rank):
        self.exist[rank] = True

    def is_exist(self, rank):
        return self.exist[rank]

spade = suits('S')
heart = suits('H')
club = suits('C')
diamond = suits('D')

n = int(sys.stdin.readline())
for i in range(n):
    suit, rank_s = sys.stdin.readline().split()
    rank = int(rank_s)
    if suit == 'S':
        spade.mark_exist(rank)
    elif suit == 'H':
        heart.mark_exist(rank)
    elif suit == 'C':
        club.mark_exist(rank)
    elif suit == 'D':
        diamond.mark_exist(rank)
    else:
        raise ValueError

for s in (spade, heart, club, diamond):
    for rank in range(1, 14):
        if s.is_exist(rank) == False:
            print(s.symbol, rank)
