import fileinput
from collections import deque
from copy import deepcopy

lines = [x.strip() for x in fileinput.input()]

player = [deque(), deque()]


p = 0
for line in lines:
    if not line:
        p += 1
    elif line.startswith("Player"):
        pass
    else:
        player[p].append(int(line))


def play_game(player0: deque, player1: deque, minigame: bool, game: int):
    # print("game:",game, player0, player1)
    pl0 = deque(deepcopy(player0))
    pl1 = deque(deepcopy(player1))
    seen = set()
    seen.add((tuple(pl0), tuple(pl1)))
    while len(pl0) > 0 and len(pl1) > 0:
        p0 = pl0.popleft()
        p1 = pl1.popleft()
        if minigame and (tuple(pl0), tuple(pl1)) in seen:
            # print("xxxxxxxresult", game, (0, pl0))
            return (0, pl0)
        seen.add((tuple(pl0), tuple(pl1)))
        if minigame and len(pl0) >= p0 and len(pl1) >= p1:
            deck0 = deque(list(pl0)[:p0])
            deck1 = deque(list(pl1)[:p1])
            winner, _ = play_game(deck0, deck1, True, game+1)
            if winner == 0:
                pl0 += [p0, p1]
            else:
                pl1 += [p1, p0]
            # minigame
        elif p0 > p1:
            pl0 += [p0, p1]
        else:
            pl1 += [p1, p0]

    if (len(pl0) > 0):
        return (0, pl0)
    else:
        return (1, pl1)


def score(deck):
    s = 0
    for i, v in enumerate(reversed(deck)):
        s += (i+1)*v
    return s


_, deck1 = play_game(player[0], player[1], False, 1)
_, deck2 = play_game(player[0], player[1], True, 1)

print(score(deck1), score(deck2))
