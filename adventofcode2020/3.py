import fileinput

lines = [line.strip() for line in fileinput.input()]
wi, hi = len(lines[0]), len(lines)


def count_hashes(x0, y0):
    s2 = 0
    x = y = 0
    while y < len(lines):
        if lines[y][x] == '#':
            s2 += 1
        x, y = (x + x0) % wi, y + y0
    return s2


s1 = count_hashes(3, 1)
s2 = 1

for x0, y0 in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    s2 *= count_hashes(x0, y0)

print(s1, s2)
