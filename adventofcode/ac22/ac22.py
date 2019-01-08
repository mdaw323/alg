from collections import defaultdict
from heapq import heappush, heappop

xx = 11
yy = 722
depth = 10689

mx = xx + 30
my = yy + 30

rocky = 0
wet = 1
narrow = 2

neither = 0
torch = 1
gear = 2


V = dict()
inf = 99999

d = defaultdict(lambda: inf, {})


def eridx(x, y):
    if (x, y) in V:
        return V[(x, y)]
    if (x == 0 and y == 0) or (x == xx and y == yy):
        v = depth % 20183
    elif y == 0:
        v = (x * 16807 + depth) % 20183
    elif x == 0:
        v = (y * 48271 + depth) % 20183
    else:
        v = (eridx(x-1, y) * eridx(x, y-1) + depth) % 20183
    V[(x, y)] = v
    return v


def terrain(u):
    return eridx(u[0], u[1]) % 3


def switch_relax(x, y, e1, e2):
    distance = d[(x, y, e1)] + 7
    if distance < d[(x, y, e2)]:
        d[(x, y, e2)] = distance
        heappush(h, (d[(x, y, e2)], (x, y, e2)))


def cost(u, v, e):
    if e == torch and (terrain(u) == wet or terrain(v) == wet):
        return inf
    elif e == neither and (terrain(u) == rocky or terrain(v) == rocky):
        return inf
    elif e == gear and (terrain(u) == narrow or terrain(v) == narrow):
        return inf
    else:
        return 1


def relax(u, v, e):
    ux, uy = u
    vx, vy = v
    if ux < 0 or uy < 0 or vx < 0 or vy < 0 or ux > mx or uy > my or vx > mx or vy > my:
        return
    distance = cost(u, v, e) + d[(ux, uy, e)]
    if d[(vx, vy, e)] > distance:
        d[(vx, vy, e)] = distance
        heappush(h, (d[(vx, vy, e)], (vx, vy, e)))
    return

h = []

def dijsktra(s):
    d[s] = 0
    heappush(h, (d[s], s))
    while h:
        _, v = heappop(h)
        x, y, e = v
        relax((x, y), (x+1, y), e)
        relax((x, y), (x-1, y), e)
        relax((x, y), (x, y+1), e)
        relax((x, y), (x, y-1), e)
        switch_relax(x, y, e, (e+1) % 3)
        switch_relax(x, y, e, (e+2) % 3)


sum = 0
for i in range(xx+1):
    for j in range(yy+1):
        sum += eridx(i, j) % 3

print ("part1", sum)

dijsktra((0, 0, torch))
print ("part2", d[xx, yy, torch])
