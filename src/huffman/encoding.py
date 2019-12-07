from collections import Counter
import heapq
from leaf import Leaf
from node import Node


def huffman_tree(n):
    queue = [(freq, Leaf(ch)) for ch, freq in Counter(n).items()]
    heapq.heapify(queue)
    if len(queue) == 1:
        _, leaf, = heapq.heappop(queue)
        codes = {leaf.char: "0"}
        return codes
    while len(queue) > 1:
        freq1, left, = heapq.heappop(queue)
        freq2, right, = heapq.heappop(queue)
        elem = (freq1 + freq2, Node(left, right))
        heapq.heappush(queue, elem)

    [(_freq, root)] = queue
    codes = {}
    root.walk(codes, "")
    return codes


def encode(n):
    codes = huffman_tree(n)
    encoded_str = "".join([codes[i] for i in n])
    return codes, encoded_str


def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(1, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        _, encoded = encode(s)
        print(encoded)


def main():
    n = input()
    codes, encoded_str = encode(n)

    print("{} {}".format(len(codes.keys()), len(encoded_str)))
    for i in codes:
        print("{}: {}".format(i, codes[i]))
    print(encoded_str)
    # test()


# Examples
# abacabad
if __name__ == "__main__":
    main()
