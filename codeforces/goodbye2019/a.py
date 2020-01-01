t = int(input())
for tt in range(t):
    n,k1,k2 = [int(x) for x in input().strip().split()]
    K = [int(x) for x in input().strip().split()]
    L = [int(x) for x in input().strip().split()]
    if (max(K) > max(L)):
        print ("YES")
    else:
        print ("NO")