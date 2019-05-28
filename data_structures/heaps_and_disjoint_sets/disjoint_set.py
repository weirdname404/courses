# python3


class DisjointSetArray:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        return self.parent[i]

    def __getattr__(self, item):
        return None

    # O(n)
    def union(self, a, b):
        roots = {self.find(a), self.find(b)}
        if len(roots) == 1:
            return

        m = min(roots)
        for i in range(len(self.parent)):
            if self.parent[i] in roots:
                self.parent[i] = m

    def __repr__(self):
        return str([i + 1 for i in self.parent])


# optimized disjoint set based on a tree
class DisjointSet(DisjointSetArray):
    def __init__(self, n):
        super().__init__(n)
        self.rank = [0] * n

    # optimized with path compression
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # optimized with rank heuristic
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return

        if self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root

        else:
            self.parent[a_root] = b_root
            if self.rank[b_root] == self.rank[a_root]:
                self.rank[b_root] += 1


# not optimized disjoint set based on a tree
class NotOptDisjointSet(DisjointSet):
    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]

        return i


# optimized for 1-based indexes
def perform_tasks(n):
    import sys

    for i in range(1, n + 1):
        try:
            with open(f"disjoint_set_tasks/{i}") as f:
                init, *commands = f.readlines()
        except FileNotFoundError:
            sys.exit(f"Task{i} is not found")

        ds_type, n = init.split()
        n = int(n)
        if ds_type == "Array":
            ds = DisjointSetArray(n)

        elif ds_type == "NOTree":
            ds = NotOptDisjointSet(n)

        else:
            ds = DisjointSet(n)

        print(f"Task{i} uses {type(ds).__name__}({n})")

        for line in commands:
            if "Find" in line:
                arg = int(line.strip('printFind()\n'))
                print(f"FIND {arg} FOUND {ds.find(arg - 1) + 1}")

            elif "Union" in line:
                args = list(map(lambda x: int(x) - 1, line.strip('Union()\n').split(', ')))
                # print("Union", args)
                ds.union(*args)

        # print(f"\nDS {ds}\nRA {ds.rank}")
        print(f"Tree height is {naive_count_tree_height(ds.parent)}\n")


def naive_count_tree_height(parent):
    height = 0
    for i in range(len(parent)):
        h = 0
        while i != parent[i]:
            h += 1
            i = parent[i]

        height = max(height, h)

    return height


def main():
    perform_tasks(4)


if __name__ == "__main__":
    main()
