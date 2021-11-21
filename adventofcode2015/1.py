import fileinput

lines = [l.strip() for l in fileinput.input()]

pos = 1
level = 0
part2 = None
for l in lines:
    for c in l:
        level += 1 if c == '(' else -1
        if level == -1 and part2 == None:
            part2 = pos
        pos += 1

print(level, part2)
