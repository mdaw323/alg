from utils import *


def do_opcodes(D, noun, verb):
    D[1] = noun
    D[2] = verb
    for i in range(len(D)//4):
        p = i*4
        if D[p] in opcodes:
            opcodes[D[p]](D, p)
        elif D[p] == 99:
            break
        else:
            raise AssertionError("invalid opcode")
    return D


def find_opcode_noun_and_verb(D, value):
    for n in range(100):
        for v in range(100):
            if (do_opcodes(D[:], n, v)[0] == value):
                return n * 100 + v


G = []
s = 0
with open("a2.in") as f:
    for line in f:
        sl = line.strip()
        G = ints(sl)

print(do_opcodes(G[:], 12, 2)[0])
print(find_opcode_noun_and_verb(G[:], 19690720))
