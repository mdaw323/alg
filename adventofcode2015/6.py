import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)

dd2 = defaultdict(lambda: 0)

dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

for nr in range(len(lines)):
    l = lines[nr]
    s = l.split()
    la, lb = map(int, s[-3].split(','))
    ra, rb = map(int, s[-1].split(','))

    for i in range(la,ra+1):
        for j in range(lb, rb+1):
            if s[0] == 'toggle':
                dd[(i,j)] ^= 1
                dd2[(i,j)] += 2
            elif s[1] == 'on':
                dd[(i,j)] = 1
                dd2[(i,j)] += 1
            elif s[1] == 'off':
                dd[(i,j)] = 0
                dd2[(i,j)] = max(0,dd2[(i,j)] -1)

print(sum(dd.values()))
print(sum(dd2.values()))
