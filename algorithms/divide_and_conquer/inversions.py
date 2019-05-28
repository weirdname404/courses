# python3
"""
The goal in this problem is to count the number of inversions of a given sequence.
"""
import sys
import time


def merge(a, b, inversions):
    res = []
    i, j = 0, 0
    l_a, l_b = len(a), len(b)

    while i < l_a and j < l_b:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
            # value b[j] should swap with (len(a) - i) values to reach its position
            inversions += l_a - i

    res.extend(a[i:])
    res.extend(b[j:])

    return res, inversions


def count_inversions(arr):
    if len(arr) < 2:
        return arr, 0

    m = len(arr) // 2
    l, left_inv = count_inversions(arr[:m])
    r, right_inv = count_inversions(arr[m:])

    return merge(l, r, left_inv + right_inv)


def select_sort_inv(arr, inv):
    if len(arr) < 2:
        return arr, inv

    min_v = min(arr)
    min_v_i = arr.index(min_v)

    if arr[0] > min_v:
        arr[0], arr[min_v_i] = arr[min_v_i], arr[0]
        inv += 1

    sorted_arr, inv = select_sort_inv(arr[1:], inv)

    return [min_v] + sorted_arr, inv


def main():
    input = sys.stdin.read()
    n, *arr = map(int, input.split())
    _arr, n = count_inversions(arr)
    print(n)


def long_test():
    d = int(input())

    for _ in range(d):
        _n = int(input())
        arr = list(map(int, input().split()))
        t0 = time.perf_counter()
        _arr, _result = count_inversions(arr)
        t1 = time.perf_counter()

        print("%.5f secs" % (t1 - t0))


def test():
    test_cases = (
        ([2, 3, 9, 2, 9], 2),
        ([1, 2, 3, 4], 0),
        ([9, 8, 7, 3, 2, 1], 15),
    )

    for arr, answ in test_cases:
        _arr, inv = count_inversions(arr)
        assert inv == answ


if __name__ == "__main__":
    test()
    long_test()
    main()
