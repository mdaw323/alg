import fileinput,re
from collections import defaultdict


def signum(x): return 1 if x > 0 else (0 if x == 0 else -1)


p1, p2 = defaultdict(lambda: 0), defaultdict(lambda: 0)
ll = [l.strip() for l in fileinput.input()]

for l in ll:
    x1, y1, x2, y2 = map(int, re.findall("\d+", l))
    xx, yy = signum(x2 - x1), signum(y2 - y1)
    for i in range(max(abs(x2-x1), abs(y2-y1)) + 1):
        x, y = x1 + i*xx, y1 + i*yy
        if x1 == x2 or y1 == y2:
            p1[(x, y)] += 1
        p2[(x, y)] += 1


print(len([x for x in p1 if p1[x] >= 2]),
      len([x for x in p2 if p2[x] >= 2]))
