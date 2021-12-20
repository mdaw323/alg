import fileinput
import itertools
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

ingredients = defaultdict(lambda: 1)

for nr, line in enumerate(lines):
    ing, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split()
    ing = ing[:-1]
    capacity = int(capacity[:-1])
    durability = int(durability[:-1])
    flavor = int(flavor[:-1])
    texture = int(texture[:-1])
    calories = int(calories)

    ingredients[ing] = (capacity, durability, flavor, texture, calories)

print(ingredients)
teaspoons = 100
in_list = list(sorted(ingredients.keys()))
print(in_list)
scored = []
p2scored = []
for t in itertools.combinations_with_replacement(range(teaspoons), 3):
    a, b, c = t
    proportions = [a, b-a, c-b, teaspoons-c]
    score = 0
    total_capacity = total_durability = total_flavor = total_texture = total_calories = 0
    for i, p in enumerate(proportions):
        capacity, durability, flavor, texture, calories = ingredients[in_list[i]]
        total_capacity += p * capacity
        total_durability += p * durability
        total_flavor += p * flavor
        total_texture += p*texture
        total_calories += p* calories
    score = max(0, total_capacity) * max(0, total_durability) * \
        max(0, total_flavor) * max(0, total_texture)
    if total_calories == 500:
        p2scored.append(score)
    scored.append(score)
    # print(score)
print(max(scored), max(p2scored))
# print(a,b,c,d, sum([a,b,c,d]))
