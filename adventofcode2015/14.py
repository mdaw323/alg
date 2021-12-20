import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]


points = defaultdict(lambda: 0)
total_distance = 2503
distances = []
reindeers = set()
for nr, line in enumerate(lines):
    a, _, _, speed, _, _, flying_time, *_, rest_time, _ = line.split()
    speed = int(speed)
    flying_time = int(flying_time)
    rest_time =int(rest_time)
    reindeers.add(a)
    for i in range(1,total_distance+1):
        cycles = i // (flying_time + rest_time)
        rest = i % (flying_time + rest_time)
        distance = cycles * speed * flying_time + min(rest, flying_time) * speed
        dd[(a,i)] = distance


for i in range(1,total_distance+1):
    results = []
    for r in reindeers:
        results.append((dd[(r,i)],r) )
    results.sort(reverse=True)
    p , winner = results[0]
    points[winner] +=1
    if i == total_distance:
        p1 = p


print(p1, max(points.values()))
