import fileinput

lines = [line.strip() for line in fileinput.input()]
p1 = 0
for line in lines:
    t = [int(x) for x in line.split()]
    if sum(t) - max(t) > max(t):
        p1 += 1

p2 = 0
for i in range(0, len(lines), 3):
    t = []
    for j in range(3):
        line = lines[i+j]
        t.append([int(x) for x in line.split()])
    for k in range(3):
        z = [t[0][k], t[1][k], t[2][k]]
        if sum(z) - max(z) > max(z):
            p2 += 1
print(p1, p2)
