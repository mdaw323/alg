def fw(i, range):
    if i == 0:
        return (True, 0)
    okres = (i-1) // (range-1)
    up = okres % 2 == 0
    k = (i-1) % (range-1)

    p = 0
    if up:
        p = k+1
    else:
        p = range - 2 - k

    # print (i, okres, up, k, p)

    return (up, p)


d = []
with open('13.in') as f:
    i = 0
    for line in f:
        s = line.split()
        r = (int(s[0][0:-1]), int(s[1]))
        # print (r)
        d.append(r)
        i += 1

# print (d)


for i in range(10000000):
    s = 0
    for (a, b) in d:
        (x, y) = fw(a+i, b)
        (xx, yy) = fw(a+i+1, b)
        if (yy and y == 0) or (xx and yy == 0):
            # print (a,b, x, xx)
            s += 1
            break
    if (s == 0):
        print(i)
        break


# 0 6
# 1 5 7
# 2 4 8
# 3   9


# print (s)

# for i in range(10):
#    print (i, fw(i,4))
