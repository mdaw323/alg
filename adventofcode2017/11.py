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
# lines = ['se,sw,se,sw,sw']

steps = lines[0].split(',')

m = {
    'n' : (0,-2),
    's' : (0, 2),
    'nw' : (-1, -1),
    'ne' : (1, -1),
    'sw' : (-1, 1),
    'se' : (1, 1),
}

maxd = 0

x = y = 0
for s in steps:
    xx,yy = m[s]
    x += xx
    y += yy
    d = min(abs(x),abs(y))
    d += (abs(y)-d) // 2 + (abs(x)-d)
    maxd = max(maxd, d)

x = abs(x)
y = abs(y)


d = min(x,y)
d += (y-d) // 2 + (x-d)


print(d, maxd)
