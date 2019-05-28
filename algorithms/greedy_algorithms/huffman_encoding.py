import heapq
from collections import Counter, namedtuple

"""
This program implements Huffman encoding with the help of Python heap.
"""


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    code = {}
    h = []

    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _c1, left = heapq.heappop(h)
        freq2, _c2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")

    return code


def huffman_decode(encoded, code):
    key = ''
    decoded = ''
    decode_code = {key: ch for ch, key in code.items()}
    for s in encoded:
        key += s
        if key in decode_code:
            decoded += decode_code[key]
            key = ''

    return decoded


def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(s), len(encoded))
    for key in sorted(code):
        print(f'{code[key]}: {key}')
    print(encoded)


def test(n_iter):
    import random as r
    import string
    import sys

    for _ in range(n_iter):
        length = r.randint(0, 32)
        s = "".join(r.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        try:
            decoded = huffman_decode(encoded, code)
            assert s == decoded
        except AssertionError:
            sys.exit(f'{s}, {decoded}')
    print('ALL OK')


if __name__ == "__main__":
    # test(1000)
    main()
