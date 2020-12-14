import fileinput
from collections import defaultdict
lines = [x.strip() for x in fileinput.input()]
cmds = [x.split("=") for x in lines]


def merge_masks(adress: int, mask: list):
    m = list(f'{adress:036b}')
    for i in range(len(mask)):
        if mask[i] in 'X1':
            m[i] = mask[i]
    return m


mem1 = defaultdict(lambda _: 0)
mem2 = defaultdict(lambda _: 0)
s1 = s2 = 0
or_mask = 0
and_mask = 1
mask = ''
for cmd, value in cmds:
    if cmd.startswith("mem"):
        v = int(value)
        p = int(cmd.strip()[4:-1])
        s1 -= mem1.get(p, 0)
        mem1[p] = (v & and_mask) | or_mask
        s1 += mem1[p]
        c = mask.count('X')
        merged_mask = merge_masks(p, list(mask))
        for i in range(1 << c):
            m = merged_mask[:]
            for j in range(c):
                r = str((i >> j) & 1)
                pos = m.index('X')
                m[pos] = r
            ad = int(''.join(m), 2)
            s2 += v - mem2.get(ad, 0)
            mem2[ad] = v

    elif cmd.startswith("mask"):
        v = str(value.strip())
        or_mask = int(v.replace('X', '0'), base=2)
        and_mask = int(v.replace('X', '1'), base=2)
        mask = v


print(s1, s2)
