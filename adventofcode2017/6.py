import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p = p2 = 0

ll = [l.strip() for l in fileinput.input()]

a = []
for i in range(len(ll)):
    l = ll[i]
    a = list(map(int,l.split()))
    print(a)

seen = set()
seen.add(tuple(a))

p = p1 = 0
part2 = False

while True:

    p+=1
    ma = max(a)

    i = a.index(ma)


    r = a[i]
    a[i] = 0
    # print ("r",r)
    # print (*a,i,r)
    for j in range(r):
        jj = (j + i + 1) % len(a)
        a[jj] += 1
        # k = r // (len(a) - j)
        # r -= k
        # if r > 0:
            # k+=1
            # r-=1
        # print("k",r, k,jj)
        # a[jj] += k

    # print(*a)
    if (tuple(a) in seen):
        if part2:
            break
        else:
            p1 = p
            p = 0
            seen = set()
            part2 = True
    seen.add(tuple(a))

print(p1, p)
