part1 = part2 = 0
for num in range(307237, 769058+1):
    D = [-1] + [int(i) for i in str(num)] + [10]        
    if any([D[j] > D[j+1] for j in range(len(D)-1)]):
        continue
    part1 += 1 if any([D[j] == D[j+1] for j in range(len(D)-1)]) else 0
    part2 += 1 if any([D[j] == D[j+1] and D[j-1] != D[j] and D[j] != D[j+2] for j in range(1,len(D)-1)]) else 0
print(part1, part2)