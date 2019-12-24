from utils import ints
import math
xx = 25013 #6253
# xx = 25031 25030
# xx = 10007
deck = [x for x in range(xx)]
ldeck = len(deck)
di = []

CUT = 1
INC = 2
REV = 3


def cut(D, n):
    return D[n:] + D[:n]


def inc(D, n):
    pos = 0
    copydeck = [None] * len(D)
    for i in D:
        copydeck[pos] = i
        pos = (pos + n) % xx
    return copydeck


def rev(D, _):
    D.reverse()
    return D



ops = []
with open('a22.in') as f:
    for line in f.readlines():

        if line.startswith('cut'):
            n = ints(line)[0]
            ops.append((CUT, cut, n))
            # deck = deck[n:] + deck[:n]
            # assert len(deck) == ldeck
            # print('cut', n)
        elif line.startswith('deal with increment'):
            n = ints(line)[0]
            di.append(n)
            ops.append((INC, inc, n))
            # copydeck = deck.copy()
            # pos = 0
            # for i in range(xx):
            # deck[pos] = copydeck[i]
            # pos = (pos + n) % xx
            # print('deal with increment', n)
        else:
            assert line.startswith('deal into new stack')
            ops.append((REV, rev, 0))
            # deck.reverse()
            # print ('deal into new stack')

ss = 0
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

def find_answer(deck, ops):    
    # deck = deck.copy()
    iterations = 1
    for _, op_func, n in ops:
        deck = op_func(deck, n)
    while deck[2020] != 2020:
        if (iterations % 1000 == 0):
            print ("d", iterations)        
        for _, op_func, n in ops:                 
            deck = op_func(deck, n)
        iterations += 1    
    assert all([x == i for i,x in enumerate(deck)])
    return iterations    


def find_cycle(d,op_func,n):
    deck = d.copy()
    deck = op_func(deck, n)              
    iterations = 1
    while deck[2020] != 2020:
        if (iterations % 1000 == 0):
            print ("d", iterations)        
        deck = op_func(deck, n)
        iterations += 1    
    assert all([x == i for i,x in enumerate(deck)])
    return iterations



def find_repetitve(deck, ops):    
    M = {}
    # deck = deck.copy()
    opi = 0
    M[tuple(deck)] = opi
    iterations = 1    
    
    for _, op_func, n in ops:
        deck = op_func(deck, n)
        opi+=1
        td = tuple(deck)
        if td in M:
            print ("found ident: ", M[td], opi)            
        M[td] =opi
    
    while deck[2020] != 2020:
        if (iterations % 1000 == 0):
            print ("d", iterations)        
        for _, op_func, n in ops:                 
            deck = op_func(deck, n)
            opi+=1
            td = tuple(deck)
            if td in M:
                print ("found ident: ", M[td], opi)            
            M[td] =opi
        iterations += 1    
    assert all([x == i for i,x in enumerate(deck)])
    return iterations    

# print(iterations)
# print (deck)

# print(find_cycle([i for i in range(xx)] , inc, 11))
# print (len(ops))
# print (find_answer([i for i in range(xx)], ops[0:4]))
print (find_repetitve([i for i in range(xx)], ops))

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