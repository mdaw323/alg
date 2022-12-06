import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement



#     [G] [R]                 [P]
#     [H] [W]     [T] [P]     [H]
#     [F] [T] [P] [B] [D]     [N]
# [L] [T] [M] [Q] [L] [C]     [Z]
# [C] [C] [N] [V] [S] [H]     [V] [G]
# [G] [L] [F] [D] [M] [V] [T] [J] [H]
# [M] [D] [J] [F] [F] [N] [C] [S] [F]
# [Q] [R] [V] [J] [N] [R] [H] [G] [Z]
#  1   2   3   4   5   6   7   8   9


stacks = [
    ['Q','M', 'G', 'C', 'L'],
    list(reversed(['G', 'H', 'F', 'T', 'C', 'L', 'D', 'R'])),
    list(reversed(['R', 'W', 'T', 'M', 'N', 'F', 'J', 'V'])),
    list(reversed(['P', 'Q', 'V', 'D', 'F', 'J'])),
    list(reversed(['T', 'B', 'L', 'S', 'M', 'F', 'N'])),
    list(reversed(['P', 'D', 'C', 'H', 'V', 'N', 'R'])),
    ['H','C','T'],
    list(reversed(['P', 'H', 'N', 'Z', 'V', 'J', 'S', 'G'])),
    ['Z', 'F', 'H', 'G']
]

print(*stacks)


p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]
#move 1 from 2 to 1
for line in lines:
    if line.startswith('move'):
        _, c, _, f,_, t = line.split()
        c,f,t = map(int,[c,f,t])
        f-=1
        t-=1
        m = list(stacks[f][-c:])
        # print (line, c,f,t, m)
        # print (stacks[f])
        # print (stacks[t])
        stacks[f] = stacks[f][:-c]
        stacks[t] = stacks[t] + m
        # print (stacks[f])
        # print (stacks[t])


p1 = []
for s in stacks:
    p1 += s[-1:]

print(*p1,sep='')
