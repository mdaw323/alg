import fileinput

lines = [line.strip() for line in fileinput.input()]


reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

def prog(reg):
    instr = 0
    while instr < len(lines):
        s = lines[instr].split()
        if s[0] == 'cpy':
            reg[s[2]] = int(reg[s[1]]) if s[1] in reg else int(s[1])
        elif s[0] == 'inc':
            reg[s[1]] += 1
        elif s[0] == 'dec':
            reg[s[1]] -= 1
        elif s[0] == 'jnz':
            z = reg[s[1]] if s[1] in reg else s[1]
            if (z != 0):
                if instr == 20:
                    reg['a'] += reg['d']
                    reg['d'] = 0
                elif instr == 12:
                    reg['a'] += reg['b']
                    reg['b'] = 0
                else:
                    instr += int(s[2])
                    continue
        instr += 1
    return reg['a']
print(prog({'a': 0, 'b': 0, 'c': 0, 'd': 0}), prog({'a': 0, 'b': 0, 'c': 1, 'd': 0}))
