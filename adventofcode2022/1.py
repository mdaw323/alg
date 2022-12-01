import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement


p1 = []
s = 0
for l in fileinput.input():
    if not l.strip():
        p1.append(s)
        s = 0
    else:
        s+=int(l.strip())
p1.append(s)

print(max(p1), sum(sorted(p1)[-3:]))
