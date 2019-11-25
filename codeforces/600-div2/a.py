for t in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    d = -9999
    for i in range(n):
        nd = B[i]-A[i]
        if nd == d or (nd == 0 and d ==-9999):
            continue
        if nd <0:
            d = -10000
            break
        if d == -9999:
            d = nd
        elif nd == 0:
            d = 0
        else:
            d = -10000
            break    
    print("YES" if d>=-9999 else "NO")