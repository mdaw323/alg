import fileinput
from collections import deque, defaultdict
from itertools import permutations, combinations, combinations_with_replacement



p1 = p2 = 0

lines = [l.strip() for l in fileinput.input()]


class Node:
    def __init__(self, name, parent) -> None:
        self.parent = parent
        self.directories = {}
        self.name = name
        self.size = 0

# cmd = None

root = Node("/", None)
current_node = None

p1 = 0

for line in lines:
    cmd = line.split()
    part_size = 0

    if line.startswith("$ ls"):
        pass
    elif line.startswith("$ cd"):
        dir_name = cmd[2]
        if dir_name == "/":
            current_node = root
        elif dir_name == "..":
            current_node = current_node.parent
        else:
            current_node = current_node.directories[dir_name]
    elif line.startswith("dir"):
        dir_name = cmd[1]
        current_node.directories[dir_name] = Node(dir_name, current_node)
    else:
        size = int(cmd[0])
        cur = current_node
        while cur != None:
            cur.size+=size
            cur = cur.parent

def seek(node:Node):
    result = 0
    # print("node",node.name)
    if node.size <=100000:
        result += node.size
        # print(f"{node.name} {node.size}")
    for name, directory in node.directories.items():
        result += seek(directory)
    return result

def seek2(node:Node):
    result = 9999999999999
    # print(f"{node.name} {node.size}")
    if node.size >= 2677139:
        result = min(node.size, result)
        print(f"{node.name} {node.size}")
    for name, directory in node.directories.items():
        result = min(seek2(directory), result)
    return result



print(seek(root), seek2(root))

print(30000000 - (70000000 - root.size))

    # print (cmd)
