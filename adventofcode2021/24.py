import fileinput
import sys
import random
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

program = []
for nr in range(len(lines)):
    l = lines[nr]
    s = l.split()
    if len(s) == 3:

        program.append(s)
    else:
        a, b = s
        program.append([a,b,'0'])


def run(inp):
    reg = {'w':0, 'z':0, 'x':0, 'y':0}
    input = [int(c) for c in inp]
    k = 0
    for i,instr in enumerate(program):
        cmd, a, b = instr
        # print (cmd, a, b, b.lstrip('-').isnumeric())
        assert a in 'wxzy'
        if cmd == 'inp':
            reg[a] = input[k]
            k+=1
        elif cmd == 'add':
            reg[a] += int(b) if b.lstrip('-').isnumeric() else reg[b]
        elif cmd == 'mul':
            reg[a] *= int(b) if b.lstrip('-').isnumeric() else reg[b]
        elif cmd == 'div':
            c = int(b) if b.lstrip('-').isnumeric() else reg[b]
            if c ==0:
                print('div by zero')
                return (False, reg)
            reg[a] //= c
        elif cmd == 'mod':
            c = int(b) if b.lstrip('-').isnumeric() else reg[b]
            if (reg[a] < 0 or c<=0):
                print(f'mod {reg[a]} {c}')
                return (False, reg)
            reg[a] %= c
        elif cmd == 'eql':
            c = int(b) if b.lstrip('-').isnumeric() else reg[b]
            reg[a] = 1 if reg[a] == c else 0
        else:
            assert False
    return reg['z']

def translate():
    reg = {'w':0, 'z':0, 'x':0, 'y':0}

    k = 0
    for i,instr in enumerate(program):
        cmd, a, b = instr
        # print (cmd, a, b, b.lstrip('-').isnumeric())
        assert a in 'wxzy'
        if cmd == 'inp':
            print(f'{a} = input[{k}];')
            k+=1
        elif cmd == 'add':
            print(f'{a} += {b};')
        elif cmd == 'mul':
            print(f'{a} *= {b};')
        elif cmd == 'div':
            print(f'{a} /= {b};')
        elif cmd == 'mod':
            print(f'{a} %= {b};')
        elif cmd == 'eql':
            print(f'{a} = {a} == {b} ? 1 : 0;')
        else:
            assert False
    return reg

def real(inpt):
    inp = [int(i) for i in inpt]
    x = y = z = w = 0

    x =z % 26 + 12
    # print(f"0", x,y,z,w)


    z = inp[0] + 15

    # print(f"1", x,y,z,w)
    z *= 26
    z += inp[1] +12
    z *= 26
    z += inp[2] + 15
    x = z % 26 -9
    z //= 26

    # print(f"3", x,y,z,w)
    x = 0 if x == inp[3] else 1
    z *= 25 * x + 1

    z += (inp[3] + 12) * x


    x = z % 26 - 7
    z //= 26
    # print(f"4", x,y,z,w)
    x = 0 if x == inp[4] else 1

    z *= 25 * x + 1
    z += (inp[4] + 15) * x

    # print(f"5", x,y,z,w)

    z *= 26
    z += inp[5] + 2


    x = z % 26 -1
    z //= 26
    # print(f"6", x,y,z,w)
    x = 0 if x == inp[6] else 1
    z *= 25*x + 1
    z += (inp[6] + 11) * x

    x = z % 26 - 16
    z //= 26

    # print(f"7", x, w)
    x = 0 if x == inp[7] else 1
    z *= 25*x + 1
    z += (inp[7] + 15) * x



    # print(f"8", x, w)
    x = 1

    z *= 26


    z +=  inp[8] + 10

    w = inp[9]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -15
    # print(f"9", x, w)
    x = 0 if x == w else 1
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 2
    y *= x
    z += y

    w = inp[10]
    x *= 0
    x += z
    x %= 26

    x += 10
    # print(f"10", x, w)
    x = 0 if x == w else 1
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 0
    y *= x
    z += y

    w = inp[11]
    x *= 0
    x += z
    x %= 26

    x += 12
    # print(f"11", x, w)
    x = 0 if x == w else 1
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 0
    y *= x
    z += y

    w = inp[12]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -4
    # print(f"12", x, w)
    x = 0 if x == w else 1
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 15
    y *= x
    z += y

    w = inp[13]
    x = z % 26
    z //= 26

    # print(f"13", x, w)
    x = 0 if x == w else 1
    # x = 1 if x == 0 else 0

    y = 25 *x + 1 # 26 lub 1
    z *= y
    y = (w + 15) * x
    z += y

    # print(z)
    return z


