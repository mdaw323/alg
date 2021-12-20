import fileinput
import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]
g = defaultdict(lambda: [])
wg = {}
not_root = set()
for nr in range(len(lines)):
    l = lines[nr]
    s = l.split(' -> ')
    pr, v = s[0].split()
    wg[pr] = int(v[1:-1])
    if len(s) == 2:
        adj = [x.strip() for x in s[1].split(',')]
        not_root |= set(adj)
        g[pr] = adj
    else:
        g[pr] = []

ws = {}


def dfs(x):
    global p2
    w = 0
    if len(g[x]) > 0:
        vv = [dfs(v) for v in g[x]]
        minvv = min(vv)
        maxvv = max(vv)
        if minvv != maxvv:
            to_change = maxvv
            correct = minvv
            c = Counter(vv)
            if (c[minvv] < c[maxvv]):
                to_change = minvv
                correct = maxvv

            for weight, el in zip(vv, g[x]):
                if weight == to_change:
                    change = correct - to_change
                    wg[el] = wg[el] + change
                    p2 = wg[el]
            vv = [dfs(v) for v in g[x]]

        w = sum(vv)
    ws[x] = w + wg[x]
    return ws[x]


root = list(set(g.keys()) - not_root)[0]

dfs(root)
print(root, p2)
