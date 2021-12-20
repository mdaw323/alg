import fileinput
from typing import Counter

ll = [l.strip() for l in fileinput.input()]

numbers = []
for line_nr in range(len(ll)):
    l = ll[line_nr]
    numbers = [int(x) for x in l.split(',')]


def count_fishes(days):
    dd = Counter(numbers)
    for _ in range(days):
        new_fishes = dd[0]
        for i in range(0, 8):
            dd[i] = dd[i+1]
        dd[6] += new_fishes
        dd[8] = new_fishes
    return sum([dd[i] for i in dd])


print(count_fishes(80), count_fishes(256))
