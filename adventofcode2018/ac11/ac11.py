from collections import defaultdict

serial_number = 7689
part_sum_row = defaultdict(lambda: 0, {})
part_sum = defaultdict(lambda: 0, {})
max_all_sizes = max_3_size = (-1, -1, -100, 0)


def cpl(x, y):
    rack_id = x + 10
    return (rack_id * y + serial_number) * rack_id % 1000 // 100 - 5


for x in range(1, 301):
    for y in range(1, 301):
        part_sum_row[(x, y)] = part_sum_row[(x-1, y)] + cpl(x, y)
        part_sum[(x, y)] = part_sum[(x, y-1)] + part_sum_row[(x, y)]


for size in range(1, 301):
    for x in range(size, 301):
        for y in range(size, 301):
            pwl = part_sum[(x, y)] - part_sum[(x - size, y)] - \
                (part_sum[(x, y-size)] - part_sum[x-size, y-size])
            if max_all_sizes[2] < pwl:
                max_all_sizes = (x-size + 1, y-size + 1, pwl, size)
            if size == 3 and max_3_size[2] < pwl:
                max_3_size = (x-size + 1, y-size + 1, pwl, size)

print(max_3_size)
print(max_all_sizes)
