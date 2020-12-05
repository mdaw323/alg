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


def count_hashes2(x0, y0, n):
    count = x = y = 0
    visited = set()
    period_sum = []
    i = 0
    while (x, y) not in visited:
        # print(i, x, y)
        i += 1
        if lines[y][x] == '#':
            count += 1
        visited.add((x, y))
        period_sum.append(count)
        x, y = (x + x0) % wi, (y + y0) % hi
    period = len(period_sum)
    print(period)
    count = count * (n // period) + period_sum[n % period]
    return count


print("part3", count_hashes2(3, 1, 289347237489237389273894273947273947293))
