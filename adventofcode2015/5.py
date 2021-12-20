import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

ll = [l.strip() for l in fileinput.input()]

vowels = set('aeiou')
disallowed_strings = set(['ab', 'cd', 'pq', 'xy'])

for ii in range(len(ll)):
    l = ll[ii]
    sum_vowels = sum([1 for c in l if c in vowels]) >= 3
    duplicate = False
    prohibited_strings = False

    for i in range(len(l) -1):
        x = l[i]
        y = l[i+1]
        if l[i] == l[i+1]:
            duplicate = True
        if l[i:i+2] in disallowed_strings:
            prohibited_strings = True

    if (sum_vowels and duplicate and (not prohibited_strings)):
        p1+=1

    rep = False
    overl = False
    for i in range(len(l) -2):
        if l[i] == l[i+2]:
            rep = True
    for i in range(len(l) -2):
        x = l[i:i+2]

        if l[i+2:].find(x) >=0:
            overl = True
    print (l, rep, overl)
    if rep and overl:
        p2+=1


print(p1, p2)
