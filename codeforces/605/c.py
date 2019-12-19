def nton(n):
    if n == 0:
        return 0
    else:
        return n * (n+1) // 2
        
        
n,k = [int(x) for x in input().split()]
s = input().strip()
C = set(input().strip().split())
ss = 0
i = 0
for c in s:
    if c not in C:
        ss+= nton(i)
        i = -1
    i+=1
ss+= nton(i)

print (ss)
