import re
import sys
import typing
from collections import defaultdict, deque, namedtuple

Point = namedtuple('Point', ['x', 'y'])


sys.setrecursionlimit(100000)


def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(a_string: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", a_string))


def floats(a_string: str) -> typing.List[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", a_string))


def words(a_string: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", a_string)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


def insert_after(prev_node: Node, d):
    el = Node(d)
    el.prev = prev_node
    el.next = prev_node.next
    if prev_node.next != None:
        prev_node.next.prev = el
    prev_node.next = el
    return el


def join_nodes(p: Node, n: Node):
    if p!=None:
        p.next = n
    if n != None:
        n.prev = p


def to_array(p: Node):
    s = [p.data]
    e = p.next
    while e != None and e != p:
        s += [e.data]
        e = e.next
    return s

# opcodes


# def addr(D, p):
#     D[D[p+3]] = D[D[p+1]] + D[D[p+2]]
#     return D


# def addi(D, p):
#     D[D[p+3]] = D[D[p+1]] + D[p+2]
#     return D


# def mulr(D, p):
#     D[D[p+3]] = D[D[p+1]] * D[D[p+2]]
#     return D


def muli(D, p):
    D[D[p+3]] = D[D[p+1]] * D[p+2]
    return D


def banr(D, p):
    D[D[p+3]] = D[D[p+1]] & D[D[p+2]]
    return D


def bani(D, p):
    D[D[p+3]] = D[D[p+1]] & D[p+2]
    return D


def borr(D, p):
    D[D[p+3]] = D[D[p+1]] | D[D[p+2]]
    return D


def bori(D, p):
    D[D[p+3]] = D[D[p+1]] | D[p+2]
    return D


def setr(D, p):
    D[D[p+3]] = D[D[p+1]]
    return D


def seti(D, p):
    D[D[p+3]] = D[p+1]
    return D


def gtir(D, p):
    D[D[p+3]] = 1 if D[p+1] > D[D[p+2]] else 0
    return D


def gtri(D, p):
    D[D[p+3]] = 1 if D[D[p+1]] > D[p+2] else 0
    return D


def gtrr(D, p):
    D[D[p+3]] = 1 if D[D[p+1]] > D[D[p+2]] else 0
    return D


def eqir(D, p):
    D[D[p+3]] = 1 if D[p+1] == D[D[p+2]] else 0
    return D


def eqri(D, p):
    D[D[p+3]] = 1 if D[D[p+1]] == D[p+2] else 0
    return D


def eqrr(D, p):
    D[D[p+3]] = 1 if D[D[p+1]] == D[D[p+2]] else 0
    return D



