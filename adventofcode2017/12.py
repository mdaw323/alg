import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
adj = defaultdict(lambda: [])
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

for nr in range(len(lines)):
    l = lines[nr]
    a,b = l.split(' <-> ')
    a = int(a)
    adj[a].extend(list(map(int,b.split(','))))


seen = set()
def dfs(s):
    if s in seen:
        return 0
    seen.add(s)
    for v in adj[s]:
        dfs(v)
dfs(0)
print(len(seen))

groups = 1
for v in adj:
    if v not in seen:
        groups+=1
        dfs(v)
print(groups)
