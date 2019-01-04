#xx = 11
#yy = 722
#depth = 10689

xx = 10
yy = 10
depth = 510

rocky = 0
wet = 1
narrow = 2

neither = 0
torch = 1
gear = 2


V = dict()
inf = 99999

d = []


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


def init():
    d[0][0][torch] = 0


sum = 0
for i in range(xx+7):
    for j in range(yy+7):
        sum += eridx(i, j) % 3

def terrain(u):
    return V[u] % 3

def switch_relax(x, y):
    if terrain((x, y)) == rocky:
        d[x][y][torch] = min(d[x][y][gear] + 7, d[x][y][torch])
        d[x][y][gear] = min(d[x][y][torch] + 7, d[x][y][gear])
    if terrain((x, y)) == wet:
        d[x][y][neither] = min(d[x][y][gear] + 7, d[x][y][neither])
        d[x][y][gear] = min(d[x][y][neither] + 7, d[x][y][gear])
    if terrain((x, y)) == narrow:
        d[x][y][torch] = min(d[x][y][neither] + 7, d[x][y][torch])
        d[x][y][neither] = min(d[x][y][torch] + 7, d[x][y][neither])


def cost(u, v, e):
    if e == torch and (terrain(u) == wet or terrain(v) == wet):
        return inf
    elif e == neither and (terrain(u) == rocky or terrain(v) == rocky):
        return inf
    elif e == gear and (terrain(u) == narrow or terrain(v) == narrow):
        return inf
    else:
        return 1


def relax(u, v):
    ux, uy = u
    vx, vy = v
    for e in (gear, torch, neither):
        d[vx][vy][e] = min(d[vx][vy][e], cost(u, v, e) + d[ux][uy][e])
        d[ux][uy][e] = min(d[ux][uy][e], cost(v, u, e) + d[vx][vy][e])
    return


def bf():
    for i in range((xx+7) * (yy+7) * 3):        
        for y in range(yy+7):
            for x in range(xx):
                relax((x, y), (x+1, y))
                relax((x+1, y), (x, y))
        for x in range(xx+7):
            for y in range(yy):
                relax((x, y), (x, y+1))
                relax((x, y+1), (x, y))
        for x in range(xx+7):
            for y in range(yy+7):
                switch_relax(x, y)
        print (i,(xx+7) * (yy+7) * 3, d[xx][yy][torch])                



for x in range (xx+7):
    d.append([])
    for y in range (yy+7):
        d[x].append([])
        for e in range(3):
            d[x][y].append(inf)

d[0][0][torch] = 0

bf()

for x in range (xx+7):    
    for y in range (yy+7):    
        print (x,y,d[x][y])



