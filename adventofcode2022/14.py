import fileinput
import functools
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

data = open(sys.argv[1] if len(sys.argv) >1 else '14.in').read().strip()

# data = '''498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9'''

m = defaultdict(lambda: '.')

maxy = 0

lines = [l.strip() for l in data.split("\n")]
for line in lines:
    points = line.split(" -> ")
    a = b = None
    for p in points[:]:
        c, d = map(int,p.split(","))
        maxy = max(maxy, d)
        if a != None:
            for x in range(min(a,c),max(a,c)+1):
                for y in range(min(b,d), max(b,d) + 1):
                    m[(x,y)] = '#'
        a , b = c, d
        # print (a,b)

maxy +=1

print(*m.keys())

def print_map():
    for y in range (0,15):
        print(*[m[(x,y)] for x in range (492, 506)])


while True:
    s = (500,0)

    sx,sy = s
    while True:
        if sy == maxy:
            break
        if sy >1000:
            break
        if m[(sx, sy+1)] == '.':
            sy +=1
        elif m[(sx-1, sy+1)] == '.':
            sx, sy = sx-1, sy+1
        elif m[(sx+1, sy+1)] == '.':
            sx, sy = sx +1, sy +1
        else:
            break
    if sy > 1000:
        break
    if sy ==0:
        break
    else:
        m[(sx,sy)] = 'o'
    # print_map()

print_map()

print (list(m.values()).count('o')+1)
