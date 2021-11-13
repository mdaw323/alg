import fileinput
import re


lines = [line.strip() for line in fileinput.input()]

def has_abba(s:str):
    for i in range(len(s) - 3):
        t = s[i:i+4]
        # print(t)
        if t[0] == t[3] and t[1] == t[2] and t[0] != t[1]:
            return True
    return False

def get_aba(s:str):
    res = []
    for i in range(len(s) - 2):
        t = s[i:i+3]
        if t[0] == t[2] and t[0] != t[1]:
            res.append(t)
    return res

def invert(s:str):
    return s[1] + s[0] + s[1]

p1 = p2 = 0

for line in lines:
    outside = []
    inside = []
    left = line.split('[')
    for token in left:
        right = token.split(']')
        if len(right) == 2:
            outside.append(right[1])
            inside.append(right[0])
        elif len(right) == 1:
            outside.append(right[0])
    if (all([not has_abba(x) for x in inside])) and any([has_abba(x) for x in outside]):
        p1 += 1

    # print(line)
    abas = []
    p2_cond = False
    for w in outside:
        abas.extend(get_aba(w))
    # print (abas)
    for aba in abas:
        bab = invert(aba)
        for wi in inside:
            if wi.find(bab) >=0:
                p2_cond = True
    if p2_cond:
        p2 += 1


print(p1, p2)
print(invert('bab'))