import fileinput
import sys
sys.setrecursionlimit(15000000)

E = []
for i in range(200):
    E.append([])


# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

M = {}
words = []


lines = [x.strip() for x in fileinput.input()]
for line in lines:
    print(line)
    if ":" in line:
        ll, r = line.split(": ")
        ll = int(ll)
        if r == '"a"':
            M[ll] = 'a'
        elif r == '"b"':
            M[ll] = 'b'
        else:
            x = r.split("|")
            print(x)
            if (len(x)) == 2:
                a, b = x
                a = [int(s) for s in a.split()]
                b = [int(s) for s in b.split()]
                assert len(a) <= 3
                assert len(b) <= 3
                E[ll].append(a)
                E[ll].append(b)

            elif (len(x) == 1):
                a = [int(s) for s in x[0].split()]
                assert len(a) <= 3
                E[ll].append(a)
    else:
        if line:
            words.append(line)


mem = {}


def dfs(x, le, ri, w):
    if ((x, le, ri) in mem):
        return mem[(x, le, ri)]
    if len(E[x]) > 0:
        for e in E[x]:
            if len(e) == 1:
                if dfs(e[0], le, ri, w):
                    mem[(x, le, ri)] = True
                    return True
            elif len(e) == 2:
                for i in range(le, ri+1):
                    if (dfs(e[0], le, i, w) and dfs(e[1], i+1, ri, w)):
                        mem[(x, le, ri)] = True
                        return True
            elif len(e) == 3:
                for i in range(le, ri+1):
                    for j in range(i+1, ri + 1):
                        if (dfs(e[0], le, i, w)
                                and dfs(e[1], i+1, j, w)
                                and dfs(e[2], j+1, ri, w)):
                            mem[(x, le, ri)] = True
                            return True
    else:
        mem[(x, le, ri)] = (le == ri and words[w][le] == M[x])
        return mem[(x, le, ri)]
    mem[(x, le, ri)] = False
    return False


# ababbb
res = []
for i in range(len(words)):
    mem = {}
    res.append(dfs(0, 0, len(words[i]) - 1, i))

print(res)
print(res.count(True), len(words))
# print(dfs(0, 0, 5, 0))
# for i, e in enumerate(E):
#     print(i, e)
# print(M, words, mem)
