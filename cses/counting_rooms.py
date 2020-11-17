import sys
from collections import deque
 
def input():
    return sys.stdin.readline()
 
 
n, m = [int(x) for x in input().strip().split()]
 
lab = []
 
for i in range(n):
    lab.append([x == '.' for x in input().strip()])
 
 
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
 
 
def visit(x, y):
    lab[x][y] = False
    queue = deque([(x,y)])
    while queue :
        a,b = queue.popleft()        
        for xx, yy in moves:
            nx = a+xx
            ny = b+yy
            if (0 <= nx < n and 0 <= ny < m and lab[nx][ny]):
                # print ("append",nx,ny)
                lab[nx][ny] = False
                queue.append( (nx,ny) )    
 
res = 0
for i in range(n):
    for j in range(m):
        if lab[i][j]:
            # print (i,j)
            res += 1
            visit(i,j)
 
 
print(res)