# python3
"""
You are given a rooted binary tree.
Build and output its in-order, pre-order and post-order traversals.

This version turned out to work slower than tree_traversal2.py
"""
import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def walk(f):
    res = []

    def wrapper(*args):
        res.extend(i for i in f(*args))
        return res

    return wrapper


class TreeOrders:
    def __init__(self):
        next(sys.stdin)
        self.tree = [tuple(map(int, line.split())) for line in sys.stdin]

    @walk
    def in_order(self, i):
        stack = []
        while i != -1:
            stack.append(i)
            i = self.tree[i][1]

        while stack:
            i = stack.pop()
            yield self.tree[i][0]

            if self.tree[i][2] != -1:
                self.in_order(self.tree[i][2])

    @walk
    def pre_order(self, i):
        stack = []
        while i != -1:
            yield self.tree[i][0]
            stack.append(i)
            i = self.tree[i][1]

        while stack:
            i = stack.pop()
            if self.tree[i][2] != -1:
                self.pre_order(self.tree[i][2])

    @walk
    def post_order(self, i):
        stack = []
        while i != -1:
            stack.append(i)
            i = self.tree[i][1]

        while stack:
            i = stack.pop()
            if self.tree[i][2] != -1:
                self.post_order(self.tree[i][2])

            yield self.tree[i][0]


def main():
    tree = TreeOrders()
    print(*tree.in_order(0))
    print(*tree.pre_order(0))
    print(*tree.post_order(0))


threading.Thread(target=main).start()
