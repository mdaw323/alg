from collections import deque
# import networkx as nx
# import matplotlib.pyplot as plt
M = []

with open('a18b.in') as f:
    for line in f.readlines():
        M.append([x for x in line.strip()])


def printMaze():
    for L in M:
        print(*L, sep='')


keys = set()
doors = set()
key_pos = {}
# G = nx.Graph()

available_keys = set([chr(x) for x in range(
    ord('a'), ord('z') + 1)] + ['@', '1', '2', '3', '4'])
available_doors = set([chr(x) for x in range(ord('A'), ord('Z') + 1)])
for y, L in enumerate(M):
    for x, c in enumerate(L):
        if c in available_keys:
            key_pos[c] = (y, x)
# printMaze()
# M[position[0]][position[1]] = '.'
printMaze()


print(sorted(available_keys))

E = {}
P = []


def bfs(pos):
    queue = deque()
    queue.append((pos, set(), 0, set([pos])))
    starting_vector = M[pos[0]][pos[1]]
    results = []
    d = 0
    while len(queue) > 0:
        top, dep, d, visited = queue.popleft()
        for v in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            n = (top[0] + v[0], top[1] + v[1])
            c = M[n[0]][n[1]]
            if c != '#' and n not in visited:
                visited.add(n)
                if c in available_doors:

                    dep = dep | set(c.lower())

                    queue.append((n, dep, d+1, visited))
                elif c in available_keys:
                    # print("found key", c, n, d[n])
                    # results.append((0, d[n], c, n))
                    if c > starting_vector:
                        # queue.append((n, dep, d, visited))
                        # print("edge", starting_vector, c, d+1, dep)
                        E[starting_vector].append((c, d+1, dep))
                        E[c].append((starting_vector, d+1, dep))
                        # G.add_edge(starting_vector, c,                                weight=d+1, dependencies=dep)
                elif c == '.':
                    queue.append((n, dep, d+1, visited))
    return results


for v, x in sorted(key_pos.items()):
    E[v] = []

for v, x in sorted(key_pos.items()):
    #print(v, x)
    bfs(x)


# print (E)
def part1():
    queue = [[] for i in range(10000)]
    visited = set()
    queue[0].append(('@', ('@')))
    d = 0
    while d < 9999:
        # print (d)
        for tail, path in queue[d]:
            if (tail, path) not in visited:
                if len(path) == len(key_pos):
                    print("found solution", path, d)
                    d = 9999999
                    break
                visited.add((tail, path))
                path_set = set(path)
                for neighbour, distance, dependecies in E[tail]:
                    if len(dependecies - path_set) == 0:
                        queue[d + distance].append((neighbour,
                                                    tuple(path_set | set(neighbour))))
        d += 1


def part2():
    queue = [[] for i in range(10000)]
    visited = set()
    queue[0].append((tuple(set(['1', '2', '3', '4'])),
                     (tuple(set(['1', '2', '3', '4'])))))
    d = 0
    while d < 9999:
        # print (d)
        for tails, path in queue[d]:
            if (tails, path) not in visited:
                if len(path) == len(key_pos):
                    print("found solution", path, d)
                    d = 9999999
                    break
                visited.add((tails, path))
                path_set = set(path)
                tails_set = set(tails)
                for tail in list(tails):
                    for neighbour, distance, dependecies in E[tail]:
                        if len(dependecies - path_set) == 0:
                            tt = (tails_set - set(tail)) | set(neighbour)
                            queue[d + distance].append((tuple(tt),
                                                        tuple(path_set | set(neighbour))))
        d += 1


part2()
