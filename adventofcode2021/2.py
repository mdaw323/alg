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

hp = de1 = de2 = aim = 0
for i in range(len(ll)):
    l = ll[i]
    a, b = l.split()
    b = int(b)
    if a == 'forward':
        hp += b
        de2 += aim * b
    elif a == 'down':
        aim += b
        de1 += b
    elif a == 'up':
        aim -= b
        de1 -= b


print(hp * de1, hp * de2)
