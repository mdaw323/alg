import fileinput
import itertools
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

persons = set()

for nr, line in enumerate(lines):
    a, _, action, v, *_, b =line.split()
    v = int(v)
    if action == 'lose':
        v = -v
    b = b[:-1]
    dd[(a,b)] = v
    persons.add(a)
    persons.add(b)
    # print (a,v,b)

persons = list(sorted(persons))


def count_happiness(first, others):
    happiness = []
    for p in itertools.permutations(others, len(others)):
        candidate = [first] + list(p)
        h = 0
        for i,person in enumerate(candidate):
            prev = (i -1) % len(candidate)
            next = (i+1) %len(candidate)
            h += dd[(person,candidate[prev])] + dd[(person,candidate[next])]
        happiness.append(h)
        # print(candidate, h)
    return max(happiness)


print(count_happiness(persons[0], persons[1:]), count_happiness('me', persons[:]))
