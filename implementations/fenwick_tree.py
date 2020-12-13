

def update(A, n, idx, value):
    print(A, n, idx, value)
    while (idx <= n):
        A[idx] += value
        idx += idx & -idx


def query(A, idx):
    s = 0
    while idx > 0:
        s += A[idx]
        idx -= idx & -idx
    return s


A1 = [1, 2, 3, 4, 5, 6]
BIT = [0]*7

for i, a in enumerate(A1):
    update(BIT, len(A1), i+1, a)

print(A1)

for i in range(6):
    print(query(BIT, i))
