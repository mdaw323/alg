import fileinput

lines = [s.strip() for s in fileinput.input()]
black = set()
dx = [-1, 1, -2, 2, -1, 1]
dy = [1, 1, 0, 0, -1, -1]


def flip(x, y):
    if (x, y) in black:
        black.discard((x, y))
    else:
        black.add((x, y))


for s in lines:
    x = (2 * (s.count('e') - s.count('w'))
         - s.count('ne') - s.count('se') + s.count('nw') + s.count('sw'))
    y = s.count('n') - s.count('s')
    flip(x, y)
print(len(black))

for day in range(100):
    cnt = {}

    for b in black:
        cnt[b] = 0
    for b in black:
        for d in range(len(dx)):
            p = (b[0] + dx[d], b[1] + dy[d])
            cnt[p] = cnt.get(p, 0) + 1
    for p, c in cnt.items():
        if (p not in black and c == 2
                or p in black and (c == 0 or c > 2)):
            flip(*p)
print(len(black))
