from collections import namedtuple
import re
Point = namedtuple('Point', 'x y vx vy')


second = 0

with open('adventofcode/ac10/input.txt') as f:
    raw = f.read()

rgx = r"position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>"

points = [Point(int(x), int(y), int(vx), int(vy))
          for x, y, vx, vy in re.findall(rgx, raw)]


def draw(minx, miny, maxx, maxy, second):
    print(second)
    width = maxx - minx + 1
    heigth = maxy - miny + 1
    picture = []
    for y in range(heigth):
        picture.append(['.'] * width)

    for p in points:
        picture[p.y - miny][p.x - minx] = '#'

    for y in range(heigth):
        print(''.join(picture[y]))


def recount():
    minx = min([p.x for p in points])
    miny = min([p.y for p in points])
    maxx = max([p.x for p in points])
    maxy = max([p.y for p in points])
    return (minx, miny, maxx, maxy)


def move():
    global points, second
    second += 1
    for i in range(len(points)):
        p = points[i]
        points[i] = Point(p.x + p.vx, p.y + p.vy, p.vx, p.vy)


minx, miny, maxx, maxy = recount()
while (maxx - minx > 100):
    move()
    minx, miny, maxx, maxy = recount()


for i in range(10):
    draw(minx, miny, maxx, maxy, second)
    move()
    minx, miny, maxx, maxy = recount()

# HJBJXRAZ
# 10641
