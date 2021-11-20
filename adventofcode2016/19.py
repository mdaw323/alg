n = 3001330
# n = 190

class LinkedList:
    def __init__(self,x):
        self.x = x
        self.next = None

    def link(self,next):
        self.next = next

    def has_next(self):
        return self.next != None and self.next != self

    def get_next(self):
        return self.next


    def remove_next(self):
        self.next = self.next.next

elves = []

for i in range(n):
    elves.append(LinkedList(i))
for i in range(n):
    elves[i].link(elves[(i+1)%n])

e:LinkedList = elves[0]

while (e.has_next()):
    e.remove_next()
    e = e.get_next()
p1 = e.x+1

el = []

for i in range(n):
    el.append(i)


while len(el) >1:
    lel = len(el)
    for i in range(len(el)//2):
        step = (len(el) + i)//2
        to_remove = (i + step) % len(el)
        # print(f"remove {i} - {el[to_remove]}")
        el[to_remove] = -1

    step = lel//2
    nel = []
    for j in range(lel):
        k = (j+step) % lel
        if el[k] >=0:
            nel.append(el[k])
    el = nel
print (p1, el[0]+1)