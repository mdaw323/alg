import fileinput
import re

lines = [x.strip() for x in fileinput.input()]

tt = 0


conditions = []
my_ticket = []
nearby_tickets = []

ok_numbers = [0] * 1000
cond_names = []
invalid = []


for line in lines:
    if not line:
        tt += 1
        continue
    if line.startswith("your ticket") or line.startswith("nearby"):
        continue
    if tt == 0:
        r = re.findall("(.+): (\\d+)-(\\d+) or (\\d+)-(\\d+)", line)[0]
        name, a, b, c, d = r
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        # if line.startswith("departure"):
        conditions.append((a, b, c, d))
        cond_names.append(name)
        for i in range(a, b+1):
            ok_numbers[i] += 1
        for i in range(c, d+1):
            ok_numbers[i] += 1
    elif tt == 1:
        my_ticket = [int(x) for x in line.split(',')]
    else:
        numbers = [int(x) for x in line.split(',')]
        valid = True
        for n in numbers:
            if ok_numbers[n] == 0:
                valid = False
                invalid.append(n)
        if valid:
            nearby_tickets.append(numbers)

print(sum(invalid))

# print(nearby_tickets)
# print(my_ticket)

mapa = {}
mapb = {}

for row in range(len(my_ticket)):
    mapa[row] = []

for cond in range(len(conditions)):
    mapb[cond] = []


for row in range(len(my_ticket)):
    for cond in range(len(conditions)):
        pass
        a, b, c, d = conditions[cond]
        can_match = True
        for ticket in nearby_tickets:
            if not (a <= ticket[row] <= b or c <= ticket[row] <= d):
                can_match = False
                break
        if can_match:
            # print(row, cond_names[cond])
            mapa[row].append(cond)
            mapb[cond].append(row)

# print(mapa)
# print(mapb)


def find_fact():
    for r, c in mapa.items():
        if len(c) == 1:
            return (r, c[0])
    for c, r in mapb.items():
        if len(r) == 1:
            return (r[0], c)


facts = []

while True:
    f = find_fact()
    if not f:
        break
    row, cond = f
    facts.append((row, cond_names[cond]))
    del mapa[row]
    del mapb[cond]

    for v in mapa.values():
        if cond in v:
            v.remove(cond)
    for v in mapb.values():
        if row in v:
            v.remove(row)

# print(facts)

product = 1
for row, cond in facts:
    if cond.startswith("departure"):
        product *= my_ticket[row]

print(product)
