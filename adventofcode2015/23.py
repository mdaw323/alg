#!/usr/bin/python3

import sys
from copy import deepcopy
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(10000)

filename = sys.argv[1] if len(sys.argv) > 1 else '23.in'

dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE
p1 = p2 = 0

reg = {'a' : 0, 'b' : 0}

lines = [l.strip() for l in open(filename).read().split("\n")]

prog = []
for nr, line in enumerate(lines):
    if line:
        s = line.replace(',','').split()
        prog.append(s)

def run(prog, registers):
    reg = deepcopy(registers)
    i = 0
    while 0<=i< len(prog):
        assert reg['a'] >=0 and reg['b'] >= 0
        # print (i+1,prog[i], reg)
        # if i == 39: break
        s = prog[i]
        c = s[0]
        r = s[1]
        if c == 'hlf':
            reg[r] //=2
            i+=1
        elif c == 'tpl':
            reg[r] *=3
            i+=1
        elif c == 'inc':
            reg[r]+=1
            i+=1
        elif c == 'jmp':
            i = i + int(s[1])
        elif c == 'jie':
            if reg[r] % 2 == 0 :
                i += int(s[2])
            else:
                i+=1
        elif c == 'jio':
            if reg[r] == 1 :
                i += int(s[2])
            else:
                i+=1
        else:
            assert False, (s,i)
    return reg['b']


reg['a'] = 1
print(run(prog,reg))
