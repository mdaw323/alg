import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

for nr in range(len(lines)):
    l = lines[nr]
    cmd, cmp = l.split(' if ')
    l_reg, l_cmd, l_val = cmd.split()
    r_reg, r_op, r_val = cmp.split()
    r_val = int(r_val)
    l_val = int(l_val)
    cond = ((r_op == '>' and dd[r_reg] > r_val)
            or (r_op == '<' and dd[r_reg] < r_val)
            or (r_op == '>=' and dd[r_reg] >= r_val)
            or (r_op == '<=' and dd[r_reg] <= r_val)
            or (r_op == '!=' and dd[r_reg] != r_val)
            or (r_op == '==' and dd[r_reg] == r_val))
    if cond:
        if l_cmd == 'inc':
            dd[l_reg] += l_val
        else:
            dd[l_reg] -= l_val
        p2 = max(p2, dd[l_reg])

print(max(dd.values()), p2)
