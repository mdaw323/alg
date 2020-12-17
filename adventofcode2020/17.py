import fileinput
from collections import defaultdict
from collections import namedtuple

Point = namedtuple('Point', 'x y z w')

lines = [x.strip() for x in fileinput.input()]


active = set()


rg = [-1, 0, 1]
directions = set ()
for x in rg:
    for y in rg:
        for z in rg:
            for w in rg:
                directions.add(Point(x,y,z,w))
directions.remove(Point(0,0,0,0))

z = 0
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == '#':
            active.add(Point(x,y,z,0))        

def step(active):
    cnt = defaultdict(lambda : 0)
    new_active = set()
    for x, y, z, w in active:
        for dx, dy, dz, dw in directions:
            cnt[Point(x+dx, y+dy, z+dz, w+dw)] += 1

    for point, c in cnt.items():
        if c == 3:
            new_active.add(point)
        elif c == 2 and point in active:
            new_active.add(point)
    return new_active


for i in range(6):
    active = step(active)

print (len(active))
