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


ans = []
for i in range(250):
    y = 0
    yy = i
    maxy = 0
    while y >=-159:
        y += yy
        maxy = max(maxy,y)
        if (-159<=y<=-121 ):
            ans.append(maxy)
        yy -=1


print(sorted(ans)[-1])

ans = []
for j in range(126):
    for i in range(-159,250):
        y = 0
        x = 0
        yy = i
        xx = j
        while y >=-159:
            y += yy
            x+=xx
            if (-159<=y<=-121) and (70<=x<=125 ) :
                ans.append((i,j,x,y))
                break
            yy -=1
            xx -= 1
            if (xx < 0):
                xx = 0

print(len(ans))
