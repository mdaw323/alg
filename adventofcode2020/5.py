import fileinput
lines = [s.strip() for s in fileinput.input()]
p1 = 0
seats = set()
for seat in lines:
    ba = le = 0
    fo = 128
    ri = 8
    for c in seat:
        if c == 'F':
            fo = (ba + fo) // 2
        elif c == 'B':
            ba = (ba + fo) // 2
        elif c == 'L':
            ri = (le + ri) // 2
        else:
            le = (le + ri) // 2
    seats.add(ba * 8 + le)
    p1 = max(ba * 8 + le, p1)


p2 = 0
for i in range(1, 999):
    if i not in seats and i-1 in seats and i+1 in seats:
        p2 = i
        break

print(p1, p2)
