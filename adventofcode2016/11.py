from collections import deque
import fileinput
import itertools
import re

starting_state = []
materials = {}
lines = [line.strip() for line in fileinput.input()]
for i in range(4):
    generators = re.findall(r' ([a-z\-]+) generator', lines[i])
    microchips = re.findall(r' ([a-z\-]+)-compatible microchip', lines[i])
    for generator in generators:
        if generator not in materials:
            materials[generator] = len(materials)
            starting_state += [0,0]
        idx = materials[generator]
        starting_state[idx*2] = i+1
    for microchip in microchips:
        if microchip not in materials:
            materials[microchip] = len(materials)
            starting_state += [0,0]
        idx = materials[microchip]
        starting_state[idx*2 + 1] = i+1

mats = len(materials)
positions = mats*2

print(materials, starting_state)


starting_state = tuple(starting_state + [1])
# starting_state = State(, , , , 1)
end_state = tuple([4 for _ in range(positions)] + [4])

print (starting_state, end_state)
mem = set()
d = deque()

for c in itertools.combinations_with_replacement([1,2,3,4],2):
    print(c)


def is_valid(state):
    # print(state)
    floor_gen_safe = [True for i in range(4)]
    floor_mic_safe = [True for i in range(4)]
    for i in range(mats):
        if state[2*i] != state[2*i+1]:
            floor_gen_safe[state[2*i]-1] = False
            floor_mic_safe[state[2*i+1]-1] = False
    return all([floor_gen_safe[i] or floor_mic_safe[i] for i in range(4)])


d.append((starting_state, 0))
mem.add(starting_state)

j = 0
while len(d) > 0:
    state, steps = d.popleft()
    j+=1
    if j % 100000 == 0:
        print(j, state, steps, len(mem))
    if state == end_state:
        print(j, state, steps, len(mem))
        break
    same_floor = []
    for i in range(positions):
        if state[i] == state[-1]:
            same_floor.append(i)
    for elevator in [state[-1] -1, state[-1]+1]:
        if 1 <= elevator <= 4:
            for a,b in itertools.combinations_with_replacement(same_floor, 2):
                st = list(state)
                st[a] = st[b] = st[-1] = elevator
                new_state = tuple(st)
                mem_state = tuple(sorted([(st[2*k], st[2*k+1]) for k in range(mats)]) + [elevator])
                if mem_state not in mem and is_valid(new_state):
                    mem.add(mem_state)
                    d.append((new_state, steps+1))
