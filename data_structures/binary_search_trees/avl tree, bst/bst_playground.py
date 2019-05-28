from avl_tree import AVLTree, BinarySearchTree
"""
This playground was developed for testing purposes.
"""

def test_avl():
    test(AVLTree())


def test_bst():
    test(BinarySearchTree())


def test(tree):
    for _ in range(int(input())):
        cmd, *args = input().split()
        values = map(int, args)
        if cmd == 'a':
            tree.append(*values)
        elif cmd == 'f':
            value = next(values)
            node = tree.find(value)
            if not node or node.value != value:
                print("NOT FOUND")
            else:
                print("FOUND")
        elif cmd == 'd':
            print_tree_layers(tree.root)
        elif cmd == "max":
            print(tree.get_max_node(tree.root).value)
        elif cmd == "min":
            print(tree.get_min_node(tree.root).value)
        elif cmd == "n":
            print(tree.next_value(*values))
        elif cmd == "t":
            print(tree.in_order_traversal())
        elif cmd == "rt":
            print(tree.reversed_in_order_traversal())
        elif cmd == "rs":
            print(tree.range_search(*values))
        elif cmd == "del":
            tree.delete(*values)
        elif cmd == "r":
            print(tree.root)
        elif cmd == "b":
            success = False
            try:
                success = tree.check_balance()
            except AttributeError as e:
                print(e)

            if success:
                print("ALL GOOD\n")
            else:
                print_tree_layers(tree.root)


def print_tree_layers(tree_root):
    layer = []
    if tree_root:
        layer = [tree_root]

    while layer:
        res = []
        new_layer = []
        for node in layer:
            if node.is_left:
                side = "LEFT"
            elif node.is_right:
                side = "RIGHT"
            else:
                side = "ROOT"

            try:
                node_h = node.height
            except AttributeError:
                node_h = None

            res.append(f"({side} V: {node.value}, P: {node.parent.value if node.parent else None} H: {node_h})")

            if node.left:
                new_layer.append(node.left)
            if node.right:
                new_layer.append(node.right)

        print(res)
        layer = new_layer


if __name__ == "__main__":
    import time

    t0 = time.perf_counter()
    test_avl()
    # test_bst()
    print(time.perf_counter() - t0)
