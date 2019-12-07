from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def __lt__(self, other):
        if isinstance(other, Node):
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.left == other.left and self.right == other.right
        return False

    def walk(self, codes, acc):
        self.left.walk(codes, acc + "0")
        self.right.walk(codes, acc + "1")

