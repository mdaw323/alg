import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement


p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

g = []
i = 0
for line in lines:
    a,b = line[:len(line)//2], line[len(line)//2:]
    v = list(set(a).intersection(set(b)))[0]
    k = 0
    if v.isupper():
        k= ord(v) - ord('A') + 27
    else:
        k= ord(v) - ord('a') + 1


    if len(g) == 3:
        x,y,z = g
        vv = list(set(x).intersection(set(y).intersection(set(z))))[0]
        print (x,y,z, vv)
        if vv.isupper():
            p2+= ord(vv) - ord('A') + 27
        else:
            p2+= ord(vv) - ord('a') + 1

        g = []

    g.append(line)
    p1+=k
    i+=1
    # print(a,b, v,k)
if len(g) ==3:
    x,y,z = g
    vv = list(set(x).intersection(set(y).intersection(set(z))))[0]
    print (x,y,z, vv)
    if vv.isupper():
        p2+= ord(vv) - ord('A') + 27
    else:
        p2+= ord(vv) - ord('a') + 1

print(p1,p2)
