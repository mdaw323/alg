t = int(input())
for tt in range(t):
    n = int(input())
    A = [int(x) for x in input().strip().split()]    
    found = False
    for i in range(1,n):
        if max(A[i-1], A[i]) - min(A[i-1], A[i])>=2:
            found = True
            print("YES")
            print(i, i+1)
            break
    if not found:
        print ("NO")