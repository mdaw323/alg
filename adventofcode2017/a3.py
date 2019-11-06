import math




l = 265149

# l = 22
i = 1
j = 3
while (l > j * j):
    i += 1
    j += 2
n = l - (j-2) * (j-2) 
k = (j)//2
s = n  % (j-1)
d = min(abs(s-k), abs(k-s))
print (d+i)

