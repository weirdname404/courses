# python3
"""
You are given a rooted binary tree.
Build and output its in-order, pre-order and post-order traversals.
"""
import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order_traverse(self):
        result = []

        def walk(i):
            stack = []
            while i != -1:
                stack.append(i)
                i = self.left[i]

            while stack:
                i = stack.pop()
                result.append(self.key[i])

                if self.right[i] != -1:
                    walk(self.right[i])
            return result

        return walk(0)

    def pre_order_traverse(self):
        result = []

        def walk(i):
            stack = []
            while i != -1:
                result.append(self.key[i])
                stack.append(i)
                i = self.left[i]

            while stack:
                i = stack.pop()
                if self.right[i] != -1:
                    walk(self.right[i])
            return result

        return walk(0)

    def post_order_traverse(self):
        result = []

        def walk(i):
            stack = []
            while i != -1:
                stack.append(i)
                i = self.left[i]

            while stack:
                i = stack.pop()
                if self.right[i] != -1:
                    walk(self.right[i])

                result.append(self.key[i])
            return result

        return walk(0)


def main():
    tree = TreeOrders()
    print(*tree.in_order_traverse())
    print(*tree.pre_order_traverse())
    print(*tree.post_order_traverse())


threading.Thread(target=main).start()
