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
M = 256
numbers = [ord(c) for c in lines[0]] + [17, 31, 73, 47, 23]

print(numbers)
# numbers = [3, 4, 1, 5]
# M = 5

N = list(range(M))


# print(numbers)

i = 0
skip = 0
for round in range(64):
    for lenght in numbers:
        j = (i + lenght - 1) % M
        for l in range(lenght//2):
            N[(i+l) % M], N[(j-l) % M] = N[(j-l) % M], N[(i+l) % M]
        i+=(lenght+skip) %M
        skip += 1

kn = []
for i in range(16):
    s = 0
    for j in range(16):
        s ^= N[i*16+j]

    kn.append(hex(s)[2:])

print(*kn, sep='')

# print (*N)
# print(N[0]* N[1])
