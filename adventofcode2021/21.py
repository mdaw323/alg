import fileinput
import sys
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import permutations, combinations, combinations_with_replacement, product
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = 6
p2 = 10


def part1(p1, p2):
    die = 1
    score1 = score2 = 0
    turn = True
    rolled = 0
    while (score1 < 1000 and score2 < 1000):

        d1 = die
        die = die % 100 + 1
        d2 = die
        die = die % 100 + 1
        d3 = die
        die = die % 100 + 1
        rolled += 3
        roll = d1+d2+d3
        if turn:
            p1 = (p1 - 1 + roll) % 10 + 1
            score1 += p1
        else:
            p2 = (p2 - 1 + roll) % 10 + 1
            score2 += p2
        turn = not turn
    return min(score1, score2) * rolled



@lru_cache(maxsize=None)
def old_dp(p1, p2, score1, score2, turn):
    if score1 >= 21:
        return Counter({"p1": 1})
    elif score2 >= 21:
        return Counter({"p2": 1})
    s = Counter()
    for i, j, k in product([1, 2, 3], repeat=3):
        if turn:
            z = (p1 - 1 + i+j+k) % 10 + 1
            s += old_dp(z, p2, score1 + z, score2, not turn)
        else:
            z = (p2 - 1 + i+j+k) % 10 + 1
            s += old_dp(p1, z, score1, score2+z, not turn)
    return s

dices = []
for i, j, k in product([1, 2, 3], repeat=3):
    dices.append(i+j+k)
dices = Counter(dices)

@lru_cache(maxsize=None)
def dp(p1, p2, score1, score2):
    if score1 >= 21:
        return (1,0)
    elif score2 >= 21:
        return (0,1)
    a = b = 0
    for k,times in dices.items():
        z = (p1 - 1 + k) % 10 + 1
        x,y = dp(p2, z, score2, score1 + z)
        a+=times * x
        b+=times * y
    return (b,a)

# print(part1(p1, p2), max(old_dp(p1, p2, 0, 0, True)))
print(part1(p1, p2), max(dp(p1, p2, 0, 0)))
