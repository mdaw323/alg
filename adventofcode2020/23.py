class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)

    def wypisz(self, n):
        p = []
        node = self
        for _ in range(n):
            p.append(str(node.value+1))
            node = node.next
        print(''.join(p))


def solve(no_of_cups, moves):
    N = [None] * no_of_cups
    N[0] = Node(0)
    for i in range(1, no_of_cups):
        N[i] = Node(i)

    cur = None
    for i in range(len(cup) - 1):
        N[cup[i]].next = N[cup[i+1]]
        cur = N[cup[i+1]]

    for i in range(9, no_of_cups):
        cur.next = N[i]
        cur = N[i]

    cur.next = N[cup[0]]
    next_to_be = N[cup[0]]
    current = None

    for i in range(moves):
        current = next_to_be
        pickup = [current.next, current.next.next, current.next.next.next]
        pickup_val = [x.value for x in pickup]
        current.next = pickup[2].next
        destination_val = (current.value - 1) % no_of_cups

        while destination_val in pickup_val:
            destination_val = (destination_val - 1) % no_of_cups
        destination = N[destination_val]

        pickup[2].next = destination.next
        destination.next = pickup[0]
        next_to_be = current.next
    return N[0]


cup = [int(x) - 1 for x in '394618527']
p1 = solve(9, 100)
p1.next.wypisz(8)
p2 = solve(1_000_000, 10_000_000)
print((p2.next.value+1) * (p2.next.next.value + 1))
