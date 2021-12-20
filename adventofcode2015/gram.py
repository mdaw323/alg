#!/usr/bin/python3

import sys
from lark import Lark, tree

grammar = """

    Al     : Th F
           | Th Rn F Ar
           | "Al"
    Th     : "Th"
    F      : "F"
    Ar     : "Ar"
    Rn     : "Rn"

    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='Al', ambiguity='explicit')

sentence = 'Th Rn F Ar'

def make_png(filename):
    tree.pydot__tree_to_png( parser.parse(sentence), filename)

def make_dot(filename):
    tree.pydot__tree_to_dot( parser.parse(sentence), filename)

if __name__ == '__main__':
    print(parser.parse(sentence).pretty())
    # make_png('gram.pgn')
