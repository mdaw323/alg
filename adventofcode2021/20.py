import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: '.')
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]  # NSWE
dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

enhanced = lines[0]


for nr in range(2, len(lines)):
    l = lines[nr]
    for i,c in enumerate(l):
        if c == '#':
            dd[(i, nr-2)] = c

def apply(default):
    global dd
    left= right= up= down = 0
    for x,y in dd:
        left = min(left,x)
        right = max(right,x)
        up = min(up,y)
        down = max(down,y)

    new_dd = defaultdict(lambda:default)
    for y in range(up-2, down+3):
        for x in range(left-2, right+3):
            s = ''
            for i in range(len(dx)):
                xx = x + dx[i]
                yy = y + dy[i]
                s += '1' if dd[(xx,yy)] == '#' else '0'
            new_dd[(xx,yy)] = enhanced[int(s,2)]
    dd = new_dd


apply('#')
apply('.')

print(list(dd.values()).count('#'))

for i in range(24):
    apply('#')
    apply('.')

print(list(dd.values()).count('#'))
