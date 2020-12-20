import fileinput
import re
import math
from collections import defaultdict


def get_point_state(n, p, state):
    x, y = p
    if state // 4 == 1:
        x, y = n-1-x, y
    for _ in range(state % 4):
        x, y = (n-1-y), x
    return (x, y)


def left(A, state):
    X = []
    n = len(A)
    for i in range(n):
        x, y = get_point_state(n, (i, 0), state)
        X.append(A[x][y])
    return ''.join(X)


def right(A, state):
    X = []
    n = len(A)
    for i in range(n):
        x, y = get_point_state(n, (i, n-1), state)
        X.append(A[x][y])
    return ''.join(X)


def up(A, state):
    X = []
    n = len(A)
    for i in range(n):
        x, y = get_point_state(n, (0, i), state)
        X.append(A[x][y])
    return ''.join(X)


def down(A, state):
    X = []
    n = len(A)
    for i in range(n):
        x, y = get_point_state(n, (n-1, i), state)
        X.append(A[x][y])
    return ''.join(X)


def fix_picture(A, state):
    n = len(A)
    X = []
    for i in range(n):
        X.append([None] * n)

    for i in range(n):
        for j in range(n):
            x, y = get_point_state(n, (i, j), state)
            X[i][j] = A[x][y]
    return X


lines = [s.strip() for s in fileinput.input()]
tile = 0
pictures = {}
picture = []
for line in lines:
    if not line:
        pictures[tile] = picture
        picture = []
    elif line.startswith("Tile"):
        tile = int(re.findall("(\\d+)", line)[0])
    else:
        picture.append(list(line))
pictures[tile] = picture
ll = len(picture)

emap = defaultdict(lambda: [])

for tile, v in pictures.items():
    for state in range(8):
        key = up(v, state)
        emap[key].append(tile)


neighbour_counter = {}
for k, v in emap.items():
    if len(v) == 1:
        neighbour_counter[v[0]] = neighbour_counter.get(v[0], 0) + 1

part1 = 1
corner = 0
for k, v in neighbour_counter.items():
    if v == 4:
        part1 *= k
        corner = k


states = []
states_size = int(math.sqrt(len(pictures)))
for i in range(states_size):
    states.append([None] * states_size)

# wybierz narożnik jako 0,0
for state in range(8):
    if (len(emap[up(pictures[corner], state)]) == 1
            and len(emap[left(pictures[corner], state)]) == 1):
        states[0][0] = (corner, state)
        break

# wypełnij w prawo pierwszy rząd
i = 0
for j in range(1, states_size):
    p, state = states[i][j-1]
    to_be = right(pictures[p], state)
    found = emap[to_be][0] if emap[to_be][0] != p else emap[to_be][1]
    for new_state in range(8):
        if left(pictures[found], new_state) == to_be:
            states[i][j] = (found, new_state)
            break

# wypełnij w dół pierwszą kolumnę
j = 0
for i in range(1, states_size):
    p, state = states[i-1][j]
    to_be = down(pictures[p], state)
    found = emap[to_be][0] if emap[to_be][0] != p else emap[to_be][1]
    for new_state in range(8):
        if up(pictures[found], new_state) == to_be:
            states[i][j] = (found, new_state)
            break

# wypełnij pozostałe na podstawie lewego sąsiada
for i in range(1, states_size):
    for j in range(1, states_size):
        p, state = states[i][j-1]
        to_be = right(pictures[p], state)
        found = emap[to_be][0] if emap[to_be][0] != p else emap[to_be][1]
        for new_state in range(8):
            if left(pictures[found], new_state) == to_be:
                states[i][j] = (found, new_state)
                break


big_image_size = states_size * 8

big_image = []
for i in range(big_image_size):
    big_image.append([None] * big_image_size)

for i in range(states_size):
    for j in range(states_size):
        p, state = states[i][j]
        picture = fix_picture(pictures[p], state)
        for x in range(1, 9):
            for y in range(1, 9):
                # print(i, j, x, y, i*8 + x, j*8 + y)
                big_image[i*8 + x-1][j*8 + y-1] = picture[x][y]


sea_monster_pattern = [list('                  # '),
                       list('#    ##    ##    ###'),
                       list(' #  #  #  #  #  #   ')]

sea_monster = set()
px = len(sea_monster_pattern)
py = len(sea_monster_pattern[0])

for i in range(px):
    for j in range(py):
        if (sea_monster_pattern[i][j] == '#'):
            sea_monster.add((i, j))

part2 = 1e9
for state in range(8):
    fixed_picture = fix_picture(big_image, state)
    for x in range(big_image_size-px):
        for y in range(big_image_size-py):
            found = True
            for dx, dy in sea_monster:
                if fixed_picture[x+dx][y+dy] != '#':
                    found = False
                    break
            if found:
                for dx, dy in sea_monster:
                    fixed_picture[x+dx][y+dy] = 'O'
    hash_count = sum([i.count('#') for i in fixed_picture])
    part2 = min(part2, hash_count)

print(part1, part2)
