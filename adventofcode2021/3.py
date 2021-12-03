import fileinput, sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE


ll = [l.strip() for l in fileinput.input()]

N = len(ll[0])

gamma = []
epsilon = []
for j in range(N):
    s = []
    for i in range(len(ll)):
        l = ll[i]
        s.append(l[j])
    ones = s.count('1')
    zeros = s.count('0')
    if ones > zeros:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma = "".join(gamma)
epsilon = "".join(epsilon)

x = ""

for j in range(N):
    s = []
    for i in range(len(ll)):
        l = ll[i]
        if (l.startswith(x)):
            s.append(l[j])
    ones = s.count('1')
    zeros = s.count('0')
    if ones >= zeros:
        x = x + '1'
    else:
        x = x + '0'
a = int(x,2)

x = ""
for j in range(N):
    s = []
    for i in range(len(ll)):

        l = ll[i]
        if (l.startswith(x)):
            s.append(l[j])
    ones = s.count('1')
    zeros = s.count('0')
    if ones == 0:
        x = x + '0'
    elif zeros == 0:
        x = x + '1'
    elif ones < zeros:
        x = x + '1'
    else:
        x = x + '0'

b = int(x,2)

print (int(gamma,2) *int(epsilon,2), a*b)
