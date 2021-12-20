import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE



lines = [l.strip() for l in fileinput.input()]


p1 = 0
p2 = []

expected = {')': '(', ']': '[', '}': '{', '>': '<'}
score_p1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
score_p2 = {'(': 1, '[': 2, '{': 3, '<': 4}

for nr, l in enumerate(lines):
    de = []
    incomplete = True
    for c in l:
        if c in '([{<':
            de.append(c)
        else:
            z = de.pop()
            if z != expected[c]:
                p1 += score_p1[c]
                incomplete = False
                break

    if incomplete:
        s = 0
        while(len(de) > 0):
            x = de.pop()
            s = s*5 + score_p2[x]
        p2.append(s)

print(p1, sorted(p2)[len(p2)//2])
