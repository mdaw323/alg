import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)

dx = [0, 0, -1, 1,1,1,-1,-1]  # NSWE
dy = [-1, 1, 0, 0,1,-1,1,-1]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

N = len(lines)

dd = defaultdict(lambda:False)
corners = set([(0,0),(N-1,0), (N-1,N-1), (0,N-1)])
for i, line in enumerate(lines):
    for j,c in enumerate(line):
        dd[(i,j)] = (c == '#')
        if (i,j) in corners:
            dd[(i,j)] = True



def draw(step):
    print(step)
    for i in range(N):
        z =[]
        for j in range(N):
            z.append('#' if dd[(i,j)] else '.')
        print(*z,sep='')


for step in range(100):
    # draw(step)
    new_dd = defaultdict(lambda:False)
    is_on = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                cnt += 1 if dd[(x,y)] else 0
            new_dd[(i,j)] = dd[(i,j)] and (2<=cnt <=3) or ((not dd[(i,j)]) and cnt == 3)
            if (i,j) in corners:
                new_dd[(i,j)] = True
            is_on += 1 if new_dd[(i,j)] else 0
    dd = new_dd



print (is_on)
