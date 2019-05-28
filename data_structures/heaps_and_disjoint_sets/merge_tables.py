# python3
"""
There are N tables with random number of rows.
The task is to process M merge tables queries.
It is required to output max number of rows among all tables after each query.
"""

import sys


class DisjointSetOfTables:
    def __init__(self, n_rows, rows):
        self.max_row_n = max(rows)
        self.rows = rows
        self.parent = list(range(n_rows))
        self.rank = [0] * n_rows

    def find(self, table):
        if table != self.parent[table]:
            self.parent[table] = self.find(self.parent[table])
        return self.parent[table]

    def merge(self, destination, source):
        destination_root = self.find(destination - 1)
        source_root = self.find(source - 1)
        if destination_root == source_root:
            return self.max_row_n

        acc_row_n = self.rows[source_root] + self.rows[destination_root]
        if self.rank[destination_root] < self.rank[source_root]:
            self.parent[destination_root] = source_root
            self.rows[source_root] += self.rows[destination_root]
        else:
            if self.rank[destination_root] == self.rank[source_root]:
                self.rank[destination_root] += 1

            self.parent[source_root] = destination_root
            self.rows[destination_root] += self.rows[source_root]

        self.max_row_n = max(self.max_row_n, acc_row_n)

        return self.max_row_n


def process_queries(queries, tables_disjoint_set):
    for i in range(1, len(queries), 2):
        destination, source = queries[i - 1], queries[i]
        yield tables_disjoint_set.merge(destination, source)


def test():
    import sys
    import time

    tables_disjoint_set = DisjointSetOfTables(6, [10, 0, 5, 0, 3, 3])
    queries = [6, 6, 6, 5, 5, 4, 4, 3]
    assert list(process_queries(queries, tables_disjoint_set)) == [10, 10, 10, 11]

    tables_disjoint_set = DisjointSetOfTables(5, [1, 1, 1, 1, 1])
    queries = [3, 5, 2, 4, 1, 4, 5, 4, 5, 3]
    assert list(process_queries(queries, tables_disjoint_set)) == [2, 2, 3, 5, 5]

    try:
        with open("merge_test/116") as f:
            n_rows, rows, queries = parse_date(f.read())

    except FileNotFoundError as e:
        sys.exit(e)

    t0 = time.perf_counter()
    list(process_queries(queries, DisjointSetOfTables(n_rows, rows)))
    t1 = time.perf_counter()

    print("OK\nlong test took %.5f secs" % (t1 - t0))


def parse_date(data):
    data = list(map(int, data.split()))
    n_rows = data[0]
    rows = data[2:n_rows + 2]
    queries = data[n_rows + 2:]

    return n_rows, rows, queries


def main():
    n_rows, rows, queries = parse_date(sys.stdin.read())
    tables_disjoint_set = DisjointSetOfTables(n_rows, rows)

    for i in process_queries(queries, tables_disjoint_set):
        print(i)


if __name__ == "__main__":
    # test()
    main()
