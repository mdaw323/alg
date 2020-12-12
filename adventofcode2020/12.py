import fileinput
lines = [s.strip() for s in fileinput.input()]

mv = {
    'E': (1, 0),
    'N': (0, 1),
    'W': (-1, 0),
    'S': (0, -1)
}

dr = {
    0: (1, 0),
    90: (0, 1),
    180: (-1, 0),
    270: (0, -1)
}


def dist(x, y):
    return abs(x) + abs(y)


def part1():
    pos = (0, 0)
    angle = 0

    for cmd in lines:
        # print (cmd)
        c, d = cmd[0], int(cmd[1:])
        if c in 'NEWS':
            pos = (pos[0] + mv[c][0] * d, pos[1] + mv[c][1] * d)
        elif c == 'F':
            pos = (pos[0] + dr[angle][0] * d, pos[1] + dr[angle][1] * d)
        elif c == 'R':
            angle = (360 + angle - d) % 360
        elif c == 'L':
            angle = (angle + d) % 360
    return dist(*pos)


def part2():
    waypoint = (10, 1)
    pos = (0, 0)
    for cmd in lines:
        # print (cmd)
        c, d = cmd[0], int(cmd[1:])
        if c in 'NEWS':
            waypoint = (waypoint[0] + mv[c][0] * d, waypoint[1] + mv[c][1] * d)
        elif c == 'F':
            pos = (pos[0] + waypoint[0] * d, pos[1] + waypoint[1] * d)
        elif c == 'L':
            angle = d
            while angle != 0:
                waypoint = (waypoint[1] * -1, waypoint[0])
                angle = angle - 90
        elif c == 'R':
            angle = d
            while angle != 0:
                waypoint = (waypoint[1], -1 * waypoint[0])
                angle = angle - 90
    return dist(*pos)


print(part1(), part2())
