t = int(input())
for _ in range(t):
    n = int(input())
    d = []
    m = dict()
    c = 0
    for ni in range(n):
        g = [int(x) for x in input().strip()]
        d.append(g)
        tg = tuple(g)
        if tg not in m:
            m[tg] = 0
        m[tg] += 1
    
    for ii in range(len(d)):
        
        tog = tuple(d[ii])
        if m[tog] > 1:
            for i in range(9):
                d[ii][3]= (d[ii][3] +1) % 10
                tg = tuple(d[ii])
                if tg not in m:
                    m[tog] -= 1
                    m[tg] = 1
                    c += 1
                    break
    print(c)
    for g in d:
        print(*g,sep='')