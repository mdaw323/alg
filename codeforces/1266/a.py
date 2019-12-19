n = int(input())
for _ in range(n):
    s = [int(x) for x in input().strip()]
    
    if s.count(0) > 0 and sum(s) % 3 == 0 and (s.count(0)> 1 or s.count(4)> 0 or s.count(2)> 0 or s.count(6)> 0 or s.count(6)> 0 or s.count(8)> 0 or sum(s) == 0):
        print('red')
    else:
        print('cyan')
    