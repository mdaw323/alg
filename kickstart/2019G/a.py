for T in range(int(input())):
    n, m, q = [int(x) for x in input().split()]
    ans =  [1] * (n+1)
    for x in input().split():
        ans[int(x)]-=1
    for i in range(1,n+1):
        for j in range (i+i, n+1,i):
            ans[i]+=ans[j]    
    print("Case #%d: %d" % (T+1, sum([ans[int(x)] for x in input().split()])))