digits = [x for x in '123456789']

# minz = 999999999999999
# max_found = 94399898949849
# for i in range(100_000_000):
#     s = str(max_found)
#     # print (s)
#     # assert real(s) == run(s)
#     _,_,z,_ = run(s)
#     if z ==0:
#         print(s)
#     max_found += 1
# # inp = '12355678912345'


71396786836846

def sytematic(min_found):

    for i in range(100_000_000):
        s = ''
        s = str(min_found)
        min_found -=1
        if s.count('0') > 0:
            continue


        _,_,z,_ = run(s)
        # if z <= minz:
        if z ==0:
            print(z, s)
            minz = z

            # minz = z
            # if z == 0:
            #     min_found = ints

def luck(min_found):
    minz = 999999999999
    while True:
        s = ''
        for j in range(14):
            if j == 0:
                s+='2'
            elif j == 1:
                s+='1'
            elif j == 2:
                s+= '1'
            elif j == 3:
                s+= '7'
            elif j == 4:
                s+= '6'
            elif j == 5:
                s+= '1'
            else:
                s+=random.choice(digits)
        # s = str(min_found)
        min_found -=1

        if int(s) > min_found:
            continue
        _,_,z,_ = run(s)
        if z <= minz:
            print(z, s)
            minz = z
            # minz = z
            # if z == 0:
            #     min_found = ints

def max_luck(st, limit, iterations = 100000, best_found = 0):
    print(f"max luck starting from {st}, limit: {limit}, iterations = {iterations}, best_found = {best_found}")
    for _ in range(iterations):
        s = ''
        for j in range(14):
            if j < len(st):
                s+= st[j]
            else:
                s+=random.choice(digits)
        n = int(s)
        if n <= best_found:
            continue
        z = real(s)
        if z <= limit:
            print(z, s)
            best_found = n
    return str(best_found)

def min_luck(st, limit, iterations = 100000, best_found = 99999999999999):
    print(f"min luck starting from {st}, limit: {limit}, iterations = {iterations}, best_found = {best_found}")
    for _ in range(iterations):
        s = ''
        for j in range(14):
            if j < len(st):
                s+= st[j]
            else:
                s+=random.choice(digits)
        n = int(s)
        if n >= best_found:
            continue
        z = real(s)
        if z <= limit:
            print(z, s)
            best_found = n
    return str(best_found)


def verify(m):
    for i in range(m):
        s = ''
        for _ in range(14):
            s+=random.choice(digits)

        assert run(s) == real(s)

def part1():
    candidate = max_luck('', 15, 250_000_000)
    candidate = max_luck(candidate[:1], 15, 150_000_000, int(candidate))
    candidate = max_luck(candidate[:2], 15, 25_000_000, int(candidate))
    candidate = max_luck(candidate[:3], 15, 20_000_000, int(candidate))
    candidate = max_luck(candidate[:5], 0, 15_000_000)
    p1 = max_luck(candidate[:7], 0, 15_000_000, int(candidate))
    return p1



def part2():
    candidate = min_luck('', 15, 250_000_000)
    candidate = min_luck(candidate[:1], 15, 150_000_000, int(candidate))
    candidate = min_luck(candidate[:2], 15, 25_000_000, int(candidate))
    candidate = min_luck(candidate[:3], 15, 20_000_000, int(candidate))
    candidate = min_luck(candidate[:5], 0, 15_000_000)
    p1 = min_luck(candidate[:7], 0, 15_000_000, int(candidate))
    return p1

p1 = part1()
p2 = part2()

print (p1,p2)

