import sys
n, m = map(int, sys.stdin.readline().split())
G = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    u, v = [int(x) for x in sys.stdin.readline().split()]
    G[v].append(u)
    G[u].append(v)

s = 0
i = m = 1
stack = [i]
while (i <= n):
    while (len(stack) > 0):
        v = stack.pop()
        visited[v] = True
        if (v > m):
            m = v
        for e in G[v]:
            if not visited[e]:
                stack.append(e)
                visited[e] = True
    while i <= n and visited[i]:
        i += 1
    if i <= m:
        s += 1
    stack.append(i)
print(s)
