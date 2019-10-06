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

ip = 0
ip_register = 3
s = 0
regexp = r"(\w*?) (\d+) (\d+) (\d+)"

input = '''addi 3 16 3
seti 1 0 4
seti 1 0 1
mulr 4 1 5
eqrr 5 2 5
addr 5 3 3
addi 3 1 3
addr 4 0 0
addi 1 1 1
gtrr 1 2 5
addr 3 5 3
seti 2 9 3
addi 4 1 4
gtrr 4 2 5
addr 5 3 3
seti 1 2 3
mulr 3 3 3
addi 2 2 2
mulr 2 2 2
mulr 3 2 2
muli 2 11 2
addi 5 4 5
mulr 5 3 5
addi 5 16 5
addr 2 5 2
addr 3 0 3
seti 0 8 3
setr 3 2 5
mulr 5 3 5
addr 3 5 5
mulr 3 5 5
muli 5 14 5
mulr 5 3 5
addr 2 5 2
seti 0 0 0
seti 0 0 3'''

instructons = []

for ins, aa,bb,cc in re.findall(regexp,input):
    instructons.append( (ins, [-1, int(aa),int(bb),int(cc)]) )
    
print (instructons[0])
print (instructons[7])

data = [0] * 6
data[0] = 1
d = 100
while True:
    data[ip_register] = ip
    
    if (ip < 0 or ip >= len(instructons) ):
        break
    ins, reg = instructons[ip]
    copyData = data[:]
    data = fun[ins](reg,data)    
    
    if d % 1 == 0:
        print (copyData, ins, reg[1:], data)
    
    ip = data[ip_register]
    ip+=1
    d-=1
    
print ("res ", data,d)    
