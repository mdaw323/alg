import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

ll = [int(l.strip()) for l in fileinput.input()]

i = 0
while( 0<=i<len(ll)):
    l = ll[i]
    ll[i] += 1
    i += l
    p1 += 1


ll = [int(l.strip()) for l in fileinput.input()]

i = 0
while( 0<=i<len(ll)):
    l = ll[i]
    if l >= 3:
        ll[i] -= 1
    else:
        ll[i] += 1
    i += l
    p2 += 1

print(p1, p2)
