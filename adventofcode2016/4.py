import fileinput

lines = [x.strip() for x in fileinput.input()]
p1 = 0
p2 = 0
for line in lines:
    tokens = line.split(sep='-')
    rooms = tokens[:-1]
    t = tokens[-1].split('[')
    sector = int(t[0])
    result = ''.join([x for x in t[1]][:-1])
    s = ''.join(rooms)
    letters = set(''.join(rooms))
    r = []
    for l in letters:
        r.append([-s.count(l), l])
    r.sort()
    real_result = ''.join([y for (x, y) in r[:5]])
    if result == real_result:
        decrypted = []
        for room in rooms:
            new_room = ''.join(
                [chr((ord(c) - ord('a') + sector) % 26 + ord('a')) for c in room])
            decrypted.append(new_room)
        p1 += sector
        if ''.join(decrypted).find('pole') >= 0:
            p2 = sector
print(p1, p2)
