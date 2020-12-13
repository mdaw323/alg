import fileinput
# import math
lines = [x.strip() for x in fileinput.input()]
timestamp = int(lines[0])

line = [x for x in lines[1].split(',')]
bus_ids = []
for i, ll in enumerate(line):
    if ll != 'x':
        bus_ids.append((int(ll), i))


P1 = []
for bus, _ in bus_ids:
    b = bus - timestamp % bus
    P1.append((b, b*bus))

print(min(P1)[1])


def chin(A, M):
    mm = 1
    for m in M:
        mm *= m
    ss = 0
    for i in range(len(A)):
        x = mm // M[i]
        ix = pow(x, -1, M[i])
        ss += A[i] * x * ix
    return ss % mm


A = []
M = []
mm = 1
for bus, m in bus_ids:
    r = -m % bus
    A.append(r)
    M.append(bus)
    mm *= bus

print(chin(A, M))
