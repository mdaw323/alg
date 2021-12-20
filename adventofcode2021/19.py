import fileinput
import sys
import math
from functools import lru_cache
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from typing import Sequence
sys.setrecursionlimit(10000000)

dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]
nr = 0
scanner = defaultdict(lambda: [])
trans = defaultdict(lambda: defaultdict(lambda: []))


def dist(a, b):
    d = 0
    for i in range(3):
        d += (a[i] - b[i]) * (a[i] - b[i])
    return d

def vec(a, b):
    return (b[0] - a[0], b[1] - a[1], b[2] - a[2])

def add_vec(a,b):
    return (b[0] + a[0], b[1] + a[1], b[2] + a[2])


dd = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: set())))

trmap = {0: 0}
trvec = {0: (0, 0, 0)}


tr = [
    (1, 2, 3),
    (1, 3, -2),
    (1, -3, 2),
    (1, -2, -3),
    (2, -3, -1),
    (2, -1, 3),
    (2, 1, -3),
    (2, 3, 1),
    (3, -2, 1),
    (3, -1, -2),
    (3, 1, 2),
    (3, 2, -1),
    (-3, -2, -1),
    (-3, -1, 2),
    (-3, 1, -2),
    (-3, 2, 1),
    (-2, -3, 1),
    (-2, -1, -3),
    (-2, 1, 3),
    (-2, 3, -1),
    (-1, -3, -2),
    (-1, -2, 3),
    (-1, 2, -3),
    (-1, 3, 2),
]

SUCCESS = 12

# print(tr)


def transform_points(a, id):
    b = []
    for u in a:
        v = [0, 0, 0]
        x, y, z = tr[id]
        n = [1 if x > 0 else -1, 1 if y > 0 else -1, 1 if z > 0 else -1]
        xx = abs(x)-1
        yy = abs(y)-1
        zz = abs(z)-1
        t = [xx, yy, zz]
        for i in range(3):
            v[i] = n[i] * u[t[i]]
        b.append(tuple(v))
    return b

def move_by_vector(points,v):
    result = []
    for p in points:
        result.append(add_vec(p,v))
    return result

def transform_and_move(a, id, v):
    points = transform_points(a,id)
    result = []
    for p in points:
        result.append(add_vec(p,v))
    return result


def compare(sc_a, sc_b, t_a, t_b):
    # assert scanner[sc_a] == transform_points(scanner[sc_a], t_a)
    points_a = transform_points(scanner[sc_a], t_a)
    points_b = transform_points(scanner[sc_b],t_b)
    s = set(points_a)
    for a in range(len(points_a)):
        for b in range(len(points_b)):
            v = vec(points_b[b], points_a[a])
            np = move_by_vector(points_b,v)

            if len(s & set(np)) >= SUCCESS:
                return v
    return None


for line in lines:
    if not line:
        continue

    if line.startswith('---'):
        s = line.split()
        nr = int(s[2])
    else:
        s = line.split(',')
        scanner[nr].append(tuple(map(int, s)))

q = deque()
q.appendleft(0)

scanners = [(0,0,0)]

seen = set([0])
while q:
    i = q.pop()
    for j in range(len(scanner)):
        if i == j or j in seen:
            continue
        for t in range(len(tr)):
            res = compare(i,j,0,t)
            if res:
                scanners.append(res)
                seen.add(j)
                q.appendleft(j)
                scanner[j] = transform_and_move(scanner[j], t, res)



all_points = set()
for sc in range(len(scanner)):
    for p in scanner[sc]:
        all_points.add(p)

print(len(all_points))


def md(a,b):
    return abs(a[0] - b[0] ) + abs(a[1] - b[1] ) + abs(a[2] - b[2] )

ddist = []
for a,b in combinations(scanners, 2):
    ddist.append(md(a,b))

print(max(ddist))
