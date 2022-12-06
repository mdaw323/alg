import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

# rock AX
# paper BY
# scisors CZ

res = {
    'X':1,
    'Y':2,
    'Z':3
}

wins = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

draws = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

loses = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

results = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
    }


# print (results)
s = 0
s2 = 0
lines = [l.strip() for l in fileinput.input()]
for line in lines:
    s+= results[line]
    a,b = line.split()
    r = 0

    if b == 'Z':
        r+= 6 + res[wins[a]]
    elif b == 'Y':
        r+= 3 + res[draws[a]]
    else:
        r+= res[loses[a]]
    print(a,b, r)
    s2+=r

print(s, s2)
