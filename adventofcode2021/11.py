import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1,1,1,-1,-1]  # NSWE
dy = [-1, 1, 0, 0,1,-1,1,-1]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]
n = len(lines)

for i in range(len(lines)):
    l = lines[i]
    for j,c in enumerate(l):
        dd[(i,j)] = int(c)

for step in range(1000):
    f = 0

    flash = deque()
    for i in range(n):
        for j in range(n):
            if dd[(i,j)] == 9:
                flash.appendleft((i,j))
                f += 1
                dd[(i,j)] = 0
            else:
                dd[(i,j)] += 1

    while(len(flash) > 0):
        i,j = flash.pop()
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
            p = (x,y)
            if dd[p] > 0:
                if dd[p] == 9:
                    flash.appendleft(p)
                    f+=1
                    dd[p] = 0
                else:
                    dd[p] += 1
    p1 +=f
    if f == 100:
        print (step+1, f)
        break
        # break
    # print(step,f)



print(p1)
