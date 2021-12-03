import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

ll = [l.strip() for l in fileinput.input()]

for i in range(len(ll)):
    l = ll[i]
    pp = l.split()
    ppset = set()
    pp2 = set()
    for w in pp:
        ppset.add(w)
        pp2.add("".join(sorted(w)))
    if len(pp) == len(ppset):
        p1 += 1
    if len(pp) == len(pp2):
        p2 += 1


print(p1, p2)
