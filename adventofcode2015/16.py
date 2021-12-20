import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: None)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

valid = {'children': 3,
         'cats': 7,
         'samoyeds': 2,
         'pomeranians': 3,
         'akitas': 0,
         'vizslas': 0,
         'goldfish': 5,
         'trees': 3,
         'cars': 2,
         'perfumes': 1}

for nr, line in enumerate(lines):
    _, sue, *p = line.split()
    sue = int(sue[:-1])
    names = [p[0][:-1], p[2][:-1], p[4][:-1]]
    values = list(map(int, [p[1][:-1], p[3][:-1], p[5]]))
    qualified = True
    q2 = True
    for n, v in zip(names, values):
        if valid[n] != v:
            qualified = False
        if n in ['cats', 'trees']:
            q2 = q2 and v > valid[n]
        elif n in ['pomeranians', 'goldfish']:
            q2 = q2 and v < valid[n]
        elif valid[n] != v:
            q2 = False
    if qualified:
        p1 = sue
    if q2:
        p2 = sue


print(p1, p2)
