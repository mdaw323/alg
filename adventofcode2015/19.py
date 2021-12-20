#!/usr/bin/python3

import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(1000)

filename = sys.argv[1] if len(sys.argv) > 1 else '19.in'


dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

rules, molecule = [l.strip() for l in open(filename).read().split("\n\n")]

rules = [rule.split(' => ') for rule in rules.split("\n")]
# print(molecule,rules)
sr = sorted([(len(re), re, ru) for ru, re in rules],reverse=True)

molecules = set()

for rule, replacement in rules:
    # print(rule,replacement)
    i = molecule.find(rule)

    while i>=0:
        molecules.add(molecule[:i] + replacement + molecule[i+len(rule):])
        i = molecule.find(rule,i+1)
        # print(i)

print(len(molecules))

def find_molecules(m):
    molecules = set()
    for replacement, rule in rules:
        # print(rule,replacement)
        i = m.find(rule)
        while i>=0:
            molecules.add(m[:i] + replacement + m[i+len(rule):])
            i = m.find(rule,i+1)
            # print(i)
    return molecules
# print(molecule)

def find_minimum_steps(molecule):
    molecules = set([molecule])

    for step in range(100):
        print (step, len(molecules))
        new_molecules = set()
        for m in molecules:
            for candindate in find_molecules(m):
                if candindate == 'e':
                    return step+1
                if len(candindate) >= len(m):
                    continue
                new_molecules.add(candindate)
        molecules = new_molecules
        # print (step+1, new_molecules)


print(molecule)
print(sr)

for step in range(500):
    for _, rep, ru in sr:
        i = molecule.find(rep)
        if i >=0:
            molecule = molecule[:i] + ru + molecule[i+len(rep):]
            break
    print(step+1, molecule)
    if molecule == 'e':
        break
