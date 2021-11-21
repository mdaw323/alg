import fileinput

lines = [l.strip() for l in fileinput.input()]
line = lines[0]
x = 0
y = 0

seen = set()
houses = 1
seen.add((x, y))

rx = ry = 0
sx = sy = 0

for i, c in enumerate(line):
    if i % 2 == 0:
        x, y = rx, ry
    else:
        x, y = sx, sy

    if c == '^':
        x -= 1
    elif c == '>':
        y += 1
    elif c == '<':
        y -= 1
    else:
        x += 1

    if i % 2 == 0:
        rx, ry = x, y
    else:
        sx, sy = x, y

    if (x, y) not in seen:
        seen.add((x, y))

print(2565, len(seen))
