import heapq
from collections import namedtuple
from node import Node as CommonNode


class Leaf(namedtuple("Leaf", ["code", "char"])):
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

    def find(self, code):
        return self.char if self.code == code else None


class Node(CommonNode):
    def find(self, code):
        result = self.left.find(code)
        if not result:
            result = self.right.find(code)
        return result if result else None


def huffman_tree(codes):
    queue = [(priority, Leaf(code, char)) for priority, code, char in codes]
    heapq.heapify(queue)
    if len(queue) == 1:
        _, leaf, = heapq.heappop(queue)
        return leaf
    while len(queue) > 1:
        priority1, left, = heapq.heappop(queue)
        priority2, right, = heapq.heappop(queue)
        elem = (priority1 + priority2, Node(left, right))
        heapq.heappush(queue, elem)

    [(_char, root)] = queue
    return root


def decode(encoded_str, codes):
    tree = huffman_tree(codes)
    string = ""
    buffer = ""
    for symbol in encoded_str:
        buffer += symbol
        result = tree.find(buffer)
        if result:
            buffer = ""
            string += result

    return string


def main():
    number_of_chars, encoded_str_length = map(int, input().split())
    codes = []
    for i in range(number_of_chars):
        char, code = input().split(": ")
        codes.append((code, char))
    encoded_str = input()
    codes.sort(key=lambda elem: elem[0])
    codes = [(i,) + codes[len(codes) - i] for i in range(len(codes), 0, -1)]
    print(decode(encoded_str, codes))


# Examples
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111
if __name__ == "__main__":
    main()
