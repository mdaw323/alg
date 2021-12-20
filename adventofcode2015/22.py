#!/usr/bin/python3

import itertools
import sys
from enum import IntEnum
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10000)

dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE
p1 = p2 = 0


class Spell(IntEnum):
    MISSILE = 0
    DRAIN = 1
    SHIELD = 2
    POISON = 3
    RECHARGE = 4


spells = {
    Spell.MISSILE: (53, 0, 4),
    Spell.DRAIN: (73, 0, 2),
    Spell.SHIELD: (113, 6, 7),
    Spell.POISON: (173, 6, 3),
    Spell.RECHARGE: (229, 5, 101),
}

boss_hit_points = 71
boss_damage = 10

INF = 10**10

# @lru_cache(maxsize=None)
def fight(hp, mana, mana_spent, boss_hp, shield, poison, recharge, player_turn=True, turn = 0, acts = []):
    if player_turn:
        hp -= 1
    if hp <=0:
        return INF
    armor = 0
    if shield > 0:
        armor = spells[Spell.SHIELD][2]
        shield -= 1
    if poison > 0:
        boss_hp -= spells[Spell.POISON][2]
        poison -= 1
    if recharge > 0:
        mana += spells[Spell.RECHARGE][2]
        recharge -= 1
    if boss_hp <= 0:
        # print (f"{'PLAYER' if player_turn else 'BOSS'} turn {turn}  hp = {hp}, mana {mana}, boss_hp {boss_hp}, spent= {mana_spent}, others",shield, poison, recharge, acts)
        return mana_spent


    if player_turn:
        actions = [INF]
        if (mana >= spells[Spell.MISSILE][0]):
            s = spells[Spell.MISSILE]
            actions.append(fight(hp, mana - s[0],
                                 mana_spent + s[0],
                                 boss_hp - s[2],
                                 shield, poison, recharge, not player_turn, turn+1, acts + [Spell.MISSILE]))
        if (mana >= spells[Spell.DRAIN][0]):
            s = spells[Spell.DRAIN]
            actions.append(fight(hp + s[2], mana - s[0],
                                 mana_spent + s[0],
                                 boss_hp - s[2],
                                 shield, poison, recharge, not player_turn, turn+1, acts + [Spell.DRAIN]))

        if (mana >= spells[Spell.SHIELD][0] and shield == 0):
            s = spells[Spell.SHIELD]
            actions.append(fight(hp, mana - s[0],
                                 mana_spent + s[0],
                                 boss_hp,
                                 s[1], poison, recharge, not player_turn, turn+1,acts + [Spell.SHIELD]))

        if (mana >= spells[Spell.POISON][0] and poison == 0):
            s = spells[Spell.POISON]
            actions.append(fight(hp, mana - s[0],
                                 mana_spent + s[0],
                                 boss_hp,
                                 shield, s[1], recharge, not player_turn, turn+1, acts + [Spell.POISON]))

        if (mana >= spells[Spell.RECHARGE][0] and recharge == 0):
            s = spells[Spell.RECHARGE]
            actions.append(fight(hp, mana - s[0],
                                 mana_spent + s[0],
                                 boss_hp,
                                 shield, poison, s[1], not player_turn, turn+1, acts + [Spell.RECHARGE]))
        return min(actions)

    else:
        hp -= max(1, boss_damage - armor)
        if hp <= 0:
            return INF
        else:
            return fight(hp, mana, mana_spent, boss_hp,shield,poison,recharge, not player_turn, turn+1, acts)

boss_hit_points = 71
boss_damage = 10
player_hp = 50
player_mana = 500


# boss_hit_points = 14
# boss_damage = 8
# player_hp = 10
# player_mana = 250

# print([spells[x] for x in Spell])
print(fight(player_hp,player_mana, 0, boss_hit_points, 0,0,0))
