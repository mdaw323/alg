import fileinput

lines = [line.strip() for line in fileinput.input()]
surveys = [[]]
for line in lines:
    if line == '':
        surveys.append([])
    else:
        surveys[len(surveys)-1].append(line)

p1 = p2 = 0
for answers in surveys:
    s1 = set()
    s2 = set(answers[0])
    for a in answers:
        s1 |= set(a)
        s2 &= set(a)
    p1 += len(s1)
    p2 += len(s2)


print(p1, p2)
