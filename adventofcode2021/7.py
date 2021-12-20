import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE



lines = [l.strip() for l in fileinput.input()]
numbers = []

for nr in range(len(lines)):
    l = lines[nr]
    numbers = list(map(int,l.split(',')))

avg = sum(numbers) // len(numbers)

print (avg, len(numbers))
numbers.sort()
median = sorted(numbers)[len(numbers) // 2]

p1 = p2 = 9999999999999999
for k in numbers:
    t = 0
    t2 = 0
    for n in numbers:
        r = abs(n - k)
        t += r * (r+1) // 2
        t2 += r
    p2 = min(p2,t)
    p1 = min(p1,t2)
    print (k,t2, t)

print (p1, p2)
