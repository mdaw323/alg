import sys
# infile = open("a.in")
infile = sys.stdin

n = int(infile.readline())
for i in range(n):
    c, s = [int(x) for x in infile.readline().split()]    
    k = s // c
    m = s - k * c    
    q = 0
    q+= ((k+1)**2) * m  + (k**2)* (c-m)
    print(q)
