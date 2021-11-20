import utils
from itertools import permutations

lines = utils.readLines()


def swap_position(s, x, y):
    t = s[x]
    s[x] = s[y]
    s[y] = t
    return s


def swap_letter(s, a, b):
    x = y = None
    for i in range(len(s)):
        if s[i] == a:
            x = i
        elif s[i] == b:
            y = i
    assert (x != None and y != None)
    return swap_position(s, x, y)


def rotate(s, x):
    return s[x:] + s[:x]


def rotate_on_pos(s, a):
    for i in range(len(s)):
        if s[i] == a:
            x = i
            x = 1 + i + (1 if x >= 4 else 0)
            x = x % len(s)
            return rotate(s, -x)


def reverse(s, x, y):
    return s[0:x] + list(reversed(s[x:y+1])) + s[y+1:]


def move(s, x, y):
    t = s[0:x] + s[x+1:]
    return t[0:y] + s[x:x+1] + t[y:]


def transform(t):
    for line in lines:
        s = line.split()
        if s[0] == 'swap' and s[1] == 'position':
            t = swap_position(t, int(s[2]), int(s[5]))
        elif s[0] == 'swap' and s[1] == 'letter':
            t = swap_letter(t, s[2], s[5])
        elif s[0] == 'rotate' and s[1] == 'left':
            t = rotate(t, int(s[2]))
        elif s[0] == 'rotate' and s[1] == 'right':
            t = rotate(t, -int(s[2]))
        elif s[0] == 'rotate' and s[1] == 'based':
            t = rotate_on_pos(t, s[6])
        elif s[0] == 'reverse':
            t = reverse(t, int(s[2]), int(s[4]))
        elif s[0] == 'move':
            t = move(t, int(s[2]), int(s[5]))
        else:
            assert False, s
    return t


expected = [x for x in 'fbgdceah']
p1 = "".join(transform([x for x in 'abcdefgh']))

for pp in permutations([x for x in 'abcedfgh']):
    t = transform(list(pp))
    if expected == t:
        p2 = "".join(pp)
        break

print(p1, p2)
