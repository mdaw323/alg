import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

pipes = []
lead_to = {}
rates = {}

#Valve UI has flow rate=4; tunnels lead to valves YI, XO, LX, NC, RP
for line in lines:
    words = line.split()
    v = words[1]
    _, rate = words[4].split("=")
    rate = int(rate.replace(";", ""))
    lead = [x.replace(",","") for x in words[9:]]
    # print(line)
    # print(v,rate,lead)
    pipes.append(v)
    lead_to[v] = lead
    rates[v] = rate


mem = {}
mem2 = {}

pp = []
R = {}

cnt = 0
i = 0
for p in pipes:
    if rates[p] > 0:
        pp.append(p)
        R[p] = i
        i+=1
        cnt +=1



def solve(position, minutes_left, opened_pipes, realesed_preasure, next_released_preasure):
    # print (position, minutes_left, opened_pipes, realesed_preasure, next_released_preasure)
    key = (position, minutes_left, tuple(sorted(opened_pipes)))
    if key in mem:
        return mem[key]

    if len(opened_pipes) == cnt:
        res = next_released_preasure * minutes_left
        # print (position, minutes_left, opened_pipes, realesed_preasure, next_released_preasure, res, realesed_preasure + res)
        mem[key] = res
        return res

    if minutes_left == 0:
        return 0

    results = []
    #rp = realesed_preasure + next_released_preasure

    if (not (position in opened_pipes)) and rates[position] > 0:
        ns = opened_pipes.copy()
        ns.add(position)
        # ns = set(list(opened_pipes) + [position])
        results.append(solve(position, minutes_left-1, ns, 0, next_released_preasure + rates[position]))
    # else:
    for k in lead_to[position]:
        results.append(solve(k,minutes_left-1, opened_pipes, 0, next_released_preasure))
    res = next_released_preasure + max(results)
    mem[key] = res
    return res

def solve_with_ele(positions, minutes_left, opened_pipes, next_released_preasure):
    ppos = tuple(positions)
    pppipes = tuple(sorted(opened_pipes))
    key = (ppos, minutes_left, pppipes)
    if key in mem:
        return mem[key]

    if len(opened_pipes) == cnt:
        res = next_released_preasure * minutes_left
        mem[key] = res
        return res

    if minutes_left == 0:
        return 0

    results = []
    open_cnt = 0
    if ((not (positions[0] in opened_pipes) and rates[positions[0]] > 0)
        and positions[0] != positions[1]
        and (not (positions[1] in opened_pipes) and rates[positions[1]] > 0)):
            ns = opened_pipes.copy()
            ns.add(positions[0])
            ns.add(positions[1])
            open_cnt +=2
            results.append(solve_with_ele(positions, minutes_left-1, ns, next_released_preasure + rates[positions[0]] + rates[positions[1]]))
    elif (not (positions[0] in opened_pipes) and rates[positions[0]] > 0):
        ns = opened_pipes.copy()
        ns.add(positions[0])
        open_cnt +=1
        for k in lead_to[positions[1]]:
            new_pos = list(sorted([k,positions[0]]))
            results.append(solve_with_ele(new_pos, minutes_left-1, ns, next_released_preasure + rates[positions[0]]))

    elif (not (positions[1] in opened_pipes) and rates[positions[1]] > 0):
        ns = opened_pipes.copy()
        ns.add(positions[1])
        open_cnt +=1
        for k in lead_to[positions[0]]:
            new_pos = list(sorted([k,positions[1]]))
            results.append(solve_with_ele(new_pos, minutes_left-1, ns, next_released_preasure + rates[positions[1]]))
    for k in lead_to[positions[0]]:
        for v in lead_to[positions[1]]:
            new_pos = list(sorted([k,v]))
            results.append(solve_with_ele(new_pos,minutes_left-1, opened_pipes, next_released_preasure))
    res = next_released_preasure + max(results)
    mem[key] = res
    return res

# def solve_with_ele2(position, elephant, minutes_left, opened_pipes, next_released_preasure):
#     # print (position, minutes_left, opened_pipes, realesed_preasure, next_released_preasure)
#     position = sorted([position, elephant])[0]
#     elephant = sorted([position, elephant])[1]
#     key = (position,elephant, my_move, minutes_left, tuple(sorted(opened_pipes)))
#     if key in mem:
#         return mem[key]

#     # if len(opened_pipes) == cnt:
#     #     if my_move:
#     #         res = next_released_preasure * minutes_left
#     #     # print (position, minutes_left, opened_pipes, realesed_preasure, next_released_preasure, res, realesed_preasure + res)
#     #     mem[key] = res
#     #     return res

#     if minutes_left == 0:
#         return 0

#     results = []
#     # rp = realesed_preasure + next_released_preasure

#     if my_move:
#         if (not (position in opened_pipes)) and rates[position] > 0:
#             ns = opened_pipes.copy()
#             ns.add(position)
#             # ns = set(list(opened_pipes) + [position])
#             results.append(solve_with_ele(position, elephant, False, minutes_left, ns, next_released_preasure + rates[position]))
#         # else:
#         for k in lead_to[position]:
#             results.append(solve_with_ele(k, elephant,False, minutes_left, opened_pipes, next_released_preasure))
#     else:
#         if (not (elephant in opened_pipes)) and rates[elephant] > 0:
#             ns = opened_pipes.copy()
#             ns.add(elephant)
#             # ns = set(list(opened_pipes) + [position])
#             results.append(solve_with_ele(position, elephant, True, minutes_left-1, ns, next_released_preasure + rates[elephant]))
#         # else:
#         for k in lead_to[elephant]:
#             results.append(solve_with_ele(position, k, True, minutes_left-1, opened_pipes, next_released_preasure))
#     if (my_move):
#         res = next_released_preasure + max(results)
#     else:
#         res =  max(results)

#     mem[key] = res
#     return res


# print(3, solve('AA', 3, set(), 0, 0))

# for i in range(30):
#     mem = {}
#     print(i+1, solve('AA', i+1, set(), 0, 0))



# mem = {}
print(solve('AA', 30, set(), 0, 0))




# for i in range(15):
#     mem = {}
#     mem2 = {}
#     print(i+1, solve_with_ele(['AA','AA'], i+1, set(), 0))
    #
mem = {}
print(solve_with_ele(['AA','AA'], 26, set(), 0))
# print (pp)

# print (solve('CC', 6, set(['BB', 'CC', 'DD', 'EE', 'HH', 'JJ']), 0, 81))
# print (solve('CC', 7, set(['BB', 'DD', 'EE', 'HH', 'JJ']), 0, 79))
# print (solve('DD', 8, set(['BB', 'DD', 'EE', 'HH', 'JJ']), 0, 79))
# print (solve('EE', 9, set(['BB', 'DD', 'EE', 'HH', 'JJ']), 0, 79))
#print (solve('EE', 10, set(['BB', 'DD', 'HH', 'JJ']), 0, 76))
# print (solve('FF', 11, set(['BB', 'DD', 'HH', 'JJ']), 0, 76))
# print (solve('GG', 12, set(['BB', 'DD', 'HH', 'JJ']), 0, 76))



# print(pipes, lead_to, rates)
# print (mem)
