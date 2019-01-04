import re

ip_register = 4
s = 0
regexp = r"(\w*?) (\d+) (\d+) (\d+)"

input = '''seti 123 0 1
bani 1 456 1
eqri 1 72 1
addr 1 4 4
seti 0 0 4
seti 0 3 1
bori 1 65536 5
seti 8586263 3 1
bani 5 255 2
addr 1 2 1
bani 1 16777215 1
muli 1 65899 1
bani 1 16777215 1
gtir 256 5 2
addr 2 4 4
addi 4 1 4
seti 27 8 4
seti 0 1 2
addi 2 1 3
muli 3 256 3
gtrr 3 5 3
addr 3 4 4
addi 4 1 4
seti 25 8 4
addi 2 1 2
seti 17 7 4
setr 2 0 5
seti 7 8 4
eqrr 1 0 2
addr 2 4 4
seti 5 4 4'''

instructons = []


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


fun = {
    'eqri': eqri,
    'mulr': mulr,
    'gtri': gtri,
    'gtrr': gtrr,
    'banr': banr,
    'addi': addi,
    'seti': seti,
    'gtir': gtir,
    'muli': muli,
    'bori': bori,
    'setr': setr,
    'addr': addr,
    'bani': bani,
    'borr': borr,
    'eqir': eqir,
    'eqrr': eqrr
}

for ins, aa, bb, cc in re.findall(regexp, input):
    instructons.append((ins, [-1, int(aa), int(bb), int(cc)]))


def underflow(x):
    data = [x, 0, 0, 0, 0, 0]
    ip = 0
    count_limit = 100000
    oper = set()
    first = last = -1

    while count_limit > 0:
        data[ip_register] = ip
        if ip < 0 or ip >= len(instructons):
            break
        ins, reg = instructons[ip]
        if ip == 19 and data[3] * 256 < data[5]:  # muli 3 256 3
            data[2] += data[5] // 256 - data[3]
            data[3] = data[5] // 256
        if ip == 28 and data[1] not in oper:
            if first == -1:
                first = data[1]
            last = data[1]
            oper.add(data[1])
        data = fun[ins](reg, data)
        ip = data[ip_register] + 1
        count_limit -= 1
    return (first, last)


print(underflow(0))
