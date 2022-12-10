import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement



p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]

len_x = len(lines[0])
len_y = len(lines)

visible = set()

for x in range(len_x):
    cnt_x = -1
    cnt_y = -1
    for y in range(len_y):
        lx = int(lines[x][y])
        ly = int(lines[y][x])
        if lx > cnt_x:
            visible.add((x,y))
            cnt_x = lx
        if ly > cnt_y:
            visible.add((y,x))
            cnt_y = ly

for x in range(len_x-1,-1,-1):
    cnt_x = -1
    cnt_y = -1
    for y in range(len_y-1,-1,-1):
        lx = int(lines[x][y])
        ly = int(lines[y][x])
        if lx > cnt_x:
            visible.add((x,y))
            cnt_x = lx
        if ly > cnt_y:
            visible.add((y,x))
            cnt_y = ly


dx = [1,0,-1,0]
dy = [0,1,0,-1]

best = 0
for x in range(len_x):
    # if x != 3:
    #     continue
    for y in range(len_y):
        # if y != 2:
        #     continue
        score = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            k = 0
            cnt = -1
            is_blocked = False
            cnt = int(lines[x][y])
            while (len_x > nx >=0) and (len_y > ny >=0):
                k+=1
                if cnt <= int(lines[nx][ny]):
                    break

                nx = nx + dx[i]
                ny = ny + dy[i]

            # print(i,k,score)
            score = score * k
        print(x,y,lines[x][y],score)
        best = max(best, score)



print (len(visible), best)
