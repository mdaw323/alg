import fileinput
import re
from copy import deepcopy


pictures = {}


# Tile 1213:
# ..#.#..#..
# #.#....###
# ..#......#
# ##.#......
# ..#....###
# ...#.....#
# .#.#.....#
# #.#.....##
# ..##.#..#.
# ...#...#.#


lines = [s.strip() for s in fileinput.input()]

tile = 0
pic = []
for line in lines:
    if not line:
        pictures[tile] = pic
        pic = []
    elif line.startswith("Tile"):
        tile = int(re.findall("(\\d+)", line)[0])
    else:
        pic.append(list(line))
pictures[tile] = pic
ll = len(pic)

mem = {}

for tile, v in pictures.items():
    vv = []
    vv.append(v[0][:])
    vv.append(v[ll-1][:])
    v3 = []
    v4 = []
    for i in range(ll):
        v3.append(v[i][0])
        v4.append(v[i][ll-1])
    vv.append(v3)
    vv.append(v4)
    for i in range(4):
        vv.append(reversed(vv[i]))
    for i in range(len(vv)):
        key = ''.join(vv[i])
        if key not in mem:
            mem[key] = []
        mem[key].append(tile)

# print(mem)

mem2 = {}

# print(mem)
for k, v in mem.items():
    if len(v) == 1:
        mem2[v[0]] = mem2.get(v[0], 0) + 1

il = 1
# print(mem2)
fp = 0
for k, v in mem2.items():
    if v == 4:
        il *= k
        fp = k
        # print(k)

print(il)


def rotate_point(n, p):
    x, y = p
    return ((n-1-y), x)


def get_point_state(n, p, state):
    x, y = p
    if state // 4 == 1:
        x, y = flip_point(n, (x, y))
    for _ in range(state % 4):
        x, y = (n-1-y), x
    return (x, y)


def flip_point(n, p):
    x, y = p
    return (n-1-x, y)


def wypisz(A):
    print("=")
    for x in A:
        print("".join([str(z) for z in x]))
    print("-")


def rotate(A):
    B = deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A)):
            x, y = rotate_point(len(A), (i, j))
            B[i][j] = A[x][y]
    return B


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


def apply_state(A, state):
    n = len(A)
    X = []
    for i in range(n):
        X.append([None] * n)

    for i in range(n):
        for j in range(n):
            x, y = get_point_state(n, (i, j), state)
            X[i][j] = A[x][y]
    return X


states = []
sl = 12
for i in range(sl):
    states.append([None] * sl)

# print(fp)
for state in range(8):
    if (len(mem[up(pictures[fp], state)]) == 1
            and len(mem[left(pictures[fp], state)]) == 1):
        states[0][0] = (fp, state)
        break
    # print(state, fp, len(mem[up(pictures[fp], state)])
    #       == 1, len(mem[right(pictures[fp], state)]) == 1)


i = 0
for j in range(1, sl):
    p, state = states[i][j-1]
    to_be = right(pictures[p], state)
    # for i in range(sl):
    #     print(states[i])
    assert len(mem[to_be]) == 2, p
    found = mem[to_be][0] if mem[to_be][0] != p else mem[to_be][1]
    for new_state in range(8):
        if left(pictures[found], new_state) == to_be:
            states[i][j] = (found, new_state)
            break


j = 0
for i in range(1, sl):
    p, state = states[i-1][j]
    to_be = down(pictures[p], state)
    assert len(mem[to_be]) == 2, print("aaa")
    found = mem[to_be][0] if mem[to_be][0] != p else mem[to_be][1]
    for new_state in range(8):
        if up(pictures[found], new_state) == to_be:
            states[i][j] = (found, new_state)
            break


for i in range(1, sl):
    for j in range(1, sl):
        p, state = states[i][j-1]
        to_be = right(pictures[p], state)
        assert len(mem[to_be]) == 2
        found = mem[to_be][0] if mem[to_be][0] != p else mem[to_be][1]
        for new_state in range(8):
            if left(pictures[found], new_state) == to_be:
                states[i][j] = (found, new_state)
                break


n = sl * 8

P = []
for i in range(n):
    P.append([None] * n)

for i in range(sl):
    for j in range(sl):
        p, state = states[i][j]
        pic = apply_state(pictures[p], state)
        for x in range(1, 9):
            for y in range(1, 9):
                # print(i, j, x, y, i*8 + x, j*8 + y)
                P[i*8 + x-1][j*8 + y-1] = pic[x][y]


pattern = [list('                  # '),
           list('#    ##    ##    ###'),
           list(' #  #  #  #  #  #   ')]

pat = set()
px = len(pattern)
py = len(pattern[0])

for i in range(px):
    for j in range(py):
        if (pattern[i][j] == '#'):
            pat.add((i, j))
# print(pat)

# wypisz(P)

min_h = 1e9
for state in range(8):
    S = apply_state(P, state)
    for x in range(n-px):
        for y in range(n-py):
            found = True
            for dx, dy in pat:
                # print(x, y, px, py)
                if S[x+dx][y+dy] != '#':
                    found = False
                    break
            if found:
                for dx, dy in pat:
                    S[x+dx][y+dy] = 'O'
    # wypisz(S)
    hash_count = 0
    for i in S:
        hash_count += i.count('#')
    min_h = min(min_h, hash_count)
    # print(hash_count)
    # wypisz(S)

print(min_h)
