import fileinput
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

cubes = []



for line in lines:
    x,y,z = map(int,line.split(","))
    cubes.append ((x,y,z))

cs = set(cubes)

cnt = 0
cc = 0
mx, my,mz = 0,0,0
for x,y,z in cubes:
    mx = max(mx,x)
    my = max(my,y)
    mz = max(mz,z)

    for i in range(6):
        nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]
        n = (nx,ny,nz)
        if not n in cs:
            cnt += 1


mx += 2
my += 2
mz += 2

q = deque()
q.appendleft((-1,-1,-1))
cc = set()
visited = set()

cnt2 = 0
while len(q) > 0:
    e = q.pop()
    x,y,z = e

    if (e in visited) or (e in cs):
        continue
    visited.add(e)
    # if e in cs:
    #     # cc.add(e)
    #     # cnt2+=1
    #     for i in range(6):
    #         nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]
    #         n = (nx,ny,nz)
    #         if n not in cs:
    #             cc.add(n)
    #     continue

    for i in range(6):
        nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]
        v = (nx,ny,nz)
        if (-1<=nx<=mx) and (-1 <=ny <= my) and (-1 <=nz <= mz):
            q.appendleft(v)

# print(sorted(cc))
# print(sorted(cs))

cnt2 = 0
cc2 = 0
for x,y,z in cubes:
    for i in range(6):
        nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]
        n = (nx,ny,nz)
        if (not n in visited) and (not n in cs):
            cc2 +=1
            print (n)
        if (n in visited) and (not n in cs):
            cnt2 += 1


print (cnt)
print (cnt2, cc2, cnt - cc2)


# 3220 too high
# 2010 too low
# 2016 too low
