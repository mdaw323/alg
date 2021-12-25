import fileinput
import sys
from copy import deepcopy
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]
M = {}
lx = ly = 0
for y in range(len(lines)):
    l = lines[y]
    ly = max(ly,y+1)
    for x,c in enumerate(l):
        lx = max(lx,x+1)
        M[(x,y)] = c


print(lx,ly)

def pr():
    for y in range(ly):
        s = ''
        for x in range(lx):
            s+=M[(x,y)]
        print(s)
    print()

pr()

step = 0
moves = 1
while (moves > 0):
    step +=1
    moves = 0
    M2 = deepcopy(M)
    for y in range(ly):
        for x in range(lx):
            xx = (x+1) % lx
            if M[(x,y)] == '>' and M[(xx,y)] == '.':
                M2[(xx,y)] = '>'
                M2[(x,y)] = '.'
                moves +=1
    M = M2
    M2 = deepcopy(M)
    for x in range(lx):
        for y in range(ly):
            yy = (y+1) % ly
            if M[(x,y)] == 'v' and M[(x,yy)] == '.':
                M2[(x,yy)] = 'v'
                M2[(x,y)] = '.'
                moves +=1
    M = M2
    print(step, moves)

    # if step == 1: break
pr()
print(step)
