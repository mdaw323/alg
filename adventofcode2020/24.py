import fileinput
lines = [list(s.strip()) for s in fileinput.input()]

black = set()


def flip(x, y):
    if (x, y) in black:
        black.discard((x, y))
    else:
        black.add((x, y))


for line in lines:
    i = 0
    x, y = 0, 0
    while i < len(line):
        if line[i] == 'n':
            i += 1
            y += 1
            if line[i] == 'e':
                x += 1
            elif line[i] == 'w':
                x -= 1
            else:
                assert False
        elif line[i] == 's':
            i += 1
            y -= 1
            if line[i] == 'e':
                x += 1
            elif line[i] == 'w':
                x -= 1
            else:
                assert False
        elif line[i] == 'e':
            x += 2
        elif line[i] == 'w':
            x -= 2
        else:
            assert False
        i += 1
    flip(x, y)


print(len(black))

dx = [-1, 1, -2, 2, -1, 1]
dy = [1, 1, 0, 0, -1, -1]

for day in range(100):
    cnt = {}

    for k in black:
        cnt[k] = 0

    for b in black:
        bx, by = b
        for d in range(len(dx)):
            x = bx + dx[d]
            y = by + dy[d]
            cnt[x, y] = cnt.get((x, y), 0) + 1

    for p, c in cnt.items():
        x, y = p
        if p not in black and c == 2:
            flip(x, y)
        elif p in black and (c == 0 or c > 2):
            flip(x, y)

print(len(black))
