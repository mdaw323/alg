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

op = {}
reg = defaultdict(lambda: -1)
reg['0'] = 0
for nr in range(len(lines)):
    l = lines[nr]
    left, right = l.split(' -> ')
    x = left.split()
    if len(x) == 1:
        o = 'ASSIGN'
        a = x[0]
        b = 0
    elif len(x) == 2:
        o, a = x
        b = 0
    else:
        a,o,b = x
    op[right] = (o, a,b)

def rc(r):
    if reg[r]>=0:
        reg[r] = reg[r]
    else:
        o,a,b = op[r]
        a = int(a) if str(a).isnumeric() else rc(a)
        b = int(b) if str(b).isnumeric() else rc(b)

        if o == 'OR':
            reg[r] = a | b
        elif o == 'AND':
            reg[r] = a & b
        elif o == 'LSHIFT':
            reg[r] = a << b
        elif o == 'RSHIFT':
            reg[r] = a >> b
        elif o == 'NOT':
            reg[r] = ~a + (1<<16)
        elif o == 'ASSIGN':
            reg[r] = a
    assert ( 0 <= reg[r] < (1<<16))
    return reg[r]

p1 = rc('a')
reg = defaultdict(lambda: -1)
reg['b'] = p1
print (p1, rc('a'))
