#!/usr/bin/python3

import itertools
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10000)

dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE
p1 = p2 = 0


# Weapons:    Cost  Damage  Armor
weapons = [
    ("Dagger", 8,     4,     0),
    ("Shortsword", 10,     5,       0),
    ("Warhammer", 25,     6,       0),
    ("Longsword", 40,     7,       0),
    ("Greataxe", 74,     8,       0),
]


# Armor:      Cost  Damage  Armor
armors = [
    ("none", 0,     0,       0),
    ("Leather", 13,     0,       1),
    ("Chainmail", 31,     0,       2),
    ("Splintmail", 53,     0,       3),
    ("Bandedmail", 75,     0,       4),
    ("Platemail", 102,     0,       5),
]
# Rings:      Cost  Damage  Armor
rings = [
    ("None 1", 0,     0,       0),
    ("None 2", 0,     0,       0),
    ("Damage +1", 25,     1,       0),
    ("Damage +2", 50,     2,       0),
    ("Damage +3", 100,     3,       0),
    ("Defense +1", 20,     0,       1),
    ("Defense +2", 40,     0,       2),
    ("Defense +3", 80,     0,       3),
]

boss_hit_points = 109
boss_damage = 8
boss_armor = 2

counter = 0

@lru_cache(maxsize=None)
def simulate_fight(hp, damage, armor, boss_hp, player_turn=True):
    global counter
    counter+=1
    # print (hp, damage, armor, boss_hp, player_turn)
    if player_turn:
        boss_hp -= max(1, damage - boss_armor)
        if boss_hp <= 0:
            return True
    else:
        hp -= max(1, boss_damage - armor)
        if hp <= 0:
            return False
    return simulate_fight(hp, damage, armor, boss_hp, not player_turn)


player_hp = 100

boss_wins = []
players_wins = []
for weapon in weapons:
    for armor in armors:
        for ring1, ring2 in combinations(rings, 2):
            cost = weapon[1] + armor[1] + ring1[1] + ring2[1]
            dmg = weapon[2] + armor[2] + ring1[2] + ring2[2]
            arm = weapon[3] + armor[3] + ring1[3] + ring2[3]
            if simulate_fight(player_hp, dmg, arm, boss_hit_points, True):
                players_wins.append(
                    (cost, weapon[0], armor[0], ring1[0], ring2[0]))
            else:
                boss_wins.append(
                    (cost, weapon[0], armor[0], ring1[0], ring2[0]))


print(min(players_wins)[0], max(boss_wins)[0])
