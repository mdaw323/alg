import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement

lines = [l.strip() for l in fileinput.input()]

jet = lines[0]
# jet = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
shapes = [
    ([(0,0), (1,0), (2,0), (3,0)], 1),
    ([(0,1), (1,0), (1,1), (1,2), (2,1)], 3),
    ([(0,0), (1,0), (2,0), (2,1), (2,2)], 3),
    ([(0,0), (0,1), (0,2), (0,3)], 4),
    ([(0,0), (0,1), (1,0), (1,1)], 2)
]

level = 0
left = 0
right = 8
space = set()

mem = {}

def can_place(rock, xx, yy):
    for x,y in rock:
        nx, ny = xx+x, yy + y
        if ((nx,ny) in space) or (not 0<nx<8 ) or ( ny <=0 ):
            return False
    return True

def fill_space(rock, xx, yy):
    for (x,y) in rock:
        space.add( (xx+x, yy+y) )

j = 0
i = 0
# while i < 1000000000000:
while i <= 2020:
# for i in range(5000):
    rock, height = shapes[i % len(shapes)]
    x = 3
    y = level + 4
    falling = True
    while falling:
        xx = (x+1) if jet[j] == '>' else (x-1)
        if can_place(rock, xx, y):
            x = xx
        j = (j + 1) % len(jet)
        if can_place(rock, x, y-1):
            y = y-1
        else:
            fill_space(rock, x, y)
            level = max(level, y + height -1)
            falling = False

    z = ''.join(['#' if (k,level) in space  else '.' for k in range(1,8)])
    print (z)
    if z == '#######':
        key = (i % len(shapes), j)
        if ((i % len(shapes), j) in mem):
            pass
        else:
            mem[key] = (i,j,level)
    # if i == 3325:
    #     print(i, level)
        # print (i, i % len(shapes), j, level, 3987 + (i - 2550) // 1725 * 2728)
    i += 1


# 2550

# 2550 + (x * 1725) + y = 1000000000000
# (x * 1725) + y = 1000000000000 - 2550

# 579710143 * 2728 + 3987 + 1229

# for i in range (level,0,-1):
#     print(*['#' if (j,i) in space  else '.' for j in range(1,8)], sep='')

# 2550 0 4858 3987
# 4275 0 4858 6715
# 6000 0 4858 9443
# 7725 0 4858 12171
# 9450 0 4858 14899
# 11175 0 4858 17627
# 12900 0 4858 20355
# 14625 0 4858 23083
# 16350 0 4858 25811
# 18075 0 4858 28539
# 19800 0 4858 31267

print (level)
# print (579710143 * 2728 + 3987 + 1207)

# 1581449275298 too low
# 1581449275320 too high
# 1581449275309 too low
# 1581449275319 ok

# (1581449275320 +1581449275298) //2
