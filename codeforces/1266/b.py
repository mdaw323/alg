t = int(input())
T = [int(x) for x in input().strip().split()]
print(*['YES' if i > 14 and 0 < i % 14 < 7 else 'NO' for i in T])
