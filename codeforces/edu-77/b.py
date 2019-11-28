for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    a, b = max(a, b), min(a, b)
    if a % 2 == 1:
        a, b = b-a//2,1            
    print("YES" if a == 2*b else "NO")
