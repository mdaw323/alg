import hashlib
import bisect

def find_next(ss, i):
    v = bisect.bisect_right(ss, i)
    if v < len(ss):
        return ss[v]
    else:
        return 999999999

salt = 'ihaygndm'
# salt = 'abc'
fives = []
trees = []
for c in range(10):
    trees.append((chr(ord('0') + c) * 3))
    fives.append((chr(ord('0') + c) * 5))
for c in range(6):
    trees.append((chr(ord('a') + c) * 3))
    fives.append((chr(ord('a') + c) * 5))

print (trees, fives)

m = []
for f in fives:
    m.append([])

for i in range(22000):
    s = hashlib.md5(f"{salt}{i}".encode()).hexdigest()
    # print(s)
    for _ in range(2016):
        s = hashlib.md5(s.encode()).hexdigest()
    # print(s)
    for j,f in enumerate(fives):
        if f in s:
            m[j].append(i)
    if i % 1000 == 0:
        print (i)
k = 0
for i in range (22000):
    s = hashlib.md5(f"{salt}{i}".encode()).hexdigest()
    for _ in range(2016):
        s = hashlib.md5(s.encode()).hexdigest()
    candidates = []
    for j,f in enumerate(trees):
        pos = s.find(f)
        if pos > 0:
            candidates.append((pos, j))
    for _, j in candidates:
    # if len(candidates) > 0:
        # _, j = min(candidates)
        n = find_next(m[j],i)

        if i + 1000 >= n:
            print(k, s,trees[j], n,i,i + 1000 >= n)
            # print(k,i, n)
            k+=1
            break
    if k > 70:
        break
