import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement


p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

for line in lines:
    ll, rr = line.split(",")
    a,b = map(int,ll.split("-"))
    c,d = map(int,rr.split("-"))
    if (a<=c and b >= d) or (a >=c and b<=d):
        p1+=1
    if ([a,b,c,d] == sorted([a,b,c,d]) or [c,d,a,b] == sorted([a,b,c,d])) and (b != c and a != d):
        pass
    else:
        p2+=1

print(p1,p2)
