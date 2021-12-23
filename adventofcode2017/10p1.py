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

numbers = list(map(int, lines[0].split(',')))

# numbers = [3, 4, 1, 5]
# M = 5

N = list(range(M))


print(numbers)

i = 0
for skip, lenght in enumerate(numbers):
    j = (i + lenght - 1) % M
    for l in range(lenght//2):
        N[(i+l) % M], N[(j-l) % M] = N[(j-l) % M], N[(i+l) % M]
    i+=(lenght+skip) %M
print(N[0]* N[1])
