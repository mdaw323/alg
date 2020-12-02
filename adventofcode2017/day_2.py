s = s2 = 0
with open('a2.in') as f:
    for x in f.readlines():
        d = sorted([int(y) for y in x.split("\t")])
        s += max(d) - min(d)
        for i in range(len(d)):
            for b in d[i+1:]:
                if (b % d[i] == 0):
                    s2 += int(b / d[i])
print(s, s2)
