import fileinput
lines = [list(s.strip()) for s in fileinput.input()]

seen = set()
color = {}


def flip(x, y):
    color[(x, y)] = color.get((x, y), 0) ^ 1


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

p1 = 0
black = set()
for k, v in color.items():
    if v == 1:
        p1 += 1
        black.add(k)


print(p1)

dx = [-1, 1, -2, 2, -1, 1]
dy = [1, 1, 0, 0, -1, -1]

for day in range(100):
    cnt = {}

    for k, v in color.items():
        cnt[k] = 0

    for b in black:
        bx, by = b
        for d in range(len(dx)):
            x = bx + dx[d]
            y = by + dy[d]
            cnt[x, y] = cnt.get((x, y), 0) + 1

    for p, c in cnt.items():
        x, y = p
        if color.get(p, 0) == 0 and c == 2:
            flip(x, y)
            black.add(p)
        elif color.get(p, 0) == 1 and (c == 0 or c > 2):
            flip(x, y)
            black.discard(p)
    p1 = 0
    for k, v in color.items():
        if v == 1:
            p1 += 1
        # black.add(k)
    assert len(black) == p1

print(len(black))
