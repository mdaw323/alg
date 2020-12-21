import fileinput
from collections import defaultdict
lines = [x.strip() for x in fileinput.input()]
# sqjhc mxmxvkd sbzzf (contains fish)
meals = []

for line in lines:
    infr, aler = line.split(" (contains ")
    meals.append((set((infr.split())), set(aler.strip(")").split(", "))))

allergens = set()
cant_contain = defaultdict(set)
ingredients = set()

for inf, ale in meals:
    ingredients |= inf
    allergens |= ale


def find_next(allergen):
    candidates = None
    for meal_ingredients, meal_allergens in meals:
        if allergen in meal_allergens:
            if not candidates:
                candidates = meal_ingredients
            else:
                candidates = candidates & meal_ingredients
    if candidates and len(candidates) == 1:
        return (list(candidates)[0], allergen)


def remove_i_a(ind, al):
    for i, a in meals:
        i.discard(ind)
        a.discard(al)


part2 = []

while True:
    no_other_results = True
    for allergen in allergens:
        f = find_next(allergen)
        if f:
            i, a = f
            allergens.discard(all)
            remove_i_a(i, a)
            part2.append((a, i))
            no_other_results = False
    if no_other_results:
        break

part1 = 0

for meal_ingredients, _ in meals:
    part1 += len(meal_ingredients)


print(part1, ",".join([i for a, i in sorted(part2)]))
