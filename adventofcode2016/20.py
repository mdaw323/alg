import utils
from bisect import bisect_right


lines = utils.readLines()


upper = []
lower = []

for line in lines:
    l, u = map(int, line.split('-'))
    lower.append(l)
    upper.append(u)

lower.append(4294967295+1)
upper.append(4294967295+1)

upper.sort()
lower.sort()

jj = 0
ii = 0
k = 0
level = 0
ips = 0
p1 = None
while (jj < len(upper)) and (ii < len(lower)):
    u = upper[jj]
    l = lower[ii]
    # print(ii,jj)
    if level == 0 and k < l:
        if p1 == None:
            p1 = k
        ips += l-k
        k += l-k
        continue

    if u < l:
        level -= 1
        jj += 1
        k = u+1
    elif l < u:
        level += 1
        ii += 1
        k = l + 1
    else:
        jj += 1
        ii += 1
        k = u + 1


print(p1, ips)
