import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0
# n = '111221'
n = '1321131112'
for step in range(50):
    prev = None
    cnt = 0
    say = []
    for i, c in enumerate(n):
        if c == prev or prev == None:
            prev = c
            cnt += 1
        else:
            say.append(str(cnt))
            say.append(prev)
            prev = c
            cnt = 1
    say.append(str(cnt))
    say.append(prev)

    n = ''.join(say)
    if step == 39:
        p1 = len(n)
print(p1, len(n))
