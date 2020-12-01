def counter(data: [int]):
    cnt = [0] * 2021
    for k in data:
        cnt[k] += 1
    return cnt


def read_data(file: str):
    with open(file) as f:
        return [int(line.strip()) for line in f.readlines()]


def part1(data: [int]):
    cnt = counter(data)
    for a in data:
        cnt[a] -= 1
        if cnt[2020-a] > 0:
            cnt[a] += 1
            return a * (2020 - a)
        cnt[a] += 1


def part2(data: [int]):
    cnt = counter(data)
    for i in range(len(data)):
        cnt[data[i]] -= 1
        for j in range(i):
            cnt[data[j]] -= 1
            x = 2020 - (data[i] + data[j])
            if 0 <= x <= 2020 and cnt[x] > 0:
                return data[i] * data[j] * x
            cnt[data[j]] += 1
        cnt[data[i]] += 1


data = read_data('a1.in')
print(part1(data), part2(data))
