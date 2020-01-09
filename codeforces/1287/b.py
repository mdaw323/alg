import sys
def input():
    return sys.stdin.readline().strip()

n, k = [int(x) for x in input().split()]

V = [input() for x in range(n)]
M = set(V)
z = ord('S') + ord('E') + ord('T')
cc = 0
for i in range(n):
    for j in range(i+1, n):
        s = ''
        for l in range(k):
            if V[i][l] == V[j][l]:
                s += V[i][l]
            else:
                s += chr(z - ord(V[i][l]) - ord(V[j][l]))                

        if s in M:
            cc += 1

print(cc // 3)
