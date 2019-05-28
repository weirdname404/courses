# python3
from bst import BinarySearchTree, Node

"""
Implementation of AVL Tree that support operations:
- append/delete
- min/max
- next/prev
- print in order all elements
- print in reversed order all elements
- find
- range search

This implementation can append duplicates as new nodes. 
Keeping AVL property will break BST property eventually.
"""


class AVLNode(Node):
    height = 1


class AVLTree(BinarySearchTree):
    def append(self, value):
        new_node = AVLNode(value)  # new
        node = self.find_place_to_append(value)

        if node:
            new_node.parent = node
            if value < node.value:
                new_node.is_left = True
                node.left = new_node
            else:
                new_node.is_right = True
                node.right = new_node

            self.__rebalance(new_node.parent)

        else:
            self.root = new_node

    def delete(self, value):
        del_node = self.find(value)
        if not del_node:
            return

        swap_node = self.get_swap_node(del_node)
        self.swap_n_delete(del_node, swap_node)
        if swap_node:
            self.__rebalance(swap_node.parent)
        else:
            self.__rebalance(del_node.parent)

    @staticmethod
    def __get_children_heights(node):
        l_h, r_h = 0, 0
        if node.left:
            l_h = node.left.height

        if node.right:
            r_h = node.right.height

        return l_h, r_h

    def _adjust_height(self, node):
        l_h, r_h = self.__get_children_heights(node)
        node.height = max(l_h, r_h) + 1

    @staticmethod
    def __switch_side(node, left=False, right=False):
        if not node:
            return

        if left:
            node.is_right = False
            node.is_left = True

        elif right:
            node.is_right = True
            node.is_left = False

    # AVL tree property
    def __is_balanced(self, node):
        l_h, r_h = self.__get_children_heights(node)
        if l_h == 0 and r_h == 0 and node.height > 1:
            return False

        return abs(l_h - r_h) <= 1

    # BST property will be broken after several rotations in AVL tree with duplicates
    def __is_bst(self, node):
        l_v = float("-inf")
        r_v = float("inf")
        if node.left:
            l_v = node.left.value
        if node.right:
            r_v = node.right.value

        return l_v < node.value <= r_v

    def __rebalance(self, node):
        while node:
            left_h, right_h = self.__get_children_heights(node)

            if left_h > right_h + 1:
                self.__rebalance_right(node)

            elif left_h + 1 < right_h:
                self.__rebalance_left(node)

            else:
                new_h = max(left_h, right_h) + 1
                if node.height != new_h:
                    node.height = new_h

            node = node.parent

    def __rebalance_right(self, node):
        l_ch_h, r_ch_h = self.__get_children_heights(node.left)

        if r_ch_h > l_ch_h:
            self.__rotate_left(node.left)

        self.__rotate_right(node)

    def __rebalance_left(self, node):
        l_ch_h, r_ch_h = self.__get_children_heights(node.right)

        if l_ch_h > r_ch_h:
            self.__rotate_right(node.right)

        self.__rotate_left(node)

    def __rotate_left(self, node):
        """
            P                       P
            |                       |
            X                       Y
           / \     rotate right    / \
          Y   C    ----------->   A   X
         / \     <-----------        / \
        A   B     rotate left       B   C
        """
        p = node.parent
        y = node.right
        b = y.left
        y.left = node
        node.right = b
        self.copy_side(from_node=node, to_node=y)
        self.__switch_side(b, right=True)
        self.__switch_side(node, left=True)

        y.parent = p
        self.__adjust_pointers(node, y)
        node.parent = y
        if b:
            b.parent = node

        self._adjust_height(node)

    def __rotate_right(self, node):
        p = node.parent
        y = node.left
        b = y.right
        y.right = node
        node.left = b
        self.copy_side(from_node=node, to_node=y)
        self.__switch_side(b, left=True)
        self.__switch_side(node, right=True)

        y.parent = p
        self.__adjust_pointers(node, y)
        node.parent = y
        if b:
            b.parent = node

        self._adjust_height(node)

    def __adjust_pointers(self, node, y):
        if node is self.root:
            self.root = y
            y.is_right = False
            y.is_left = False

        elif y.is_right:
            y.parent.right = y
        elif y.is_left:
            y.parent.left = y

    def check_balance(self):
        node = self.get_min_node(self.root)
        while node:
            if not self.__is_balanced(node):
                print(f"Tree is IMBALANCED in node {node.value}, (h: {node.height})")
                return False
            # if not not self.__is_bst(node):
            #     print(f"BST is broken in node {node.value}, (h: {node.height})")
            #     return False
            node = self.next_node(node)

        return True
