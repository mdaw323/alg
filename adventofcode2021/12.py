import fileinput
from collections import defaultdict


lines = [l.strip() for l in fileinput.input()]

START = 0
END = 1
compress = {'start': START, 'end': END}
visit_once = [False] * 1000
adj = defaultdict(lambda: [])

for line in lines:
    l, r = line.split('-')
    if l not in compress:
        compress[l] = len(compress)
    if r not in compress:
        compress[r] = len(compress)
    visit_once[compress[l]] = l.islower()
    visit_once[compress[r]] = r.islower()
    adj[compress[l]].append(compress[r])
    adj[compress[r]].append(compress[l])


def dfs(seen_mask: int, s: int, visited_twice: bool):
    if s == START and seen_mask != 0:
        return 0
    if s == END:
        return 1
    is_path_broken = seen_mask & (1 << s) and (visit_once[s])
    if is_path_broken and visited_twice:
        return 0
    elif is_path_broken:
        visited_twice = True
    seen_mask |= 1 << s
    return sum([dfs(seen_mask, v, visited_twice) for v in adj[s]])


print(dfs(0, START, True), dfs(0, START, False))
