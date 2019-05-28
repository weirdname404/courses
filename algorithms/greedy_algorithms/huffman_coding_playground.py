# python3
"""
This program implements Huffman encoding with the help of naive priority
queue (which uses simple array instead of heap).

1) We count frequency of each symbol O(n)
2) Put (value, frequency) info about every symbol in priority queue O(n)
3) Build binary tree based on symbol frequency with the help of prior queue O(n**2)
4) We walk our binary tree using recursive dfs to create a dict with huffman codes
5) Using huffman_codes dictionary translate initial word
6) Output:
print N of unique symbols in the word AND the length of encoded word
print every symbol and its code from huffman_codes dict
print encoded word
"""

"""
v - value
f - frequency
c - child
l - left
r - right
p - parent
q - queue
e, el = element
d - dict
h_d - huffman_dict
w - word
"""


class Node:
    l = None
    r = None
    p = None
    lvl = 0
    code = 0

    def __init__(self, v, f):
        self.v = v
        self.f = f

    def set_child(self, *children):
        # self.lvl += max([c.lvl for c in children]) + 1

        for c in children:
            c.p = self

            if self.r is not None:
                self.l = c
            else:
                self.r = c
                c.code += 1


# naive
class PriorQueue:
    def __init__(self, els):
        self.q = els

    def __str__(self):
        return "node"

    def insert(self, e):
        self.q.append(e)

    def pop_min(self):
        min_f = float('inf')
        _i = 0

        for i in range(len(self.q)):
            f = self.q[i].f
            if min_f > f:
                min_f = f
                _i = i

        return self.q.pop(_i)

    def get_q(self):
        return [(el.v, el.f) for el in self.q]

    def get_first_e(self):
        return self.q[0]

    def last_e(self):
        return len(self.q) == 1


def count_priority(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = s.count(i)
    return d


def create_p_q(d):
    els = [Node(i, d[i]) for i in d]
    return PriorQueue(els)


def create_huffman_tree(p_q):
    while p_q.last_e() != True:
        min_e1 = p_q.pop_min()
        min_e2 = p_q.pop_min()
        parent = Node('*', min_e1.f + min_e2.f)
        parent.set_child(min_e1, min_e2)
        p_q.insert(parent)

    return p_q.get_first_e()


def get_huffman_code(d, root):
    if len(d.keys()) == 1:
        d[root.v] = str(root.code)
        return d
    else:
        h_d, *args = dfs(d, root.l, [])
        h_d, *args = dfs(h_d, root.r, [])

    return h_d


# recursive
def dfs(d, node, code_acc):
    code_acc.append(str(node.code))

    if node.v != '*':
        d[node.v] = ''.join(code_acc)

    else:
        d, node, code_acc = dfs(d, node.l, code_acc)
        d, node, code_acc = dfs(d, node.r, code_acc)

    code_acc.pop()
    return d, node.p, code_acc


def encode(word, h_d):
    o = ''
    for symbol in word:
        o += h_d[symbol]

    return o


def output(w, h_d):
    code = encode(w, h_d)
    keys = sorted(h_d.keys())
    print(f'{len(keys)} {len(code)}')

    for k in keys:
        print(f'{k}: {h_d[k]}')

    print(code)


# experimental
def draw(nodes, _n):
    space = ' '
    values = ''
    children = []
    lines = ''
    empty_space = ' '
    no_child = None
    l_l = '/ '
    r_l = '\\  '

    for node in nodes:
        if node:
            values += f'{node.v}:{node.f}'

            if node.l:
                lines += l_l
                children.append(node.l)
            else:
                lines += empty_space
                children.append(no_child)

            if node.r:
                lines += r_l
                children.append(node.r)
            else:
                lines += empty_space
                children.append(no_child)

        else:
            values += empty_space

        values += space

    space = _n * space

    print(f'{space}{values}')
    print(f'{space}{lines}')

    if set(children) == {None}:
        return

    _n = _n - 3 if _n - 3 >= 0 else 0
    draw(children, _n)


def main():
    w = input()
    d = count_priority(w)
    # print(d)
    # print(sum(d.values()))
    p_q = create_p_q(d)
    tree = create_huffman_tree(p_q)
    # print(tree.f)
    # print(tree.lvl)
    draw([tree], 25)
    huff_d = get_huffman_code(d.copy(), tree)
    output(w, huff_d)


if __name__ == "__main__":
    main()
