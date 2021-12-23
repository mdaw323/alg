import fileinput
from heapq import heappop, heappush
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

def is_room_ready(room_id, room):
    assert (0<=room_id<=3)
    for i in range(4):
        if room[i] != (room_id+1) and room[i] != 0:
            # print(room_id, room, False)
            return False
    # print(room_id, room, True)
    return True

def get_first_from_room(room):
    for i in range(4):
        if room[i]!=0:
            return (room[i], i, (room[:i] + tuple([0]) + room[i+1:]))
    return None

score = {
    1: 1,
    2: 10,
    3: 100,
    4: 1000
}

def moves_from_rooms(rooms, spaces):
    generated_moves = []
    for i in range(4):
        room = rooms[i]
        if not is_room_ready(i, room):
            gf = get_first_from_room(room)

            if gf:
                # print(gf)
                amphipod, dist, new_room = gf

                new_rooms = rooms[:i] + tuple([new_room]) + rooms[i+1:]
                can_board = is_room_ready(amphipod-1, rooms[amphipod-1])
                moves = possible_moves_from_room(i, spaces, amphipod-1, can_board)
                # print(f"moves: {moves}")
                for space_pos,d in moves:
                    new_spaces = spaces[:space_pos] + tuple([amphipod]) + spaces[space_pos+1:]
                    new_dist = d * 2
                    if space_pos == 0 or space_pos == 6:
                        new_dist-=1
                    energy = score[amphipod] * (dist + new_dist)
                    generated_moves.append((new_rooms, new_spaces, energy))
    return generated_moves


def moves_from_spaces(rooms, spaces):
    generated_moves = []
    for space_pos, amphipod in enumerate(spaces):
        if amphipod > 0:
            can_board = board(amphipod, rooms[amphipod -1])
            d = possible_moves_from_space(amphipod -1 , space_pos, spaces)
            if d and can_board:
                room_id = amphipod -1
                new_room, dist = can_board
                new_rooms = rooms[:room_id] + tuple([new_room]) + rooms[room_id+1:]
                new_spaces = spaces[:space_pos] + tuple([0]) + spaces[space_pos+1:]
                new_dist = d * 2
                if space_pos == 0 or space_pos == 6:
                    new_dist-=1
                energy = score[amphipod] * (dist + new_dist)
                generated_moves.append( (new_rooms, new_spaces, energy) )
                # print(f"board ",amphipod,space_pos, d, new_room, dist)

    return generated_moves

def check_if_win(rooms):
    for i in range(4):
        room = rooms[i]
        for j in range(4):
            if room[j] != i+1:
                return False
    return True

def board(amphipod, room):
    # print("board", amphipod, room)
    if not is_room_ready(amphipod-1,room):
        return None
    for i in [3,2,1,0]:
        if room[i] == 0:
            return (room[:i] + tuple([amphipod]) + room[i+1:], i)

def possible_moves_from_room(room_id, spaces, boarding_room, can_board):
    moves= []
    l = room_id + 1
    r = room_id + 2

    bl = boarding_room + 1
    br = boarding_room + 2

    dist = 1

    while (l>=0 and spaces[l] == 0):
        move = (l, dist)
        moves.append(move)
        if can_board and l in([bl,br]):
            return [move]
        dist+=1
        l-=1
    dist = 1

    while (r<=6 and spaces[r] == 0):
        move = (r, dist)
        moves.append(move)
        if can_board and r in([bl,br]):
            return [move]
        dist+=1
        r+=1
    return moves

def possible_moves_from_space(room_id, space, spaces):
    # print("possible_moves_from_space", room_id, space, spaces)
    l = room_id + 1
    r = room_id + 2
    dist = 1
    while (space == l or (l>=0 and spaces[l] == 0)):
        # print(l)
        if space == l:
            return dist
        dist+=1
        l-=1
    dist = 1
    while (space == r or (r<=6 and spaces[r] == 0)):
        if space == r:
            return dist
        dist+=1
        r+=1
    return None


my_rooms = ((2,4,4,4), (1,3,2,1), (2,2,1,4), (3,1,3,3))
my_p1_rooms = ((2,4,1,1), (1,1,2,2), (2,4,3,3), (3,3,4,4))
example =  ((2,4,4,1), (3,3,2,4), (2,2,1,3), (4,1,3,1))

#############
#...........#
###B#B#C#D###
  #D#C#B#A#
  #D#B#A#C#
  #D#C#A#A#
  #########

mw_rooms_p2 = ( (2,4,4,4), (2,3,2,3), (3,2,1,1), (4,1,3,1) )
mw_rooms_p1 = ( (2,4,1,1), (2,3,2,2), (3,1,3,3), (4,1,4,4) )


ex1_rooms = ((2,1,1,1), (3,4,2,2), (2,3,3,3), (4,1,4,4))


initial_rooms = ((1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4))
initial_spaces = (0,0,0,0,0,0,0)
initial_energy = 0


def solve():
    q = []
    seen = set()
    iteration = 0
    wins = []
    heappush(q, (initial_energy, my_rooms, initial_spaces, 0))
    # q.appendleft( (initial_energy, my_rooms, initial_spaces, 0))
    while len(q) > 0:
        energy, rooms, spaces, turn = heappop(q)
        # energy, rooms, spaces, turn = q.pop()
        if ( (rooms,spaces) in seen ):
            continue
        seen.add( (rooms,spaces) )

        # if iteration % 10000 == 0:
        #     print (energy, rooms, spaces, len(seen), len(q))

        if check_if_win(rooms):
            print (energy, rooms, spaces, len(seen), len(q))
            print("win", energy, iteration, turn)
            wins.append(energy)
            break

        moves = moves_from_spaces(rooms,spaces)
        if len(moves) == 0:
            moves = moves_from_rooms(rooms,spaces)

        for new_rooms, new_spaces, additional_energy in moves:
            heappush(q, ( energy + additional_energy, new_rooms, new_spaces, turn+1))
            # q.appendleft(( energy + additional_energy, new_rooms, new_spaces, turn+1))
            # print(new_rooms, new_spaces, additional_energy)
        iteration+=1

    print (wins)

solve()
# too low 32265
# too low 48224
