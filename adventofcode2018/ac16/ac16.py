import re

with open('adventofcode/ac16/input.txt') as f:
    data = f.read()


def addr(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] + data_in[reg[2]]
    return out


def addi(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] + reg[2]
    return out


def mulr(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] * data_in[reg[2]]
    return out


def muli(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] * reg[2]
    return out


def banr(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] & data_in[reg[2]]
    return out


def bani(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] & reg[2]
    return out


def borr(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] | data_in[reg[2]]
    return out


def bori(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]] | reg[2]
    return out


def setr(reg, data_in):
    out = data_in[:]
    out[reg[3]] = data_in[reg[1]]
    return out


def seti(reg, data_in):
    out = data_in[:]
    out[reg[3]] = reg[1]
    return out


def gtir(reg, data_in):
    out = data_in[:]
    out[reg[3]] = 1 if reg[1] > data_in[reg[2]] else 0
    return out


def gtri(reg, data_in):
    out = data_in[:]
    out[reg[3]] = 1 if data_in[reg[1]] > reg[2] else 0
    return out


def gtrr(reg, data_in):
    out = data_in[:]
    out[reg[3]] = 1 if data_in[reg[1]] > data_in[reg[2]] else 0
    return out


def eqir(reg, data_in):
    out = data_in[:]
    out[reg[3]] = 1 if reg[1] == data_in[reg[2]] else 0
    return out


def eqri(reg, data_in):
    out = data_in[:]
    out[reg[3]] = 1 if data_in[reg[1]] == reg[2] else 0
    return out


def eqrr(reg, data_in):
    out = data_in[:]
    out[reg[3]] = 1 if data_in[reg[1]] == data_in[reg[2]] else 0
    return out


known = {'gtrr', 'gtri', 'eqrr', 'eqir', 'eqri', 'gtir', 'muli',
         'setr', 'banr', 'bani', 'seti', 'mulr', 'addi', 'borr'}

fun = {
    0: eqri,
    1: mulr,
    2: gtri,
    3: gtrr,
    4: banr,
    5: addi,
    6: seti,
    7: gtir,
    8: muli,
    9: bori,
    10: setr,
    11: addr,
    12: bani,
    13: borr,
    14: eqir,
    15: eqrr
}


def count_matching_opcodes(registers, after, before):
    sum = set()
    if addr(before, registers) == after:
        sum.add('addr')
    if addi(before, registers) == after:
        sum.add('addi')
    if mulr(before, registers) == after:
        sum.add('mulr')
    if muli(before, registers) == after:
        sum.add('muli')
    if banr(before, registers) == after:
        sum.add('banr')
    if bani(before, registers) == after:
        sum.add('bani')
    if bori(before, registers) == after:
        sum.add('bori')
    if borr(before, registers) == after:
        sum.add('borr')
    if setr(before, registers) == after:
        sum.add('setr')
    if seti(before, registers) == after:
        sum.add('seti')
    if gtir(before, registers) == after:
        sum.add('gtir')
    if gtri(before, registers) == after:
        sum.add('gtri')
    if gtrr(before, registers) == after:
        sum.add('gtrr')
    if eqir(before, registers) == after:
        sum.add('eqir')
    if eqri(before, registers) == after:
        sum.add('eqri')
    if eqrr(before, registers) == after:
        sum.add('eqrr')

    return sum - known


s = 0
regexp = r"Before: \[(.*?)\]\n(.*?)\nAfter:  \[(.*?)\]"

d = {}

for before, res, after in re.findall(regexp, data):
    b = [int(i) for i in before.split(",")]
    a = [int(i) for i in after.split(",")]
    r = [int(i) for i in res.split()]

    if r[0] not in d:
        d[r[0]] = count_matching_opcodes(b, a, r)
    else:
        d[r[0]] = d[r[0]] & count_matching_opcodes(b, a, r)


#for k, v in sorted(d.items()):
    #print(k, sorted(v))


with open('adventofcode/ac16/input_program.txt') as f2:
    lines = f2.readlines()

opc = set()
r = [0,0,0,0]
for line in lines:
    s = [int(x) for x in line.strip().split()]
    f = fun[s[0]]
    r = f(s,r)
    print (r)



