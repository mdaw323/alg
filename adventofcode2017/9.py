import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

garbage = False
ignored = False
group = 0
for nr in range(len(lines)):
    l = lines[nr]
    for c in l:
        if ignored:
            ignored = False
            continue

        if c == '!':
            ignored = True
        elif c == '>':
            garbage = False
        elif garbage:
            p2+=1
            # pass
        elif c == '<':
            garbage = True
        elif c == '{':
            group += 1
        elif c == '}':
            p1 += group
            group -= 1

print (p1, p2)
