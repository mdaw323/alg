import fileinput
from itertools import permutations
from collections import deque

lines = [line.strip() for line in fileinput.input()]

used = {}
available = {}
size = {}
nodes = []

for line in lines:
    if line.startswith("/dev"):
        filesystem, fsize, fused, favail, fuse = line.split()
        fs = filesystem.split("-")
        p = (int(fs[1][1:]), int(fs[2][1:]))
        fsize = int(fsize[:-1])
        fused = int(fused[:-1])
        favail = int(favail[:-1])
        fuse = int(fuse[:-1])
        used[p] = fused
        available[p] = favail
        size[p] = fsize
        nodes.append(p)
        # print(filesystem,p, fsize, fused, favail, fuse)

# print(used)

part1 = 0

empty_node = None
static_nodes = set()

for p1, p2 in permutations(nodes, 2):
    # print (used[p1], available[p2])
    if used[p1] > 0 and used[p1] <= available[p2]:
        empty_node = p2
        # print (p1,p2,used[p1],available[p2])
        part1 += 1

for node in nodes:
    if size[node] > 100:
        static_nodes.add(node)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def part2(s):
    starting = (0, 0)
    goal = (37, 0)
    q = deque()
    seen = set()
    q.appendleft((0, goal, s))
    while (len(q) > 0):
        d, goal, empty_node = q.pop()
        # print(d, goal, empty_node)
        if goal == starting:
            return d
        if (goal, empty_node) in seen:
            continue
        seen.add((goal, empty_node))
        for i in range(4):
            x = empty_node[0] + dx[i]
            y = empty_node[1] + dy[i]
            p2 = (x, y)
            if (0 <= x <= 37) and (0 <= y <= 25) and (p2 not in static_nodes):
                if p2 != goal:
                    q.appendleft((d+1, goal, p2))
                else:
                    q.appendleft((d+1, empty_node, p2))


print(part1, part2(empty_node))
