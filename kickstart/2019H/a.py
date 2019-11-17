import heapq 
for t in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]    
    C = list([A[0]])
    k = 1
    R = [1]
    for i in range(1,n):        
        if (A[i] >= k):
            heapq.heappush(C,A[i])
            p = heapq.heappop(C)
            if (p >= k+1):
                heapq.heappush(C, p)
                k+=1
        R.append(k)        
    print ("Case #%d: %s" % (t+1, ' '.join([str(x) for x in R])))