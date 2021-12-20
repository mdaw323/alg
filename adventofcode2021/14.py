import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from typing import Counter
from functools import lru_cache
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: '')
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]
template = ''
for nr in range(len(lines)):
    line = lines[nr]
    if nr ==0:
        template = line
    elif line:
        l,r = line.split(' -> ')
        dd[l] = r

print(template)
mem = {}

@lru_cache(maxsize=None)
def f(a,b,depth) -> Counter:
    if depth == 0:
        return Counter([a,b])
    else:
        k = dd[a+b]
        cnt = f(a, k, depth-1)+ f(k, b, depth-1)
        cnt[k] -= 1
        return cnt

steps = 40

c = Counter()
for i in range(len(template) -1):
    c+=f(template[i], template[i+1], steps)

for i in range(len(template) -2):
    c[template[i+1]]-=1

# print (c)
cc = c.most_common()
print(cc[0][1] - cc[-1][1])
