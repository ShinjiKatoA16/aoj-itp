#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

side = ((2-1, 3-1, 5-1, 4-1), (6-1, 3-1, 1-1, 4-1), (1-1, 2-1, 6-1, 5-1),
        (1-1, 5-1, 6-1, 2-1), (1-1, 3-1, 6-1, 4-1), (5-1, 3-1, 2-1, 4-1))

def check_rotate(face1, face2, f2_index):
    f1_bot = face1[5]
    if face2[5-f2_index] != f1_bot:
        return False
    f2_side_index = side[f2_index] * 2
    f2_side = [face2[f2_side_index[i]] for i in range(len(f2_side_index))]
    f1_side = [face1[i] for i in (2-1, 3-1, 5-1, 4-1)]
    # print(f1_side, f2_side)

    for i in range(4):
        if f1_side == f2_side[i:i+4]:
            return True

    return False

def check_ident(face1, face2):
    f1_top = face1[0]
    for index in range(len(face2)):
        if face2[index] == f1_top:
            if check_rotate(face1, face2, index):
                return True

    return False


face1 = sys.stdin.readline().split()
face2 = sys.stdin.readline().split()

if check_ident(face1, face2):
    print('Yes')
else:
    print('No')
