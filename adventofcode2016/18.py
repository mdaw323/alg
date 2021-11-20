import utils

lines = utils.readLines()
line = lines[0]

TRAP = '^'
SAFE = '.'

safe = 0
ln = len(line)
pr = [x for x in line]
p1 = None
for it in range(400000):
    safe += pr.count(SAFE)
    if it == 39:
        p1 = safe
    nx = []
    for i in range(ln):
        left_is_trap = (i > 0 and pr[i-1] == TRAP)
        center_is_trap = (pr[i] == TRAP)
        right_is_trap = (i+1 < ln and pr[i+1] == TRAP)
        nx.append(TRAP if left_is_trap ^ right_is_trap else SAFE)
    pr = nx

print (p1, safe)
