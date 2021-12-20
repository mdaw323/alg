import fileinput
import sys
import math
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

brackets = {'[' : 1, ']': -1}

def read(s):
    a = []
    for c in s:
        if c in '[]':
            a.append(c)
        elif c == ',':
            pass
        else:
            a.append(int(c))
    return a

def pprint(a:list):
    print(*a)


def find_explode(s):
    level = 0
    for i in range(len(s)-1):
        c1 = s[i]
        c2 = s[i+1]
        if c1 in brackets:
            level+=brackets[c1]

        if (c1 not in brackets) and (c2 not in brackets) and level > 4:
            return i


def find_left(s,i):
    for j in range(i-1,0,-1):
        if s[j] not in brackets:
            return j

def find_right(s,i):
    for j in range(i+1,len(s)):
        if s[j] not in brackets:
            return j


def find_split(s):
    for i,x in enumerate(s):
        if x not in brackets and x>=10:
            return i

def split(s):
    e = find_split(s)
    if not e:
        return (False, s)
    l = s[e] // 2
    r = s[e] - l
    return (True, s[:e] + ['[',l,r,']'] + s[e+1:])

def explode(s):
    e1 = find_explode(s)
    if not e1:
        return (False,s)
    e2 = e1 + 1
    l = find_left(s,e1)
    r = find_right(s,e2)
    if l:
        s[l] +=s[e1]
    if r:
        s[r] += s[e2]
    return (True, s[:e1-1] + [0] + s[e2+2:])

def reduce(s):
    result = True
    while result:
        result, s = explode(s)
        if not result:
            result, s = split(s)
    return s


def add(x,y):
    return ['['] + x + y + [']']


def magnitude(s):
    stack = []
    for c in s:
        if c == ']':
            stack.append(2 * stack.pop() + 3* stack.pop())
        elif c not in brackets:
            stack.append(c)
    res = stack.pop()
    assert(len(stack) == 0)
    return res


s = read(lines[0])
for i in range(1,len(lines)):
    s = add(s, read(lines[i]))
    s = reduce(s)

print(magnitude(s))



results = []
for x,y in combinations(lines,2):
    x = read(x)
    y = read(y)
    results.append(magnitude(reduce(add(x,y))))
    results.append(magnitude(reduce(add(y,x))))

print(max(results))

# print(*a)
# print(magnitude(a))
# print(*explode(a)[1])
