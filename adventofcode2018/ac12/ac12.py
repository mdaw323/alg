import re

with open('adventofcode/ac12/input.txt') as f:
    initial = list(f.readline().strip())[15:]
    raw = f.read()

#  .##.. => .
rgx = r"([.#]+) => ([.#])"
d = dict()

for left, right in re.findall(rgx, raw):
    d[ left ] = right

state = dict()

offset = 5
drange = 100
mem = []
def count_result(prev_gen):
    s = 0
    for i in range(len(prev_gen)):
        if prev_gen[i] == '#':
            s += i - offset
    return s


prev_gen = ['.']*5 + initial + ['.']*5
next_gen = prev_gen[:]
#print (''.join(prev_gen))
for gen in range(drange):
    v = ''.join(prev_gen).strip('.')
    if v in state:
        print (gen, state[v],offset, count_result(prev_gen))
    else:
        state[v] = gen
    for i in range(2,len(prev_gen) - 2):
        k = ''.join(prev_gen[i-2:i+3])
        if (k in d):
            next_gen[i] = d[k]
        else:
            next_gen[i] = '.'
    
    #print (gen+1, ''.join(next_gen))
    prev_gen = ['.']*5 + next_gen + ['.']*5
    next_gen = prev_gen[:]
    offset+=5

exp = 50000000000
#exp = 93

print (8646 + (exp -92) * 72 )