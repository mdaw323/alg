import sys

def print_query(A):
    print("?", *A)
    sys.stdout.flush()

def print_result(a):
    print("!", a)
    sys.stdout.flush()

n,k = [int(x) for x in sys.stdin.readline().split()]
b = [i+1 for i in range(k)]
e = [i+2 for i in range(k)]

if k == 1:
    print_result(k)
    exit()



print_query(e)
fpos, _ = [int(x) for x in sys.stdin.readline().split()]
r = [fpos]
found = False
for i in range(1,k+1):
    q = b[:i] + e[i:]
    print_query(q)
    pos, _ = [int(x) for x in sys.stdin.readline().split()]
    r.append(pos)

if r[0] != r[1] and r[1] == r[2]:
    r[0] = r[1]

for i in range(k,0,-1):
    if r[0] != r[i]:
        print_result(i)
        found = True
        break

if not found:
    print_result(k)