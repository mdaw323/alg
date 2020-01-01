for _ in range(int(input())):
    a,b,c,r = map(int, input().strip().split())
    a, b = min(a,b), max(a,b)
    left = c-r
    right = c+r
    s = 0
    if left >= b or right <= a:
        print (b-a)
    else:
        print (max(0,c-r-min(a,b))+ max(0,max(a,b)-(c+r)))