from copy import deepcopy
M = []

with open('a24.in') as f:
    for line in f.readlines():
        M.append([x for x in line.strip()])



# print(M, C)

dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def part1(M):
    
    SEEN = set()
    C = []

    for x in range(5):
        C.append([0, 0, 0, 0, 0])

    while True:
        for x in range(5):
            for y in range(5):
                C[x][y] = 0

        for x in range(5):
            for y in range(5):
                for d in dr:
                    xx = x + d[0]
                    yy = y + d[1]
                    # print (x,y, xx,yy)
                    if 0 <= xx <= 4 and 0 <= yy <= 4 and M[xx][yy] == '#':
                        C[x][y] += 1
                        # print (x,y,xx,yy, M[xx][yy])
        bi = 0
        idx = 1
        # print (C)
        for x in range(5):
            for y in range(5):
                if M[x][y] == '#' and C[x][y] != 1:
                    M[x][y] = '.'
                elif M[x][y] == '.' and 1 <= C[x][y] <= 2:
                    M[x][y] = '#'
                if M[x][y] == '#':
                    bi += idx
                idx *= 2
        if bi in SEEN:
            return bi            
        SEEN.add(bi)

N = {}

def countNeighbours(maze, level, x, y):
    c = 0    
    for d in dr:
        xx = x + d[0]
        yy = y + d[1]
        # print (x,y, xx,yy)
        if 0 <= xx <= 4 and 0 <= yy <= 4 and maze[level][xx][yy] == '#':
            c += 1
    if (level,x,y) in N:
        for l, xx,yy in N[(level,x,y)]:
            if maze[l][xx][yy] == '#':
                c+=1
    return c

def expandNeighbours(levelFrom, levelTo):
    # print("expand", levelFrom, levelTo)
    assert levelFrom + 1 == levelTo
    N[(levelTo, 2, 1)] = [(levelFrom, x, 0) for x in range(5)]
    N[(levelTo, 2, 3)] = [(levelFrom, x, 4) for x in range(5)]
    N[(levelTo, 1, 2)] = [(levelFrom, 0, x) for x in range(5)]
    N[(levelTo, 3, 2)] = [(levelFrom, 4, x) for x in range(5)]
    for x in range(5):
        N[(levelFrom, x, 0)] = []
        N[(levelFrom, x, 4)] = []
        N[(levelFrom, 0, x)] = []
        N[(levelFrom, 4, x)] = []      
    for x in range(5):
        N[(levelFrom, x, 0)].append((levelTo, 2, 1))
        N[(levelFrom, x, 4)].append((levelTo, 2, 3))
        N[(levelFrom, 0, x)].append((levelTo, 1, 2))
        N[(levelFrom, 4, x)].append((levelTo, 3, 2))


def expandMaze(maze, level):
    maze[level] = [['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '?', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.']]


def createCounters(maze):
    counter = {}
    for level in maze:
        counter[level] = [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0], ]
    return counter                          


def checkAndExpand(maze, inner, outer):
    I = maze[inner]
    O = maze[outer]
    if I[1][2] == '#' or I[3][2] == '#' or I[2][1] == '#' or I[2][3] == '#':
        inner -= 1
        expandMaze(maze, inner)
        expandNeighbours(inner, inner+1)
    cc = 0
    for x in [0, 4]:
        for y in range(5):
            if O[x][y] == '#' or O[y][x] == '#':
                cc += 1
    if cc > 0:
        outer += 1
        expandMaze(maze, outer)
        expandNeighbours(outer-1, outer)
    return (inner, outer)


def part2():
    maze = {0: M}
    maze[0][2][2] = '?'
    inner = outer = 0
    for _ in range(200):
        # print ("iteration", iteration)
        inner, outer = checkAndExpand(maze, inner, outer)
        C = createCounters(maze)
        for l in range(inner, outer+1):
            for x in range(5):
                for y in range(5):
                    C[l][x][y] = countNeighbours(maze, l, x, y)
        cc = 0
        for l in range(inner, outer+1):                
            for x in range(5):
                for y in range(5):
                    if maze[l][x][y] == '#' and C[l][x][y] != 1:
                        maze[l][x][y] = '.'
                    elif maze[l][x][y] == '.' and 1 <= C[l][x][y] <= 2:
                        maze[l][x][y] = '#'
                    if maze[l][x][y] == '#':
                        cc += 1                
    return cc
print(part1(deepcopy(M)))
print (part2())
