from utils import *

D = []
with open('a5.in') as f:
    for line in f.readlines():
        D = ints(line)
        # D.append(words(line))


def addr(D, p, m):    
    a = D[p+1] if m[1] == 0 else p+1
    b = D[p+2] if m[2] == 0 else p+2
    c = D[p+3] if m[3] == 0 else p+3
    print("addr", p, a, b, c)
    D[c] = D[a] + D[b]
    return D


def mulr(D, p, m):
    a = D[p+1] if m[1] == 0 else p+1
    b = D[p+2] if m[2] == 0 else p+2
    c = D[p+3] if m[3] == 0 else p+3
    print("mulr", p, a, b, c)
    D[c] = D[a] * D[b]
    return D


def inp(D, p, m):
    print("inp", p, m)
    D[D[p+1]] = m
    return D


def oup(D, p, m):
    print("ouput", D[D[p+1]])
    return D[D[p+1]]


def jump_if_true(D, p, m):
    a = D[p+1] if m[1] == 0 else p+1
    b = D[p+2] if m[2] == 0 else p+2    
    if D[a] != 0:
        np = D[b]
    else:
        np = p+3
    print("jump_if_true",m, p, a, np)
    return np

def jump_if_false(D, p, m):
    a = D[p+1] if m[1] == 0 else p+1
    b = D[p+2] if m[2] == 0 else p+2
    
    if D[a] == 0:
        np = D[b]
    else:
        np = p+3
    print("jump_if_false",m, p, a, np)
    return  np

def less_than(D, p, m):
    a = D[p+1] if m[1] == 0 else p+1
    b = D[p+2] if m[2] == 0 else p+2
    c = D[p+3] if m[3] == 0 else p+3
    print("less_than", p, a, b, c)
    D[c] = 1 if D[a] < D[b] else 0

def eq(D, p, m):
    a = D[p+1] if m[1] == 0 else p+1
    b = D[p+2] if m[2] == 0 else p+2
    c = D[p+3] if m[3] == 0 else p+3
    print("eq", p, a, b, c)
    D[c] = 1 if D[a] == D[b] else 0

cds = {1: addr, 2: mulr, 3: inp, 4: oup}


def read_optcode(o):
    x = str(o)
    l = len(x)
    de = int(x[-2:])
    c = int(x[-3]) if l >= 3 else 0
    b = int(x[-4]) if l >= 4 else 0
    a = int(x[-5]) if l >= 5 else 0
    return (de, c, b, a)

def execute(D, input_value = 1):
    p = 0
    out = None
    while True:
        mm = read_optcode(D[p])
        optcode = mm[0]
        # print(mm)
        if optcode == 99:
            break
        elif optcode == 1:
            addr(D, p, mm)
            p += 4
        elif optcode == 2:
            mulr(D, p, mm)
            p += 4
        elif optcode == 3:
            inp(D, p, input_value)
            p += 2
        elif optcode == 4:
            out = oup(D, p, mm)
            p += 2
        elif optcode == 5:
            p = jump_if_true(D, p, mm)        
        elif optcode == 6:
            p = jump_if_false(D, p, mm)
        elif optcode == 7:
            less_than(D, p, mm)
            p += 4
        elif optcode == 8:
            eq(D, p, mm)
            p += 4                
        else:
            print("invalid ", optcode)
            break
    return out


print (execute(D[:], 1), execute(D[:], 5))

