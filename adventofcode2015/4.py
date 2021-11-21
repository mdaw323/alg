import hashlib

salt = 'iwrupvqb'

p1 = p2 = None
for i in range(100000000):
    x = salt + str(i)
    dig = hashlib.md5(x.encode()).hexdigest()
    if dig.startswith("00000") and p1 == None:
        p1 = i
    if dig.startswith("000000"):
        p2 = i
        break

print(p1, p2)
