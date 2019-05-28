# python3
"""
You are given a binary tree with integers as its keys.
You need to test whether it is a correct binary search tree

For example binary tree shown below is considered as INCORRECT
    2
   / \
  2   2

but binary tree
    2
   / \
  1   2
is considered as CORRECT

Non-recursive BFS traversal was used.
"""

import sys
from collections import deque


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.max_value = None
        self.min_value = None


def is_bst(tree):
    root = Node(*tree[0])
    layer = deque([root])

    while layer:
        node = layer.popleft()

        if node.max_value and node.value > node.max_value:
            return False
        if node.min_value and node.value < node.min_value:
            return False

        if node.left != -1:
            left_ch = Node(*tree[node.left])
            left_ch.max_value = node.value
            if node.min_value:
                left_ch.min_value = node.min_value

            layer.append(left_ch)

        if node.right != -1:
            right_ch = Node(*tree[node.right])
            if node.max_value:
                right_ch.max_value = node.max_value

            right_ch.min_value = node.value
            layer.append(right_ch)

    return True


def main():
    n = int(next(sys.stdin))
    tree = [tuple(map(int, line.split())) for line in sys.stdin]

    if n <= 1 or is_bst(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == "__main__":
    main()
