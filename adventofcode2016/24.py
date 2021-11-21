import fileinput
from collections import deque

lines = [f.strip() for f in fileinput.input()]
m = [[c for c in l] for l in lines]

start = None
expected_state = 0


for i, x in enumerate(m):
    for j, c in enumerate(x):
        if '0' <= c <= '9':
            p = (i, j)
            expected_state |= 1 << int(c)
            if c == '0':
                start = p

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

seen = set()
q = deque()
q.appendleft((0, start, 0))

part1 = None

while len(q) > 0:
    dist, pos, state = q.pop()
    x, y = pos
    if '0' <= m[x][y] <= '9':
        state |= 1 << int(m[x][y])
    ret = (state == expected_state)
    if ret and m[x][y] == '0':
        part2 = dist
        break
    if ret and part1 == None:
        part1 = dist
    if (pos, state) in seen:
        continue
    seen.add((pos, state))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if m[nx][ny] != '#':
            q.appendleft((dist + 1, (nx,ny), state))

print (part1, part2)
