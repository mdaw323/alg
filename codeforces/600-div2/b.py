n = int(input())
A = [int(x) for x in input().split()]
inside = set()
same_day = set()
d = 0
r = []
for x in A:
    d += 1
    if x > 0:
        if (x in inside or x in same_day):            
            break
        else:
            inside.add(x)
            same_day.add(x)
    else:
        if abs(x) not in inside:
            inside.add(0)
            break
        else:
            inside.remove(abs(x))
            if len(inside) == 0:
                r.append(d)
                same_day.clear()
                d = 0
if len(inside) > 0:
    print("-1")
else:
    print(len(r))
    print(' '.join([str(x) for x in r]))
