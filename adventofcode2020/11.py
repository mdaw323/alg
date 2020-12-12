import fileinput
import itertools
seats = [[x for x in line.strip()] for line in fileinput.input()]

wx, wy = len(seats), len(seats[0])
nb = [[0]*wy for _ in range(wx)]

dr = [(0, 1), (0, -1), (1, -1), [1, 0], (1, 1), (-1, -1), (-1, 0), (-1, 1)]


def count_nb(x, y):
    cnt = 0
    for zx, zy in dr:
        dx, dy = x+zx, y+zy
        while 0 <= dx < wx and 0 <= dy < wy and seats[dx][dy] == '.':
            dx, dy = dx+zx, dy+zy
        if 0 <= dx < wx and 0 <= dy < wy:
            if seats[dx][dy] == '#':
                cnt += 1
    # print(x, y, cnt, zz)
    return cnt


def print_matrix(L):
    for line in L:
        print(''.join([str(z) for z in line]))

    print()


# print_matrix(seats)


while True:
    changes = []

    for x, y in itertools.product(range(wx), range(wy)):
        if seats[x][y] == '#' and nb[x][y] >= 5:
            changes.append((x, y, 'L', -1))

        elif seats[x][y] == 'L' and nb[x][y] == 0:
            changes.append((x, y, '#', 1))

    for x, y, z, v in changes:
        seats[x][y] = z
    # print_matrix(seats)
    for x, y in itertools.product(range(wx), range(wy)):
        nb[x][y] = count_nb(x, y)
    # print(len(changes))
    # print_matrix(nb)
    if len(changes) == 0:
        break

print(sum([line.count('#') for line in seats]))
