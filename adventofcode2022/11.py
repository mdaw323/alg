import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement
import re

lines = [l.strip() for l in fileinput.input()]

def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
    cls.__str__ = __str__
    return cls


@auto_str
class Item:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level


@auto_str
class Monkey:
    def __init__(self,id) -> None:
        self.id = id
        self.items = set()
        self.op = '+'
        self.val = 'old'
        self.test = 1
        self.iftrue = id
        self.iffalse= id

    def do_operation(self,v):
        a = v
        if self.val == 'old':
            b = v
        else:
            b = int(self.val)
        if self.op == '+':
            return (a+b) % 9699690
        else:
            return (a*b) % 9699690



def parseint(s):
    return int(re.search(r'(\d+)', s).group(1))


monkeys = []

ic = 0
mid = 0
m = None
for line in lines:
    words = line.split()
    if not line:
        # print(m)
        monkeys.append(m)
        mid+=1
    elif words[0] == "Monkey":
        m = Monkey(parseint(words[1]))
    elif words[0] == "Starting":
        item_levels = [parseint(w) for w in words[2:]]
        for item_level in item_levels:
            ic +=1
            m.items.add(Item(ic,item_level))
    elif words[0] == 'Operation:':
        # print(words)
        m.op = words[4]
        m.val = words[5]
    elif words[0] == "Test:":
        m.test = int(words[3])
    elif words[1] == "true:":
        m.iftrue = int(words[5])
    elif words[1] == "false:":
        m.iffalse = int(words[5])
    else:
        assert False
    # print (lines)
monkeys.append(m)



# print (*monkeys)
cnt = [0] * len(monkeys)

for round in range(10000):
    print ("round", round+1)
    for m in monkeys:
        items = set(m.items)
        m.items = set()
        for item in items:
            cnt[m.id] += 1
            new_level = m.do_operation(item.level)
            item.level = new_level
            new_monkey = m.iftrue if item.level % m.test == 0 else m.iffalse
            # print (new_monkey)
            monkeys[new_monkey].items.add(item)
            # print(m.id, item, new_level)
    # for m in monkeys:
        # print(m.id, *list(sorted([x.level for x in m.items])))
    print (*cnt)

print (sorted(cnt)[-1] * sorted(cnt)[-2])

dd = 1
for m in monkeys:
    dd *= m.test

# print (dd)
