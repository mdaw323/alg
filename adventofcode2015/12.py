import fileinput
import sys,re
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]
numbers = []
ignored_numbers = []

# lines =['{"d":"red","e":[1,2,3,4],"f":5}']
def get_numbers(line):
    return [int(x) for x in re.findall(r'([-]?\d+)', line)]

print(len(lines))
for nr, line in enumerate(lines):
    stack = []
    for n in get_numbers(line):
        numbers.append(n)
    ignore = -1
    for i, c in enumerate(line):
        # print(line[i-6:i+1])
        if ignore == -1 and line[i-5:i+1] == ':"red"':

            ignore = stack[-1]
            print("ss", ignore)
        elif c == '{':
            stack.append(i)
        elif c == '}':
            p = stack.pop()
            if ignore == p:
                print(line[p:i+1], sum(get_numbers(line[p:i+1])))
                for n in get_numbers(line[p:i+1]):
                    ignored_numbers.append(n)
                ignore = -1
    print (stack)




# print (numbers)

print(sum(numbers) - sum(ignored_numbers))
