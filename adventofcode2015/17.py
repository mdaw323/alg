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

containers = []
for nr, line in enumerate(lines):
    containers.append(int(line))
containers.sort()
print(containers, len(containers))


for i in range(1 << 20):
    s = 0
    l = 0
    for j in range(20):
        if i & (1 << j):
            s+=containers[j]
            l+=1
    # print (i,s)
    if s == 150:
        dd[l]+=1
        p1+=1
print(p1, dd[min(dd)])
