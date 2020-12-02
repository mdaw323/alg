data = []
with open('2.in') as f:
    for line in f.readlines():
        x, y, z = line.strip().split()
        l, u = [int(i) for i in x.split('-')]
        y = y.strip(':')
        data.append((l, u, y, z))

part1 = 0
part2 = 0
for (lower, upper, char, password) in data:
    if lower <= password.count(char) <= upper:
        part1 += 1

    if ((lower <= len(password) and password[lower-1] == char)
            ^ (upper <= len(password) and password[upper-1] == char)):
        part2 += 1

print(part1, part2)
