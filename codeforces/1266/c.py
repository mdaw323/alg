r, c = [int(x) for x in input().strip().split()]
#print( sum([x*x for x in [1,4,2,9,7]]))



def prime(n):
    P = [1,2]
    k = 3
    while len(P) < n:        
        is_prime = True
        for j in P[1:]:        
            if k % j == 0 :
                is_prime = False
                break
            elif j*j > k:
                break
        if is_prime:
            P.append(k)
        k+=2
    return P



primes = prime(r+c)

if r == 1 or c == 0:
    print (0)
else:
    for j in range(r):
        print(*[primes[i] * primes[c+j] for i in range(c)])
        