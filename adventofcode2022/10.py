import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

x = 1
cycle_x = []
sprite = []

def draw(x):
    sprite.append('#' if x-1 <= len(cycle_x) % 40 < x+2 else '.')

# draw(x)
for line in lines:
    words = line.split()
    if words[0] == 'noop':
        draw(x)
        cycle_x.append(x)
    else:
        draw(x)
        cycle_x.append(x)
        draw(x)
        cycle_x.append(x)
        x+= int(words[1])



p1 = 0
for c in [20,60,100,140,180,220]:
    p1+=cycle_x[c-1] * c

print (p1)
for i in range(6):
    print(*sprite[i*40:i*40+40], sep='')
