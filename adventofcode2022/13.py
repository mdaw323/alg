import fileinput
import functools
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

data = open(sys.argv[1] if len(sys.argv) >1 else '13.in').read()
cases = [l.strip() for l in data.split("\n\n")]


packets = []
def compare(l,r):
    if not isinstance(l,list):
        l = [l]
    if not isinstance(r,list):
        r = [r]

    for i in range(min(len(l),len(r))):
        a = l[i]
        b = r[i]
        if isinstance(a,list) or isinstance(b,list):
            res = compare(a,b)
            if compare(a,b) != 0:
                return res
        else:
            if a > b:
                return -1
            elif a < b:
                return 1
    if len(l) > len(r):
        return -1
    elif len(l)< len(r):
        return 1
    else:
        return 0


p1 = 0
for i, case in enumerate(cases):
    a,b = case.split("\n")
    p1 += i+1 if compare(eval(a), eval(b)) ==1 else 0
    packets.append(eval(a))
    packets.append(eval(b))

packet1 = [[2]]
packet2 = [[6]]
packets.append(packet1)
packets.append(packet2)
sorted_packets = sorted(packets, key= functools.cmp_to_key(compare), reverse=True)
print(p1, (sorted_packets.index(packet1) + 1) * (sorted_packets.index(packet2) + 1))
