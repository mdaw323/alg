from collections import deque
M = []

with open('a18.in') as f:
    for line in f.readlines():
        M.append([x for x in line.strip()])


def printMaze():
    for L in M:
        print(*L, sep='')
    print(position)

keys = set()
doors = set()
key_pos = {}

for y, L in enumerate(M):
    for x, c in enumerate(L):
        if c == '@' or c.islower():            
            key_pos[c] = (y, x)
# printMaze()
position = key_pos['@']
M[position[0]][position[1]] = '.'
printMaze()



def bfs(pos):
    d = {}  
    k = -1  
    for i in range(4):
        d[(pos,i)] = 0
    
    queue = deque()
    queue.append((pos, -1, set()))
    results = []
    while len(queue) > 0:
        top, color, dep = queue.popleft()
        for v in [[-1, 0], [1, 0], [0, 1], [0, -1]]:

            n = (top[0] + v[0], top[1] + v[1])
            c = M[n[0]][n[1]]
            if c != '#' and (n, tuple(dep)) not in d:
                d[(n, tuple(dep))] = d[(top, tuple(dep))] + 1                
                if c.isupper():                    
                    # print("can open door", c, n, d[n])
                    results.append((1, d[n], c, n))
                    # queue.append(n)
                elif c.islower():
                    # print("found key", c, n, d[n])
                    results.append((0, d[n], c, n))
                    queue.append(n)
                elif c == '.':
                    queue.append(n)
    return results


# suma = 0
# results = bfs(position)
# while len(results) > 0:
#     _, s, c, p = min(results)
#     print(results)
#     if (c.isupper()):
#         doors.add(c)
#     else:
#         keys.add(c)
#     suma += s
#     M[p[0]][p[1]] = '.'
#     position = p
#     # printMaze()
#     results = bfs(position)
# # print (bfs(position))
# # printMaze()
# print(suma)
