from collections import namedtuple
from node import Node


class Leaf(namedtuple("Leaf", ["char"])):
    def __lt__(self, other):
        if isinstance(other, str):
            return self.char < other
        if isinstance(other, Node):
            return False
        return self.char < other.char

    def __eq__(self, other):
        if other is None or not isinstance(other, Leaf):
            return False
        if isinstance(other, Leaf):
            return other.char == self.char
        if isinstance(other, str):
            return self.char == other
        return self.char == other.char

    def walk(self, codes, acc):
        codes[self.char] = acc
