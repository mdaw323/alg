import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

for nr in range(len(lines)):
    number_to_letters = {}
    l = lines[nr]
    x, y = l.split('|')
    display = y.split()
    numbers = [set(s) for s in x.split()]

    # 1 4 7 8
    for s in numbers:
        if len(s) == 2:
            number_to_letters[1] = s
        elif len(s) == 3:
            number_to_letters[7] = s
        elif len(s) == 7:
            number_to_letters[8] = s
        elif len(s) == 4:
            number_to_letters[4] = s
    # 6 9 0
    for s in numbers:
        if len(s) == 6:
            if not (number_to_letters[1] <= s):
                number_to_letters[6] = s
            elif number_to_letters[4] <= s:
                number_to_letters[9] = s
            else:
                number_to_letters[0] = s
    # 2 3 5
    for s in numbers:
        if len(s) == 5:
            if number_to_letters[1] <= s:
                number_to_letters[3] = s
            elif number_to_letters[9] >= s:
                number_to_letters[5] = s
            else:
                number_to_letters[2] = s

    letters_to_number = {}
    for k in number_to_letters:
        letters_to_number[''.join(sorted(number_to_letters[k]))] = k

    p1 += sum([1 for w in display if len(w) in (2, 4, 3, 7)])
    p2 += int(''.join(str(letters_to_number[''.join(sorted(w))]) for w in display))

print(p1, p2)
