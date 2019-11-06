for _ in range(int(input())):
    a, b, c = map(int, input().split())
    t = min(c//2, b)
    t += min((b-t)//2, a)
    print(t*3)