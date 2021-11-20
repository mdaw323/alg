from collections import deque
fn = 1364


def bit_count(self):
    return bin(self).count("1")


def is_wall(p):
    x, y, _ = p
    if x < 0 or y < 0:
        return True
    z = x*x + 3*x + 2*x*y + y + y*y + fn
    return True if bit_count(z) % 2 == 1 else False


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dest = (31, 39)
part1 = part2 = None

visited = set()
q = deque()
q.appendleft((1, 1, 0))
while len(q) > 0:
    x, y, d = q.pop()
    if (x, y) == dest:
        part1 = d
    if part2 == None and d > 50:
        part2 = len(visited)

    if part1 != None and part2 != None:
        break
    if ((x, y) in visited):
        continue
    visited.add((x, y))

    for i in range(4):
        p = (dx[i] + x, dy[i] + y, d+1)
        if not is_wall(p):
            q.appendleft(p)

print(part1, part2)
