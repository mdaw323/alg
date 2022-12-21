import fileinput
import functools
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

data = open(sys.argv[1] if len(sys.argv) >1 else '15.in').read().strip()
lines = [l for l in data.split("\n")]


def dist(a,b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)

beacons = []

for line in lines:
    words = line.split()
    # sensor = int(words[1])
    _, sx = words[2].split("=")
    _, sy = words[3].split("=")

    _, bx = words[8].split("=")
    _, by = words[9].split("=")
    sx = int(sx.replace(",",""))
    sy = int(sy.replace(":",""))
    bx = int(bx.replace(",",""))
    by = int(by)
    beacons.append((sx,sy,bx,by, dist( (sx,sy), (bx,by))))
    # print (list(enumerate(line.split())))

points = set()

Y = 10
Y = 2000000
def part1():
    for sx,sy,bx,by,d in beacons:
        i = 0
        x1 = sx + i
        x2 = sx - i
        while dist( (x1,Y), (sx,sy)) <= d:
            assert dist( (x2,Y), (sx,sy)) <= d
            if not (x1,Y) in [(sx,sy),(bx,by) ]:
                points.add(x1)
            if not (x2,Y) in [(sx,sy),(bx,by) ]:
                points.add(x2)
            i+=1
            x1 = sx + i
            x2 = sx - i
    print(len(points))


L = 4000000

cross_points = set()
# i = 0
for sx,sy,bx,by,d in beacons:

    for dx in range(0, d+2):
        dy = d+1 - dx
        x1 = sx - dx
        x2 = sx + dx
        y1 = sy -dy
        y2 = sy + dy

        for (x,y) in [(x1,y1),(x1,y2), (x2,y1), (x2,y2)  ]:
            if (0<=x<=L) and (0<=y<=L):
                cross_points.add((x,y))

bad_points = set()

for i, p in enumerate(cross_points):
    x,y = p
    if i % 10000000 == 0:
        print (i, len(cross_points))
    found_point = False
    for sx,sy,bx,by,d in beacons:
        if found_point:
            break
        if dist( (sx,sy), (x,y) ) <= d:
            bad_points.add((x,y))
            found_point = True
    if not found_point:
        print (x* 4000000 + y)
        break
