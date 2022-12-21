import fileinput
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

blueprints = {}

# [(0, 'Blueprint'), (1, '30:'), (2, 'Each'),
# (3, 'ore'), (4, 'robot'), (5, 'costs'), (6, '3'), (7, 'ore.'),
# (8, 'Each'),
# (9, 'clay'), (10, 'robot'), (11, 'costs'), (12, '3'), (13, 'ore.'), (14, 'Each'),
# (15, 'obsidian'),(16, 'robot'), (17, 'costs'), (18, '2'), (19, 'ore'), (20, 'and'), (21, '7'), (22, 'clay.'),
# (23, 'Each'),
# (24, 'geode'), (25, 'robot'), (26, 'costs'), (27, '2'), (28, 'ore'), (29, 'and'), (30, '9'), (31, 'obsidian.')]
for line in lines:
    words = line.split()
    bp = int(words[1].replace(":",""))
    ore = (int(words[6]),0, 0,0)
    clay = (int(words[12]), 0, 0,0)
    obsidian = (int(words[18]), int(words[21]), 0, 0)
    geode = (int(words[27]), 0, int(words[30]), 0)
    blueprints[bp] = (ore,clay,obsidian,geode)
    # print(ore, clay, obsidian,geode)

print(blueprints)

def can_build(resources, cost):

    res = ((resources[0] - cost[0] >= 0)
        and (resources[1] - cost[1] >= 0)
        and (resources[2] - cost[2] >= 0))
    # print("cb", resources, cost, res)
    return res

def substract(resources, cost):
    return (resources[0] - cost[0], resources[1] - cost[1], resources[2] - cost[2], resources[3] - cost[3])

def add_income(resources,income):
    return (resources[0] + income[0], resources[1] + income[1], resources[2] + income[2], resources[3] + income[3])


mem = {}
expect = [0] * 33
def solve(bp, minute, total_minutes, resources, income,future_income, history):
    # print (bp, minute, total_minutes, resources, income)
    if minute == total_minutes:
        return (resources[3], history)
    # if expect[minute] > resources[3]:
    #     return (resources[3] + income[3], history)
    # else:
    #     for m in range(minute, total_minutes+1):
    #         expect[m] = max(expect[m], resources[3] + income[3] * (m-minute))
    key = (minute, resources, income )
    if key in mem:
        return mem[key]
    results = []
    build = False
    for i in range(3,-1,-1):
        b = blueprints[bp][i]
        # if i == 0 and income[0] > 15:
        #     continue
        # if i == 1 and income[1] > 15:
        #     continue
        if can_build(resources, b):
            new_income = list(income)
            new_income[i] +=1
            new_income = tuple(new_income)
            nr = add_income(substract(resources,b), income)
            results.append(solve(bp, minute+1,total_minutes, nr, new_income, (0,0,0,0), history + [(minute+1, nr, new_income)]))
            if (i >=2):
                build = True
                break

    # if not build:
        nr = add_income(resources, income)
        ni = add_income(income, future_income)
        results.append(solve(bp, minute + 1,total_minutes, nr, ni, (0,0,0,0), history + [(minute+1, nr, ni)]))
    mem[key] = max(results)
    return mem[key]


# print ((1,0) > (1,1))


p1 = 0
p2 = 1
for bp in range(min(3,len(blueprints))):
    mem = {}
    expect = [0] * 33
    k = bp + 1
    r,history = solve(k, 0, 32, (0,0,0,0), (1,0,0,0), (0,0,0,0), [])
    p1 += r * k
    p2 *= r
    print (k, r)


print (p1, p2)
# mem = {}

# for h in history:
#     print (h)



# for time in range(16,25):
#     mem = {}

    # expect[time] = r

# print(*expect)
# 1607 too low
