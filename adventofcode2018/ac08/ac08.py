with open('adventofcode/ac08/input.txt') as f:
    data = [int(x) for x in f.read().strip().split()]


def readNode(ii):
    suma = 0
    nodes = data[ii]
    meta = data[ii+1]
    ii += 2
    for i in range(nodes):
        ii, s = readNode(ii)
        suma += s
    for i in range(meta):
        suma += data[ii + i]
    return (ii+meta, suma)


def readNode2(ii):
    suma = 0
    nodes = data[ii]
    meta = data[ii+1]
    ii += 2
    idx_sum = []

    for i in range(nodes):
        ii, s = readNode2(ii)
        idx_sum.append(s)

    for i in range(meta):
        if (nodes == 0):
            suma += data[ii + i]
        elif 0 <= data[ii + i] - 1 < len(idx_sum):
            suma += idx_sum[data[ii + i] - 1]
    return (ii+meta, suma)


print(readNode(0)[1])
print(readNode2(0)[1])
