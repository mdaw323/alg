import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement


d = [int(l.strip()) for l in fileinput.input()]

print(sum([d[i+1] > d[i] for i in range(len(d)-1)]),
      sum([sum(d[i+1:i+4]) > sum(d[i:i+3]) for i in range(len(d)-3)]))
