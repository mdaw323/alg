import fileinput

lines = [l.strip() for l in fileinput.input()]
p1 = p2 = 0
for l in lines:
    l, w, h = sorted(map(int, l.split('x')))
    p1 += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    p2 += l*w*h + 2*l + 2*w

print(p1, p2)
