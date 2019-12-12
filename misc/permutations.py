
def heaps_algorithm(a, n):
    if n == 1:
        return [a[:]]
    p = []
    for i in range(n):
        p += heaps_algorithm(a, n-1)
        if n & 1:
            a[0], a[n-1] = a[n-1], a[0]
        else:
            a[i], a[n-1] = a[n-1], a[i]
    return p


a = [0, 1, 2]
print(sorted(heaps_algorithm(a[:],len(a))))

