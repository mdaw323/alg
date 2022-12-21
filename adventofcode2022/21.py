import fileinput
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

operations = {}
values = {}

for line in lines:
    a,b = line.split(": ")
    bs = b.split()
    if len(bs) == 1:
        values[a] = int(bs[0])
    else:
        operations[a] = bs

def solve(monkey, humn):
    if monkey == 'humn':
        return humn
    if monkey in values:
        return values[monkey]
    else:
        a, o, b = operations[monkey]
        a = solve(a, humn)
        b = solve(b, humn)
        if o == "+":
            v = a + b
        elif o == "*":
            v = a * b
        elif o == "-":
            v = a - b
        elif o == "/":
            v = a / b
        else:
            assert False
        return v


print(int(solve('root', values['humn'])))

a = -10**20
b = 10**20
operations['root'][1] = '-'
m = solve('root', (a + b) // 2)
dir = solve('root', a) < solve('root', b)
while (abs(m) > 0.00001):
    if (dir and m <=0) or (not dir and m >=0):
        a = (a + b) // 2
    else:
        b = (a + b) // 2
    m = solve('root', (a + b) // 2)

print ((a+b)//2)
