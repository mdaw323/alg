from utils import *

d = {}
G = []
s = 0
p = (0, 0)
d[p] = set()
cr = set()
crw = {}
wire = set()
dwr = {}

distance = 999999
with open("a3.in") as f:
    for line in f:
        j = 0
        sl = line.strip().split(",")
        p = (0, 0)
        wire = set()
        for s in sl:
            dr = s[0]
            n = ints(s)[0]
            x = y = 0
            if dr == 'U':
                x = 1
            if dr == 'D':
                x = -1
            if dr == 'L':
                y = -1
            if dr == 'R':
                y = 1
            for i in range(n):
                j += 1
                o = p
                p = (p[0] + x, p[1] + y)

                # print (p)
                if p in d and p not in wire:
                    crw[p]= dwr[p] + j
                    cr.add(p)
                if (p not in d):
                    d[p] = set()
                if (o not in d):
                    d[o] = set()
                if (i < n-1):
                    if dr == 'U':
                        d[p].add('|')
                    if dr == 'D':
                        d[p].add('|')
                    if dr == 'L':
                        d[p].add('-')
                    if dr == 'R':
                        d[p].add('-')
                wire.add(p)
                dwr[p] = j

                # if dst < distance:
                # distance = dst
            # print (dr,n)
# print (cr)
# print (d)
for c in cr:
    print (c, crw[c])
    # print("d", abs(c[0]) + abs(c[1]),c)
    k = 0
    if '-' in d[c]:
        k += 1
    if '|' in d[c]:
        k += 1

    if k >= 2:
        # print (d[c])
        dst = abs(c[0]) + abs(c[1])
        distance = min(crw[c], distance)

print(distance)
