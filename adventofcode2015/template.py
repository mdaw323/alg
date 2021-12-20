#!/usr/bin/python3

import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(10000)

filename = sys.argv[1] if len(sys.argv) > 1 else 'x.in'

dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE
p1 = p2 = 0

lines = [l.strip() for l in open(filename).read().split("\n")]

for nr, line in enumerate(lines):
    pass
