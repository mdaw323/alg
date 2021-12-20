import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

cp = 'hepxcrrq'

tr = [chr(i + ord('a')) for i in range(26)]
print(tr)
base = 26

def to_str(n):
    res = []
    if n == 0:
        res.append(tr[0])
    while n > 0:
        res.append(tr[n % base])
        n //= base

    return ''.join(reversed(res)).rjust(8,'a')


def to_int(p):
    r = 0
    m = 1
    for i, c in enumerate(reversed(p)):
        r += (ord(c) - ord('a')) * (m)
        m*=26
        # print(i,c)
    return r

def ctoi(c):
    return ord(c) - ord('a')

def itoc(i):
    return chr(i+ord('a'))

not_allowed = 'iol'

def next(p):
    l = list(reversed(p))
    r = 1
    for i,c in enumerate(l):
        v = ctoi(c) + r
        r = v // 26
        l[i] = itoc(v % 26)
        if r == 0:
            break
    l = list(reversed(l))
    reset = False
    for i,c in enumerate(l):
        if reset:
            l[i] = 'a'
        elif c in not_allowed:
            reset = True
            l[i] = itoc(ctoi(c) + 1)
    return ''.join(l)






def is_valid(p):
    straight = False
    # print(p)
    for i in range(len(p) -2):

        x,y,z = (ctoi(p[i]), ctoi(p[i+1]), ctoi(p[i+2]))
        # print (x,y,z, (x + 1 == y), (y+1 == z), (x + 1 == y) and (y+1 == z))
        if (x + 1 == y) and (y+1 == z):
            # print('ok')
            straight = True
            break

    # print (straight)
    doubles = set()
    for i in range(len(p) -1):
        if p[i] == p[i+1]:
            doubles.add(p[i])
    # if (straight):
    #     print(p, straight, len(doubles))
    return straight and (len(doubles)>=2)


# print (is_valid('heqbzabc'))

p = next(cp)
while(not is_valid(p)):
    p = next(p)
p = next(p)
while(not is_valid(p)):
    p = next(p)
print (p)
