import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(100000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]


# routes = []
# cities = set()
adj = defaultdict(lambda:[])
for nr, line in enumerate(lines):
    a, _, b, _, d = line.split()
    d = int(d)
    # cities.add(a)
    # cities.add(b)
    # routes.append((d, a, b))
    adj[a].append((b,d))
    adj[b].append((a,d))


# routes.sort()
# rank = {}
# parent = {}
# for r, city in enumerate(cities):
#     rank[city] = r
#     parent[city] = city


# def find(city):
#     while city != parent[city]:
#         city = parent[city]
#     return city


# def same(a, b):
#     return find(a) == find(b)


# def union(a, b):
#     print (f"union {a}, {b}")
#     a = find(a)
#     b = find(b)
#     if rank[a] < rank[b]:
#         a, b = b, a
#     rank[a] += rank[b]
#     parent[b] = a

# for d, a, b in routes:
#     if not same(a,b):
#         union(a,b)
#         p1 += d

MINX = -1
MAXX = 999999999
dst = 999999999


def dfs(path, s, distance):
    # print (path,s, distance)
    if s in set(path):
        return (MINX, MAXX)
    p = tuple(list(path) + [s])
    if len(p) == len(adj):
        return (distance, distance)
    else:
        # print (adj[s])
        mi = MINX
        ma = MAXX
        for u,d in adj[s]:
            t = dfs(p, u, distance + d)
            mi = max(t[0], mi)
            ma = min(t[1], ma)
            # print (u,d)
        return (mi,ma)
        # return min([dfs(p, u, distance + d) for u , d in adj[s]])


p1 = MAXX
p2 = MINX
for city in adj:
    mi,ma =  dfs(set(), city, 0)
    p1 = min(p1,ma)
    p2 = max(p2,mi)


print(p1, p2)
