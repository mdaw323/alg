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

a = []
for i in range(len(ll)):
    l = ll[i]
    a = list(map(int,l.split()))
    print(a)

seen = set()
seen.add(tuple(a))
print(*a)
while True:

    p1+=1
    ma = max(a)

    i = a.index(ma)

    # print (ma,i,r)
    r = a[i]
    a[i] = 0
    print ("r",7)
    for j in range(len(a)):
        jj = (j + i + 1) % len(a)
        k = r // (len(a) - j)
        r -= k
        if r > 0:
            k+=1
            r-=1
        print("k",r, k,jj)
        a[jj] += k

    print(*a)
    if (tuple(a) in seen):
        break
    seen.add(tuple(a))

print(p1)
