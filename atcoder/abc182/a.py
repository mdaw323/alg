a, b = [int(x) for x in input().strip().split()]
m = 2 * a + 100 - b
print(max(m, 0))
