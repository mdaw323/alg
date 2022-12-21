import fileinput
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, combinations_with_replacement

numbers = [811589153 * int(l.strip()) for l in fileinput.input()]

print(numbers)

N = len(numbers)

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)


nodes = [Node(i) for i in numbers]

zero = None
for i in range(len(nodes)):
    nodes[i].next = nodes[(i+1) % N]
    nodes[(i+1) % N].prev = nodes[i]
    if nodes[i].value == 0:
        zero = nodes[i]


def get_ordered_from_zero():
    nt = []
    node = zero
    nt.append(node.value)
    node = node.next
    # print (zero.next)
    while (node != zero):
        nt.append(node.value)
        node = node.next
    return nt

def get_desc_from_zero():
    nt = []
    node = zero
    nt.append(node.value)
    node = node.prev
    # print (zero.next)
    while (node != zero):
        nt.append(node.value)
        node = node.prev
    return nt


for _ in range(10):
    for i in range(len(nodes)):
        node = nodes[i]
        v = node.value
        # print (v, v % N if v >=0 else (v-1) % N)
        # r = v % (N-1) if v >=0 else (v) % (N-1)
        if v >= 0:
            for _ in range(abs(v) % (N-1)):
                prev = node.prev
                next = node.next
                nextnext = node.next.next
                node.prev = next
                node.next = nextnext
                prev.next = next
                next.prev = prev
                next.next = node
                nextnext.prev = node
        else:
            for _ in range(abs(v) % (N-1)):
                prev = node.prev
                next = node.next
                prevprev = node.prev.prev
                node.prev = prevprev
                node.next = prev
                next.prev = prev
                prev.next = next
                prev.prev = node
                prevprev.next = node
    # print(v, get_ordered_from_zero())

t = get_ordered_from_zero()

# print (get_desc_from_zero())

# print(t[1000 % N] , t[2000 % N], t[3000 % N] )

print(t[1000 % N] + t[2000 % N]+ t[3000 % N] )
# print(t[0]t[1], t[2], t[3])
