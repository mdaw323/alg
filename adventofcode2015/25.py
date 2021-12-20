#!/usr/bin/python3

import itertools
import sys
from copy import deepcopy
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(10000)

filename = sys.argv[1] if len(sys.argv) > 1 else '24.in'

dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE
p1 = p2 = 0

row = 2978
col = 3083

s = 20151125
for i in range(1,10000):
    for j in range(1,i+1):
        if i == 1 and j == 1:
            continue
        c = j
        r = i-(j-1)
        s = s*252533 % 33554393
        if r == row and c == col:
            print(r,c, s)
            break
