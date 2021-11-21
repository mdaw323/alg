import fileinput
from copy import deepcopy

lines = [l.strip() for l in fileinput.input()]

reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

instructions = []
for line in lines:
    instructions.append(line.split())


def prog(reg, instructions):
    ins = deepcopy(instructions)
    instr = 0
    while instr < len(ins):
        s = ins[instr]
        # print (instr, *s, reg)
        if s[0] == 'cpy':
            if s[2] in reg:
                reg[s[2]] = int(reg[s[1]]) if s[1] in reg else int(s[1])
            else:
                print("skip invalid ", instr, *s, reg)
        elif s[0] == 'inc':
            reg[s[1]] += 1
        elif s[0] == 'dec':
            reg[s[1]] -= 1
        elif s[0] == 'jnz':
            z = reg[s[1]] if s[1] in reg else s[1]
            if (z != 0):
                r = reg[s[2]] if s[2] in reg else int(s[2])
                if (r == -5 and instr == 9):
                    reg['a'] += reg['d'] * reg['b']
                    reg['c'] = 0
                    reg['d'] = 0
                elif r == -2 and ins[instr-2][0] == 'inc' and ins[instr-1][0] == 'dec' and ins[instr-1][1] == s[1]:
                    register_to_dec = s[1]
                    register_to_add = ins[instr-2][1]
                    reg[register_to_add] += reg[register_to_dec]
                    reg[register_to_dec] = 0
                else:
                    instr += r
                    continue
        elif s[0] == 'tgl':
            x = reg[s[1]] + instr
            if (0 <= x < len(ins)):
                if ins[x][0] == 'inc':
                    ins[x][0] = 'dec'
                elif (ins[x][0] == 'dec') or (ins[x][0] == 'tgl'):
                    ins[x][0] = 'inc'
                elif ins[x][0] == 'jnz':
                    ins[x][0] = 'cpy'
                elif ins[x][0] == 'cpy':
                    ins[x][0] = 'jnz'
                else:
                    assert False, s[x]
        instr += 1
    return reg['a']


print(prog({'a': 7, 'b': 0, 'c': 0, 'd': 0}, instructions))
print(prog({'a': 12, 'b': 0, 'c': 0, 'd': 0}, instructions))
