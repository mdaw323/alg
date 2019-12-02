for _ in range(int(input())):
    a,b,n = map(int,input().split())
    for i in range(0,n % 3):        
        a,b = b, a ^ b
        # print(i,a,b)
    print (a)
        