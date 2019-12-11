I = []
m = 25*6
D = {}
with open('a8.in') as f:
    line = f.readline().strip()
    layer = []
    for c in line:
        layer.append(int(c))
        if len(layer) == m:
            I.append(layer)
            layer = []

for i in I:
    assert len(i) == m


def count(A, k):
    s = 0
    for c in A:
        if k == c:
            s += 1
    return s


min_zeroes_layer = min([(count(l, 0), i) for i, l in enumerate(I)])[1]
print(count(I[min_zeroes_layer], 1) * count(I[min_zeroes_layer], 2))

image = [2] * m
for l in I:
    for i, k in enumerate(l):
        if image[i] == 2:
            image[i] = k

print(image)

s = ''
for i, d in enumerate(image):
    if (i % 25 == 0):
        print(s)
        s = ''
    s = s + ('⬛' if d == 1 else ' ')
print(s)

# LBRCE
