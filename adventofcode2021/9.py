import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: -1)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

n = len(lines)
m = len(lines[0])

for ii in range(len(lines)):
    l = lines[ii]
    for jj, k in enumerate(l):
        dd[(ii,jj)] = int(k)

# print (dd)

low_points = []

for i in range(n):
    for j in range(m):
        level = dd[(i,j)]
        low_point = True
        for k in range(4):
            ii = i + dx[k]
            jj = j + dy[k]
            if dd[(ii,jj)]>= 0 and dd[(ii,jj)] <= level:
                low_point = False

        if low_point:
            low_points.append((i,j))
            p1+=level+1

seen = set()
def bfs(sx,sy):
    q = deque()
    q.appendleft((1,sx,sy))

    d = 1
    cnt = 0
    while (len(q) > 0):
        d, x, y = q.pop()
        level = dd[(x,y)]
        if ((x,y) in seen):
            continue
        else:
            cnt += 1
            seen.add((x,y))
        for k in range(4):
            ii = x + dx[k]
            jj = y + dy[k]
            if (dd[(ii,jj)]>= 0) and (dd[(ii,jj)] > level) and (dd[(ii,jj)]<9):
                q.appendleft( (d+1,ii,jj))

    return cnt

p2 = 1
basins = []
for x,y in low_points:
    b = bfs(x,y)
    basins.append(b)

basins.sort()

for b in basins[-3:]:
    p2 *= b
print(p1, p2)
