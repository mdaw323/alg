import fileinput
from os import sep
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = None

lines = [l.strip() for l in fileinput.input()]

M = 0
N = 0

points = set()


def foldx(fold_x):
    global M
    global N
    for x, y in list(points):
        if x == fold_x:
            points.discard((x, y))
        elif x > fold_x:
            points.discard((x, y))
            xx = fold_x - (x - fold_x)
            points.add((xx, y))
    M = fold_x


def foldy(fold_y):
    global M
    global N

    for x, y in list(points):
        if y == fold_y:
            points.discard((x, y))
        elif y > fold_y:
            points.discard((x, y))
            yy = fold_y - (y - fold_y)
            points.add((x, yy))
    N = fold_y


def wypisz():
    for y in range(N):
        line = []
        for x in range(M):
            line.append('#' if (x, y) in points else '.')
        print(*line, sep='')


for line in lines:

    if not line:
        pass
    elif line.startswith('fold'):

        _, _, f = line.split()
        l, r = f.split('=')
        r = int(r)
        if l == 'x':
            foldx(r)
        elif l == 'y':
            foldy(r)
        p1 = len(points) if p1 == None else p1
        # print()
        # break
    else:
        x, y = map(int, line.split(','))
        M = max(M, x+1)
        N = max(N, y+1)
        points.add((x, y))

print(p1)
wypisz()
