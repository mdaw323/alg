
q = int(input())
for qq in range(q):
    u = d= l = r = 0
    for c in input().strip():
        if c == 'L':
            l+=1
        elif c == 'D':
            d +=1
        elif c == 'U':
            u +=1
        else:
            r +=1
    u = d = min(u,d)
    l = r = min(l,r)
    if u == 0:
        l = r = min(l,1)
    if l == 0:
        u = d = min(u,1)
    print (u + d + l + r)
    print ('U' * u + 'L' * l + 'D'* d +'R' * r)
    
        