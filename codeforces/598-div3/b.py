for _ in range(int(input())):
    n, q, s = int(input()), [int(x) for x in input().split()], set()
    for i in range(n-1):
        for j in range(n-i-2, n-1, 1):
            if not j in s and q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                s.add(j)
    print(' '.join([str(x) for x in q]))