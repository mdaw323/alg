n, m = [int(x) for x in input().split()]
X = sorted([int(x) for x in input().split()])
R = [0] * n
P = [0] * n
for i in range(m):   
    R[i] = X[i] + (0 if i == 0 else R[i-1])
    P[i] = X[i]
for i in range(m,n): 
    P[i] = X[i] + P[i - m]
    R[i] = R[i-1] + P[i-m] + X[i]     
print (' '.join([str(x) for x in R]))