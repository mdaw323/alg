def dist (a,b,c):
    return abs(a-b) + abs(a-c) + abs(b-c)

q = int(input())
for qq in range(q):
    a,b,c = [int(x) for x in input().split()]
    s = 10e10
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                s = min(s,dist(a+i, b+j, c+k))
    print(s)