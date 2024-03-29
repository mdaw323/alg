import fileinput as fi

Mx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
My = {'L': 0, 'R': 0, 'U': -1, 'D': 1}

P1 = [
    ['', '', '', '', '', ''],
    ['', '1', '2', '3', ''],
    ['', '4', '5', '6', ''],
    ['', '7', '8', '9', ''],
    ['', '', '', '', '', ''],
]


P2 = [
    ['', '', '', '', '', '', ''],
    ['', '', '', '1', '', '', ''],
    ['', '', '2', '3', '4', '', ''],
    ['', '5', '6', '7', '8', '9', ''],
    ['', '', 'A', 'B', 'C', '', ''],
    ['', '', '', 'D', '', '', ''],
    ['', '', '', '', '', '', ''],
]

def solve(p, V):
    data = [x.strip() for x in fi.input()]
    res = ''
    for line in data:
        for c in line:
            np = [p[0] + Mx[c], p[1] + My[c]]
            if (V[np[1]][np[0]] != ''):
                p = np
        res = res + V[p[1]][p[0]]
    return res

print(solve([2, 2], P1))
print(solve([1, 3], P2))
