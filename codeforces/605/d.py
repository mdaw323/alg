n = int(input())
A = [int(x) for x in input().split()]
B = [0] * n
k = 0
K = [1]
for i in range(1, n):
    if A[i-1] >= A[i]:
        k += 1
        K.append(0)
    K[k] += 1
    B[i] = k
m = max(K)

if n > 2:
    for i in range(1, n-1):
        mm = K[B[i-1]] + K[B[i+1]]
        if K[B[i]] == 1:
            if A[i-1] < A[i+1]:
                mm = K[B[i-1]] + K[B[i+1]]
                m = max(mm, m)
                # print (i,"mm", mm, A[i-1], A[i+1])
        else:
            if B[i-1]< B[i+1] and A[i-1] < A[i+1]:
                # print (i,"else", mm-1)
                m = max(mm - 1, m)
# print(A)
# print(B)
# print(K)
print(m)
