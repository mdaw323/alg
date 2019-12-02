s1 = s2 = 0
with open('a1.in') as f:
    for line in f.readlines():
        fuel = int(line.strip()) //3 - 2
        s1+=fuel
        while (fuel > 0):
            s2 += fuel
            fuel = fuel //3 -2            

print("part1",s1)
print("part2",s2)