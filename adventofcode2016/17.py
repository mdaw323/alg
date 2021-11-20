import hashlib
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dp = ['U', 'D', 'L', 'R']

salt = 'pvhmgsws'

open_doors = set('bcdef')

def moves(path:str, x, y):
    # U,D,L,R
    doors = hashlib.md5((salt + path).encode()).hexdigest()[:4]
    res = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx <= 3) and (0 <= ny <= 3) and (doors[i] in open_doors):
            res.append((path + dp[i], nx, ny))
    return res

d = deque()
d.appendleft( ('', 0,0))

p1 = p2 = None
while len(d)>0:
    p,x,y = d.pop()
    if (x,y) == (3,3):
        if p1 == None:
            p1 = p
        p2 = len(p)

        continue
    for z in moves(p,x,y):
        d.appendleft(z)

print(p1,p2)