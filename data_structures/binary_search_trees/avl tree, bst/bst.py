# python3

"""
Implementation of Binary Search Tree that support operations:
- append/delete
- min/max
- next/prev
- print in order all elements
- print in reversed order all elements
- find
- range search
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.is_left = False
        self.is_right = False

    def __repr__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, value):
        root = self.root
        while root:
            if value == root.value:
                return root
            root = self.__binary_step(value, root)

        return None

    def find_place_to_append(self, value):
        root = self.root
        parent = root

        while root:
            parent = root
            root = self.__binary_step(value, root)

        return parent

    def append(self, value):
        new_node = Node(value)
        node = self.find_place_to_append(value)

        if node:
            new_node.parent = node
            if value < node.value:
                new_node.is_left = True
                node.left = new_node
            else:
                new_node.is_right = True
                node.right = new_node
        else:
            self.root = new_node

    @staticmethod
    def get_min_node(root):  # cannot handle None root
        while root.left:
            root = root.left

        return root

    @staticmethod
    def get_max_node(root):  # cannot handle None root
        while root.right:
            root = root.right

        return root

    @staticmethod
    def __binary_step(value, node):
        if value < node.value:
            node = node.left
        else:
            node = node.right

        return node

    @staticmethod
    def copy_side(from_node, to_node):
        to_node.is_left = from_node.is_left
        to_node.is_right = from_node.is_right

    def next_value(self, value):
        if self.root:
            return self.next_node(self.find(value)).value
        else:
            return None

    def next_node(self, node):
        if node.right:
            return self.get_min_node(node.right)

        while node.is_right:
            node = node.parent

        if node.is_left:
            return node.parent

        else:
            return None

    def prev_node(self, node):
        if node.left:
            return self.get_max_node(node.left)

        while node.is_left:
            node = node.parent

        if node.is_right:
            return node.parent

        else:
            return None

    def reversed_in_order_traversal(self):
        res = []
        if self.root:
            node = self.get_max_node(self.root)
            while node:
                res.append(node.value)
                node = self.prev_node(node)

        return res

    def in_order_traversal(self):
        res = []
        if self.root:
            node = self.get_min_node(self.root)
            while node:
                res.append(node.value)
                node = self.next_node(node)

        return res

    def get_swap_node(self, del_node):
        swap_node = None
        if del_node.left:
            swap_node = self.get_max_node(del_node.left)
        elif del_node.right:
            swap_node = del_node.right

        return swap_node

    # swap values in nodes and change its pointers
    def swap_n_delete(self, del_node, swap_node):
        if swap_node:
            # the node we want to delete has left child
            if del_node.left:
                """
                There are 2 cases:
                if del_node's left child doesn't have right child:
                    1) swap_node = del_node.left
                else: (del_node's left child has right child)
                    2) swap_node = max_node of del_node left subtree
                """

                # 1st case
                if swap_node.parent == del_node:
                    del_node.left = swap_node.left
                    if swap_node.left:
                        swap_node.left.parent = del_node
                # 2d case
                else:
                    swap_node.parent.right = swap_node.left
                    if swap_node.left:
                        self.copy_side(from_node=swap_node, to_node=swap_node.left)
                        swap_node.left.parent = swap_node.parent

            # the node we want to delete has ONLY right child
            elif del_node.right:
                del_node.left = swap_node.left
                del_node.right = swap_node.right
                if swap_node.left:
                    swap_node.left.parent = del_node

                if swap_node.right:
                    swap_node.right.parent = del_node

            # before node is deleted - swap values
            swap_node.value, del_node.value = del_node.value, swap_node.value

        # the node we want to delete doesn't have any children
        else:
            if del_node is not self.root:
                if del_node.is_left:
                    del_node.parent.left = None
                elif del_node.is_right:
                    del_node.parent.right = None
            else:
                self.root = None

    def delete(self, value):
        del_node = self.find(value)
        if not del_node:
            return

        self.swap_n_delete(del_node, self.get_swap_node(del_node))

    # return all values between x and y
    def range_search(self, x, y):
        res = []
        node = self.find(x)
        while node:
            if node.value > y:
                break

            if x <= node.value <= y:
                res.append(node.value)

            node = self.next_node(node)

        return res
