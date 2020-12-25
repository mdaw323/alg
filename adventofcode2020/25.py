
mod = 20201227

# card = 5764801
# door = 17807724

card = 1327981
door = 2822615


def find_loop(value):
    v = 1
    for loop in range(1_000_000_000):
        v = (v * 7) % mod
        if v == value:
            return loop+1
    assert False, "Too hard"


card_loop = find_loop(card)
door_loop = find_loop(door)

c = 1
for i in range(door_loop):
    c = (c * card) % mod


d = 1
for i in range(card_loop):
    d = (d * door) % mod


assert c == d
print(c)
