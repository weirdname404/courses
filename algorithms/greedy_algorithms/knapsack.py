# python3
import heapq
import sys


# O(nlogn)
def sort_f_knapsack(capacity, items):
    order = [(v / w, w) for v, w in items]
    order.sort(reverse=True)
    max_value = 0

    for v_per_w, w in order:
        if capacity > w:
            capacity -= w
            max_value += w * v_per_w

        else:
            max_value += capacity * v_per_w
            break

    return max_value


# O(n)
def f_knapsack(capacity, items):
    order = [(-v / w, w) for v, w in items]
    heapq.heapify(order)
    acc = 0

    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        take_w = min(w, capacity)
        acc -= v_per_w * take_w
        capacity -= take_w

    return acc


def test():
    assert f_knapsack(0, [(60, 20)]) == 0.0
    assert f_knapsack(25, [(60, 20)]) == 60.0
    assert f_knapsack(25, [(60, 20), (0, 100)]) == 60.0
    assert f_knapsack(25, [(60, 20), (50, 50)]) == 65.0
    assert f_knapsack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0


def main():
    # N of items and the capacity W of a knapsack.
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, w = next(reader)
    items = list(reader)
    assert len(items) == n
    opt_value = f_knapsack(w, items)
    print("%.4f" % opt_value)


if __name__ == "__main__":
    main()
