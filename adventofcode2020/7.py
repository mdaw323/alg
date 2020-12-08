import fileinput
import re

lines = [line.strip() for line in fileinput.input()]

E = {}
T = {}
p1 = 0

for line in lines:
    left, right = line.split(" contain ")
    ll = re.findall('(\\w+ \\w+) bag', left)[0]
    rr = re.findall('(\\d+) (\\w+ \\w+) bag', right)
    for c, r in rr:
        if r not in E:
            E[r] = set()
        E[r].add(ll)
        if ll not in T:
            T[ll] = []
        T[ll].append((r, int(c)))

visited = set()

print(T)


def visit(v):
    visited.add(v)
    for e in E.get(v, set()):
        visit(e)


def count_bags(v, cnt):
    if v not in T:
        return cnt
    return cnt + sum([count_bags(e, c * cnt) for e, c in T[v]])


visit('shiny gold')
p2 = count_bags('shiny gold', 1)

print(len(visited) - 1, p2 - 1)
