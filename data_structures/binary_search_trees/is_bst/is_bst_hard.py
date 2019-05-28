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

Recursive in-order DFS traversal was used.
"""

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def is_key_gr_or_eq_root(key, root_key):
    return key >= root_key


def is_key_smaller_root(key, root_key):
    return key < root_key


def walk_decorator(tree, fail_condition):
    root_key = tree[0][0]
    min_key_stack = []

    def walk(i):
        stack = []

        while i != -1:
            stack.append(i)
            min_key = tree[i][0]
            i = tree[i][1]

        l_ch_key = float("-inf")

        if stack:
            min_key_stack.append(min_key)

        while stack:
            i = stack.pop()
            key = tree[i][0]
            if key <= l_ch_key or fail_condition(key, root_key):
                return False

            l_ch_key = key
            r_ch_i = tree[i][2]

            if r_ch_i != -1:
                r_ch_key = tree[r_ch_i][0]
                if key > r_ch_key or not walk(r_ch_i):
                    return False

                if min_key_stack.pop() < key:
                    return False

        return True

    return walk


def is_bst(tree):
    is_left_bst = walk_decorator(tree, is_key_gr_or_eq_root)(tree[0][1])
    if not is_left_bst:
        return False

    is_right_bst = walk_decorator(tree, is_key_smaller_root)(tree[0][2])

    return is_left_bst and is_right_bst


def main():
    n = int(next(sys.stdin))
    tree = [tuple(map(int, line.split())) for line in sys.stdin]

    if n == 0 or is_bst(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
