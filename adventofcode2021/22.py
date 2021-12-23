import fileinput
import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: False)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

cubes =[]

for nr in range(len(lines)):
    l = lines[nr]
    res, right = l.split()
    xx,yy,zz = right.split(',')
    _, x = xx.split('=')
    _, y = yy.split('=')
    _, z = zz.split('=')
    xl, xr = map(int,x.split('..'))
    yl, yr = map(int,y.split('..'))
    zl, zr = map(int,z.split('..'))
    # print(xl,xr)
    for x in range(max(-50,xl), min(50,xr)+1):
        for y in range(max(-50,yl), min(50,yr)+1):
            for z in range(max(-50,zl), min(50,zr)+1):
                # print(x,y,z)
                dd[(x,y,z)] = True if res == 'on' else False
    a = len(range(max(-50,xl), min(50,xr)+1))
    b = len(range(max(-50,yl), min(50,yr)+1))
    c = len(range(max(-50,zl), min(50,zr)+1))
    cubes.append((True if res == 'on' else False, (xl,xr+1,yl,yr+1,zl,zr+1)))

print(list(dd.values()).count(True))

RX = set()
RY = set()
RZ = set()
for _, (xl,xr,yl,yr,zl,zr) in cubes:
    RX.add(xl)
    RX.add(xr)
    RY.add(yl)
    RY.add(yr)
    RZ.add(zl)
    RZ.add(zr)

RX = list(sorted(RX))
RY = list(sorted(RY))
RZ = list(sorted(RZ))

MX = {}
MY = {}
MZ = {}

for i in range(len(RX)):
    MX[RX[i]] = i

for i in range(len(RY)):
    MY[RY[i]] = i

for i in range(len(RZ)):
    MZ[RZ[i]] = i

dd = {}
for c, (is_on,cube) in enumerate(cubes):
    xl,xr,yl,yr,zl,zr = cube
    # print(c,mode,cube)
    for x in range(MX[xl], MX[xr]):
        for y in range(MY[yl], MY[yr]):
            for z in range(MZ[zl], MZ[zr]):
                dd[(x,y,z)] = is_on

p2 = 0
for (x,y,z),is_on in dd.items():
    if is_on:
        a = RX[x+1] - RX[x]
        b = RY[y+1] - RY[y]
        c = RZ[z+1] - RZ[z]
        p2+= a*b*c
print (p2)
