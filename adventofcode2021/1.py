import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement


d = [int(l.strip()) for l in fileinput.input()]

print(sum([d[i+1] > d[i] for i in range(len(d)-1)]),
      sum([d[i+3] > d[i] for i in range(len(d)-3)]))
