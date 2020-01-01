from utils import ints
import math
# xx = 25013 #6253

# xx = 25031 25030
xx = 10007
# deck = [x for x in range(xx)]
# ldeck = len(deck)
# di = []

CUT = 1
INC = 2
REV = 3


# def cut(D, n):
#     return D[n:] + D[:n]


# def inc(D, n):
#     pos = 0
#     copydeck = [None] * len(D)
#     for i in D:
#         copydeck[pos] = i
#         pos = (pos + n) % xx
#     return copydeck


# def rev(D, _):
#     D.reverse()
#     return D

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x


ss = 'x'
a = 1
b = 0

def cut(n, k):
    global a
    global b
    b -= n
    return (k - n) % xx


def inc(n, k):
    global a
    global b
    a *= n
    b *= n
    return (n * k) % xx


def rev(n, k):    
    global a
    global b    
    a = -a
    b = -b
    b -= 1    
    return -k - 1 % xx
    


def i_cut(n, k):
    global ss
    global a
    global b
    b +=n
    ss = f'({ss} + ({n}))'
    return (k + n) % xx


def i_inc(n, k):
    global ss
    global a
    global b

    mi = modInverse(n,xx)
    a*=mi
    b*=mi
    ss = f'({ss}) * ({mi})'
    return mi *k% xx


def i_rev(n, k):
    global ss
    global a
    global b    
    a = -a
    b = -b
    b -= 1
    ss = f'(-({ss}) - 1)'
    return -k - 1 % xx


ops = []
iops = []
with open('a22.in') as f:
    for line in f.readlines():
        if line.startswith('cut'):
            n = ints(line)[0]
            ops.append((CUT, cut, n))
            iops.append((CUT, i_cut, n))
        elif line.startswith('deal with increment'):
            n = ints(line)[0]
            # di.append(n)
            ops.append((INC, inc, n))
            iops.append((INC, i_inc, n))
        else:
            assert line.startswith('deal into new stack')
            ops.append((REV, rev, 0))
            iops.append((REV, i_rev, 0))


k = 2020

# FF = [k]
xx = 119315717514047
# for i in range(1):
    # for op, op_func, n in ops:
        # op_func(n, k)        
# 
for i in range(1):
    for op, op_func, n in reversed(iops):
        op_func(n, k)

    # print(k)

a %=xx
b%=xx

# print ((a * 2019 + b) % xx)

tms = 101741582076661
# tms = 1
A = pow(a,tms,xx)
B = b * ((1 - A)% xx) * modInverse((1-a) %xx, xx) % xx


print (a,b, tms, xx)
print (A,B)
print ("ans", (A*2020 +B) %xx )
# print ("ans", (A*5755 +B) %xx )
# print (((2020 - B) % xx) * modInverse(A,xx) % xx)
# 91545790737890 nope


# a = 1
# b = 0
# ss = 'x'
# print (ss)
# k = 5755
# for i in range(1):
#     for op, op_func, n in reversed(iops):
#         op_func(n, k)

#     print ("rev", k)
# b= b%xx
# a = a%xx
# print(a,b)
# print ("zzz",(a * 2020 + b) % xx)
# for i in range(10000000):
#     k = (a * k + b) % xx    
# print(k)

# 
# print ("revp", pow (a,tms,xx) * 2020 + (b(1 - a )) )
# #48664406518071 - too high 
  #3933219310645
   
   
 
 

# print (ss)
# print (a,b)

# # II = [k]
# xx = 119315717514047
# print (a % xx)
# print (b % xx)
# # k = 2020

#     # II.append(k)

# # pow (k,10174158207666,xx)
 

# # print (*FF)
# # print (*II)

# xx = 10
# for i in range(10):
#     k = i
#     k = cut(6, k)
#     # print ("cut",i, k)
#     k = inc(7, k)
#     # print ("inc",i, k)
#     k = rev(0, k)
#     T[k] = i
#     # print ("rev", i,k)

# print(*T)

# 0 1 2 3 4 5 6 7 8 9
# cut 6
# 6 7 8 9 0 1 2 3 4 5

# deal

# cuts = []
# for op, op_func, n in ops:
# if op == CUT:
# cuts.append(n)
# ccp = [cuts[0]] + [cuts[i] + cuts[i-1] for i in range(1, len(cuts))]
# print (sorted(ccp))
# print (len(cuts))

# D = deck.copy()
# ops = [(CUT, cut, 23472)]

# deck = D.copy()
# assert all([x == i for i,x in enumerate(deck)])

# def find_answer(deck, ops):
#     # deck = deck.copy()
#     iterations = 1
#     for _, op_func, n in ops:
#         deck = op_func(deck, n)
#     while deck[2020] != 2020:
#         if (iterations % 1000 == 0):
#             print ("d", iterations)
#         for _, op_func, n in ops:
#             deck = op_func(deck, n)
#         iterations += 1
#     assert all([x == i for i,x in enumerate(deck)])
#     return iterations


# def find_cycle(d,op_func,n):
#     deck = d.copy()
#     deck = op_func(deck, n)
#     iterations = 1
#     while deck[2020] != 2020:
#         if (iterations % 1000 == 0):
#             print ("d", iterations)
#         deck = op_func(deck, n)
#         iterations += 1
#     assert all([x == i for i,x in enumerate(deck)])
#     return iterations


# def find_repetitve(deck, ops):
#     M = {}
#     # deck = deck.copy()
#     opi = 0
#     M[tuple(deck)] = opi
#     iterations = 1

#     for _, op_func, n in ops:
#         deck = op_func(deck, n)
#         opi+=1
#         td = tuple(deck)
#         if td in M:
#             print ("found ident: ", M[td], opi)
#         M[td] =opi

#     while deck[2020] != 2020:
#         if (iterations % 1000 == 0):
#             print ("d", iterations)
#         for _, op_func, n in ops:
#             deck = op_func(deck, n)
#             opi+=1
#             td = tuple(deck)
#             if td in M:
#                 print ("found ident: ", M[td], opi)
#             M[td] =opi
#         iterations += 1
#     assert all([x == i for i,x in enumerate(deck)])
#     return iterations

# print(iterations)
# print (deck)

# print(find_cycle([i for i in range(xx)] , inc, 11))
# print (len(ops))
# print (find_answer([i for i in range(xx)], ops[0:4]))
# print (find_repetitve([i for i in range(xx)], ops))

# for i in range(xx):
# if deck[i] == 2019:
# print ("solution", i)

# di
# for i in sorted(di):
# print (i, math.gcd(i, 2020))
# print (di)


# print(119315717514047 % 101741582076661)
# 101741582076661

# 119_315_717_514_047
# 59_657_858_757_023
