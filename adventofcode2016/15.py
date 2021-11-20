import utils
import re
import math

lines = utils.readLines()

cng = []

for line in lines:
    disc, positions, time, pos = map(int, re.findall(r'\d+', line))
    # print(line, disc, positions, time, pos)
    # print(f"x + {pos + disc} == 0 (mod {positions})")
    # print(f"x = {(-pos-disc) % positions} (mod {positions})")
    cng.append( (((-pos-disc) % positions),  positions))


def reminder(cng):
    a = 0
    m = 1
    for ax, mx in cng:
        has_solution = False
        for x in range(mx):
            if (a + x*m) % mx == ax:
                has_solution = True
                a = a+x*m
                m = m * mx
                break
        if not has_solution:
            return None
    return a

print(reminder(cng[:-1]), reminder(cng))

# a == 6 (mod 7)
# b == 11 (mod 13)
# c + 5 == 0 (mod 3)
# d + 2 + 4 == 0 (mod 5)
# e + 0 + 5 == 0 (mod 17)
# f + 0 + 6 == 0 (mod 19)
