for _ in range(int(input())):
    a, b, n, S = [int(x) for x in input().split()]
    print('YES' if S - min(S // n, a)*n <= b else 'NO')
