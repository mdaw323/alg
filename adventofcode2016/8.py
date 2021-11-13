import fileinput

w = 50
h = 6
M = []
for x in range(h):
    M.append(['.' for i in range(w)])


def printm():
    for y in range(h):
        print(*M[y], sep='')


def rect(x, y):
    for i in range(x):
        for j in range(y):
            M[j][i] = '#'


def rotate_row(r, v):
    copy_row = [x for x in M[r]]
    for i in range(w):
        M[r][(i+v) % w] = copy_row[i]

def rotate_col(c, v):
    copy_col = [M[i][c] for i in range(h)]
    for i in range(h):
        M[(i+v) % h][c] = copy_col[i]

# rect(3, 2)
# rotate_col(1,11)

lines = [l.strip() for l in fileinput.input()]

for line in lines:
    s = line.split()
    if line.startswith("rect"):
        a,b = map(int,s[1].split('x'))
        # print (line,a,b)
        rect(a,b)
    elif line.startswith("rotate row"):
        a = int(s[2].split('=')[1])
        b = int(s[4])
        # print (line,a,b)
        rotate_row(a,b)
    elif line.startswith("rotate column"):
        a = int(s[2].split('=')[1])
        b = int(s[4])
        # print (line,a,b)
        rotate_col(a,b)
    # printm()
print(sum(row.count('#') for row in M))
printm()
