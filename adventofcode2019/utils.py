import re
import sys
import typing


sys.setrecursionlimit(100000)


def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(a_string: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", a_string))


def floats(a_string: str) -> typing.List[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", a_string))


def words(a_string: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", a_string)




# opcodes


def addr(D, p):
    D[D[p+3]] = D[D[p+1]] + D[D[p+2]]
    return D


def addi(D, p):
    D[D[p+3]] = D[D[p+1]] + D[p+2]
    return D


def mulr(D, p):
    D[D[p+3]] = D[D[p+1]] * D[D[p+2]]
    return D


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
 
opcodes = {1: addr, 2: mulr}