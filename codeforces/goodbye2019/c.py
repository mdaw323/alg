t = int(input())
for tt in range(t):
    n = int(input())
    A = [int(x) for x in input().strip().split()]
    s = sum(A)
    xorx =0
    for a in A:
        xorx = xorx ^ a
    print(2)
    print (xorx, s+xorx)

    # A = A + [xorx,s+xorx]
    # s = sum(A)
    # xorx =0
    # for a in A:
    #     xorx = xorx ^ a
    # assert s == 2 * xorx
