# python3
"""
TASK: compute and output height of the tree.

The first line contains the number of nodes N.
The second line contains N integer numbers from −1 to N−1 parents of nodes.

Output the height of the tree.
"""

import time
from collections import deque


def timed(f):
    def wrapper(args):
        t0 = time.perf_counter()
        res = f(args)
        t1 = time.perf_counter()
        print("%s performed in %.5f secs" % (f.__name__, t1 - t0))
        return res

    return wrapper


class Node:
    def __init__(self, parent_index):
        self.parent_index = parent_index
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


@timed
def get_tree_height(parents):
    nodes = [Node(parent_index) for parent_index in parents]
    root = None

    for child_index in range(len(nodes)):
        parent_index = nodes[child_index].parent_index

        if parent_index == -1:
            root = nodes[child_index]
        else:
            nodes[parent_index].add_child(nodes[child_index])

    return bfs_tree(root)


def bfs_tree(root):
    if not root.children:
        return 1

    h = 2
    children = deque(root.children)
    next_lvl_in = len(children)
    tmp = 0

    while children:
        if next_lvl_in == 0:
            h += 1
            next_lvl_in = tmp
            tmp = 0

        new_children = children.popleft().children
        tmp += len(new_children)
        next_lvl_in -= 1
        children.extend(new_children)

    return h


# Trees are too big to walk them recursively
def dfs_tree(root):
    if root.children:
        children_depth = [1 + dfs_tree(child) for child in root.children]
        return max(children_depth)
    return 1


# @timed # time tests showed that this func is the fastest
def compute_height(parents):
    max_height = 0
    memo = {}
    height_stack = []
    node_queue = []

    for node in range(len(parents)):
        height = 0

        if parents[node] in memo:
            memo[node] = memo[parents[node]] + 1
            max_height = max(max_height, memo[node])
            continue

        while node not in memo:
            height += 1
            node_queue.append(node)
            height_stack.append(height)
            node = parents[node]

            if node == -1:
                break

        known_node_height = memo[node] if memo else 0

        max_height = max(max_height, height + known_node_height)

        if node_queue:

            for node in node_queue:
                memo[node] = height_stack.pop() + known_node_height

            del node_queue[:]

    return max_height


@timed
def naive_get_tree_h(nodes):
    # this func turned out to be very slow
    # because we have to recalculate lots of nodes
    memo = {}
    max_h = 1
    for i in range(len(nodes)):
        h = 1
        p = nodes[i]
        while p != -1:
            if memo.get(p, None):
                h += memo[p]
                memo[i] = h
                break

            p = nodes[p]
            h += 1

        max_h = max(max_h, h)

    return max_h


def test(*funcs):
    import sys
    import os

    try:
        f = funcs[0]

        assert f([4, -1, 4, 1, 1]) == 3
        assert f([-1, 0, 4, 0, 3]) == 4

    except AssertionError:
        sys.exit("Short tests has failed")

    try:
        test_files = [f for f in os.scandir("tests")]

    except FileNotFoundError as e:
        sys.exit(e)

    for file in test_files:
        with open(file) as f:
            _n = f.readline()
            nodes = list(map(int, f.readline().split()))

        if not nodes:
            sys.exit("Something wrong with tests")

        try:
            print("\nTest %s" % file.name)
            results = [f(nodes) for f in funcs]
            assert results.count(results[0]) == len(results)

        except AssertionError:
            sys.exit("TEST %s failed" % file.name)

    print("OK")


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(parents))


if __name__ == "__main__":
    # test(compute_height, get_tree_height)
    main()
