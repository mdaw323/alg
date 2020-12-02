directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
all_directions = directions + [(-1, -1), (1, -1), (-1, 1), (1, 1)]


def part1(ll: int):
    d = 0
    direction = directions[d % 4]
    next_dir = directions[(d+1) % 4]

    rooms = {(0, 0)}
    x, y = 1, 0
    for i in range(2, ll + 1):
        rooms.add((x, y))
        if ll == i:
            return abs(x) + abs(y)
        if (x+next_dir[0], y+next_dir[1]) not in rooms:
            d += 1
            direction = directions[d % 4]
            next_dir = directions[(d+1) % 4]
        x, y = x + direction[0], y + direction[1]
    return 0


def part2(ll: int):
    d = 0
    direction = directions[d % 4]
    next_dir = directions[(d+1) % 4]
    rooms = {(0, 0): 1}
    x, y = 1, 0

    while True:
        s = 0
        for dd in all_directions:
            zz = (x + dd[0], y + dd[1])
            if zz in rooms:
                s += rooms[zz]

        rooms[(x, y)] = (s)
        if s > ll:
            return s
        if (x+next_dir[0], y+next_dir[1]) not in rooms:
            d += 1
            direction = directions[d % 4]
            next_dir = directions[(d+1) % 4]
        x, y = x + direction[0], y + direction[1]


if __name__ == "__main__":
    print(part1(265149), part2(265149))
