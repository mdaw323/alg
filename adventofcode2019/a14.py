import math
import networkx as nx

def read(s):
    a, b = s.strip().split()
    return (int(a), str(b))

reactions = {}
rec_count = {}
G = nx.DiGraph()
with open('a14.1') as f:
    for line in f.readlines():
        rec, res = line.strip().split('=>')
        cc, pp = read(res)
        rec_count[pp] = cc
        reactions[pp] = {}
        for cr, pr in [read(s) for s in rec.split(',')]:
            G.add_edge(pp, pr)
            reactions[pp][pr] = cr

def reduce_reaction(react):
    reaction = react.copy()
    for product in nx.topological_sort(G):
        k = rec_count[product]
        if product in reaction:
            iterations = math.ceil(reaction[product] / k)
            for rr, cc in reactions[product].items():
                if rr in reaction:
                    reaction[rr] += iterations * cc
                else:
                    reaction[rr] = iterations * cc
            del reaction[product]
            return reaction

# part1
reaction = reduce_reaction({"FUEL": 1})
while (len(reaction) > 1):
    reaction = reduce_reaction(reaction)
print(reaction['ORE'])

# part2
search_range = [0, 1000000000000]
while search_range[0]+1 < search_range[1]:
    half = (search_range[0] + search_range[1]) // 2
    reaction = reduce_reaction({"FUEL": half})
    while (len(reaction) > 1):
        reaction = reduce_reaction(reaction)
    if reaction['ORE'] < 1000000000000:
        search_range[0] = half
    else:
        search_range[1] = half
print(search_range[0])
