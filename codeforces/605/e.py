from collections import deque
n = int(input())
A = [int(x) for x in input().strip().split()]

distance = [-1] * n
edge = [[] for i in range(n)]

def bfs():
    queue = deque()
    for v in range(n):
        if distance[v] != -1:
            queue.append(v)    
    while len(queue) > 0:
        v = queue.popleft()
        for e in edge[v]:
            if distance[e] == -1:
                queue.append(e)
                distance[e] = distance[v] + 1


for i in range(n):
    for m in [i - A[i], i + A[i]]:
        if 0 <= m < n:
            if (A[i] & 1) == (A[m] & 1):
                edge[m].append(i)
            else:
                distance[i] = 1

bfs()
print(*distance)
