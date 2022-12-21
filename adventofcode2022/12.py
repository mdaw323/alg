import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

start = None
end = None

m = defaultdict(lambda: -10)

starting = []
for i, row in enumerate(lines):
    for j, c in enumerate(row):
        if c == "S":
            start = (i,j)
            starting.append((i,j))
            m[(i,j)] = ord('a') - ord('a')
        elif c == "E":
            end = (i,j)
            m[(i,j)] = ord('z') - ord('a')
        else:
            m[(i,j)] = ord(c) - ord('a')
            if c == 'a':
                starting.append((i,j))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

r = []

seen = set()
q = deque()
for start in starting:
    q.appendleft((0,start))
d = 0
while(len(q) > 0):
    d, v = q.pop()
    print (d,v)
    if v in seen:
        continue
    if v == end:
        print ("found", d)
        r.append(d)
        break
    seen.add(v)
    for i in range(4):
        x = v[0] + dx[i]
        y = v[1] + dy[i]
        e = (x,y)

        if m[e] >=0 and  (m[e] - m[v]<=1):
            # print (e, end, m[e], m[v])
            q.appendleft( ((d+1), e) )


print(min(r))
