import fileinput
import sys
import re
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)


dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

for nr in range(len(lines)):
    l = lines[nr]
    x = l
    original_len = len(l)

    x = re.sub(r'\\\\','-', x)
    x = re.sub(r'\\"','_', x)
    x = re.sub(r'\\x[a-f0-9]{2}','+',x)

    # print (l,x, original_len, original_len - (len(x)-2) )
    p1 += original_len - (len(x)-2)
    p2 += l.count('"') + l.count('\\') + 2
print(p1, p2)
