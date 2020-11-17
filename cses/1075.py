n = int(input())
A = sorted([int(x) for x in input().strip().split()])

mid = A[n // 2]
print (sum([abs(mid - x) for x in A]))
