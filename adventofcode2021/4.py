import fileinput
import sys
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_right
sys.setrecursionlimit(10000000)
dd = defaultdict(lambda: 0)
dx = [0, 0, -1, 1]  # NSWE
dy = [-1, 1, 0, 0]  # NSWE

p1 = p2 = 0

ll = [l.strip() for l in fileinput.input()] + ['']

numbers = []
board = []

mink = -1
maxk = 999999

p1 = p2 = None
for ii in range(len(ll)):
    l = ll[ii]
    if ii == 0:
        numbers = [int(x) for x in l.split(',')]
    elif l == '':
        if len(board) >0:
            winner = False
            for k, n in enumerate(numbers):
                for i in range(5):
                    for j in range(5):
                        if board[i][j] == n:
                            board[i][j] = -1

                for i in range(5):
                    row = True
                    col = True

                    for j in range(5):
                        if board[i][j] >=0:
                            row = False
                        if board[j][i] >=0:
                            col = False
                    if row or col:
                        winner = True
                c = 0
                for i in range(5):
                    for j in range(5):
                        if board[i][j] >= 0:
                            c+=board[i][j]

                if winner:
                    if mink <k:
                        mink = k
                        p2 = n*c
                    if maxk > k:
                        maxk = k
                        p1 = n*c
                    break

        board = []
    else:
        board.append([int(x) for x in l.split()])

print(p1,p2)
