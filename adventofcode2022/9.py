import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

rope = [(0,0)] * 10
direction = {'L':(-1,0), 'R':(1,0), 'U':(0,-1), 'D':(0,1)}

p1 = set()
p2 = set()
sgn = lambda x: 0 if x == 0 else 1 if x>0 else -1

for line in lines:
    d, length =  line.split()
    for _ in range(int(length)):
        rope[0] = (rope[0][0] + direction[d][0], rope[0][1] + direction[d][1])
        for i in range(1,10):
            if abs(rope[i-1][0] - rope[i][0]) > 1 or abs(rope[i-1][1] - rope[i][1]) > 1:
                rope[i] = ( rope[i][0] + sgn(rope[i-1][0] - rope[i][0])
                          , rope[i][1] + sgn(rope[i-1][1] - rope[i][1]) )
        p1.add(rope[1])
        p2.add(rope[9])

print (len(p1), len(p2))
