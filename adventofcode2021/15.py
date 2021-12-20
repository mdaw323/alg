import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from heapq import *
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

M = len(lines)
N = len(lines[0])


for i, line in enumerate(lines):
    for j, c in enumerate(line):
        dd[(i, j)] = int(c)

for ii in range(5):
    for jj in range(5):
        for i in range(M):
            for j in range(N):
                k = (dd[(i, j)] + ii+jj - 1) % 9 + 1
                dd[(i+(ii*M), j + (jj*N))] = k


def dijkstra(sx, sy, N, M):
    visited = set()
    q = []
    distance = defaultdict(lambda: 9999999)
    distance[(sx, sy)] = 0
    heappush(q, (0, sx, sy))
    while len(q) > 0:
        _, x, y = heappop(q)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if (0 <= xx < N) and (0 <= yy < M) and distance[(xx, yy)] > distance[(x, y)] + dd[(xx, yy)]:
                distance[(xx, yy)] = distance[(x, y)] + dd[(xx, yy)]
                heappush(q, (distance[(xx, yy)], xx, yy))
    return distance


distance = dijkstra(0, 0, N, M)
print(distance[(M-1, N-1)])

distance = dijkstra(0, 0, 5*N, 5*M)
print(distance[(5*M-1, 5*N-1)])
