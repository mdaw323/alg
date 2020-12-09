import fileinput

numbers = [int(x.strip()) for x in fileinput.input()]


def find_first_not_a_sum(PA):
    cache = {}
    for i in range(PA):
        j = numbers[i]
        cache[j] = cache.get(j, 0) + 1

    for i in range(PA, len(numbers)):
        n = numbers[i]
        seen = False
        for j in range(i-PA, i):
            # print(j)
            a = numbers[j]
            b = n - a
            seek = 2 if a == b else 1
            if cache.get(b, 0) >= seek:
                seen = True
                assert a + b == n
                break
        if not seen:
            return n
        cache[numbers[i - PA]] = cache[numbers[i - PA]] - 1
        cache[n] = cache.get(n, 0) + 1


p1 = find_first_not_a_sum(25)

i = j = 0
s = numbers[0]
while (s != p1):
    if s > p1:
        s -= numbers[i]
        i += 1
    elif s < p1:
        j += 1
        s += numbers[j]

p2 = min(numbers[i:j+1]) + max(numbers[i:j+1])
print(p1, p2)
