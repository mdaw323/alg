import fileinput

ex = [l.strip() for l in fileinput.input()][0]


def decompress(l, r, part):
    s = 0
    i = l
    while i < r:
        if (ex[i] == '('):
            j = ex.find(')', i)
            v1, v2 = map(int, ex[i+1:j].split('x'))
            i = j+1 + v1
            s += v2 * (decompress(j+1, i, part) if part == 2 else v1)
        else:
            i += 1
            s += 1
    return s


print(decompress(0, len(ex), 1), decompress(0, len(ex), 2))
