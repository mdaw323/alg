start = [12, 1, 16, 3, 11, 0]
# start = [0, 3, 6]

mem = {}
turn = 0


for s in start:
    turn += 1
    # next_to_speak = turn - mem.get(s, turn)
    mem[s] = [turn]
    next_to_speak = s
    # print(next_to_speak, mem)
    last_spoken = s

diff = 0
speak = 0

for turn in range(len(start), 30000001):
    # print(turn, last_spoken, mem)
    zz = mem[last_spoken]
    if len(zz) > 1:
        speak = zz[-1] - zz[-2]
    else:
        speak = 0
    mem[speak] = mem.get(speak, [])[-1:]
    mem[speak].append(turn)
    # print("speak: ", turn, last_spoken, speak)
    last_spoken = speak

print("speak: ", turn, speak)
