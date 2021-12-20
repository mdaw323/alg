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

lines = [l.strip() for l in open(filename).readlines()]

numbers = set()
for line in lines:
    numbers.add(int(line))


def prod(x):
    r = 1
    for y in x:
        r*=y
    return r

def solve(groups):
    results = []
    mid = sum(numbers)//groups

    for i in range(4,7):
        for n in combinations(numbers,i):
            if sum(n) == mid:
                results.append((prod(n), n))

    for p, n in sorted(results):
        rest = numbers - set(n)
        for i in range(4,10):
            for k in combinations(rest,i):
                if sum(k) == mid:
                    return p


print(solve(3), solve(4))
