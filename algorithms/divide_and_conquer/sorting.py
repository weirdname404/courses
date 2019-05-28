# Uses python3
"""
Task: add 3 half partition in quicksort
"""
import sys
import random
import time


# 3 half
def partition3(a, l, r):
    p = a[l]
    # start, end of middle part
    m1, m2 = l, l

    for i in range(l + 1, r + 1):
        if a[i] <= p:
            m2 += 1
            # swap big known element with element
            a[i], a[m2] = a[m2], a[i]

            if a[m2] < p:
                m1 += 1
                a[m1], a[m2] = a[m2], a[m1]

    a[l], a[m1] = a[m1], a[l]
    return m1, m2


# 2 half
def partition2(a, l, r):
    # pivot value
    p = a[l]
    # last element of left part
    m = l
    for i in range(l + 1, r + 1):
        if a[i] <= p:
            m += 1
            a[i], a[m] = a[m], a[i]
    a[l], a[m] = a[m], a[l]
    return m


def rand_qs_2(a, l, r):
    if l >= r:
        return
    p = random.randint(l, r)
    a[l], a[p] = a[p], a[l]
    m = partition2(a, l, r)
    rand_qs_2(a, l, m - 1)
    rand_qs_2(a, m + 1, r)


def rand_qs_3(a, l, r):
    if l >= r:
        return
    p = random.randint(l, r)
    a[l], a[p] = a[p], a[l]
    m1, m2 = partition3(a, l, r)
    rand_qs_3(a, l, m1 - 1)
    rand_qs_3(a, m2 + 1, r)


def randomized_quicksort(a, l, r):
    while l < r:
        p = random.randint(l, r)
        a[l], a[p] = a[p], a[l]
        m1, m2 = partition3(a, l, r)

        if m1 - l < r - m2:
            randomized_quicksort(a, l, m1 - 1)
            l = m2 + 1
        else:
            randomized_quicksort(a, m2 + 1, r)
            r = m1 - 1


def test2(*funcs):
    for f in funcs:
        longest_time = 0
        for _ in range(5):
            test = [random.randint(0, 10 ** 6) for _ in range(10**5)]
            # insert repeated values
            for _ in range(random.randint(1000, 10000)):
                test.insert(random.randint(1, len(test)), random.choice(test))

            test_arr = test.copy()
            t0 = time.perf_counter()
            f(test_arr, 0, len(test) - 1)
            t1 = time.perf_counter()
            assert test_arr == sorted(test)
            longest_time = max(longest_time, t1 - t0)
        print("{} PASSED in {} secs".format(f.__name__, round(longest_time, 5)))


def test1(f):
    longest_time = 0
    for _ in range(50):
        test_arr = [random.randint(0, 10 ** 4) for _ in range(random.randint(1, 10 ** 3))]
        pivot = test_arr[0]
        # insert repeated values
        for _ in range(random.randint(1, 500)):
            test_arr.insert(random.randint(1, len(test_arr)), pivot)
        t0 = time.perf_counter()
        m1, m2 = f(test_arr, 0, len(test_arr) - 1)
        t1 = time.perf_counter()
        longest_time = max(longest_time, t1 - t0)
        sorted_arr = sorted(test_arr)
        r_s_t = list(reversed(sorted_arr))
        assert m1 == sorted_arr.index(pivot)
        assert m2 == len(test_arr) - 1 - r_s_t.index(pivot)

    print("{} PASSED in {} secs".format(f.__name__, round(longest_time, 5)))


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quicksort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


if __name__ == '__main__':
    test1(partition3)
    test2(rand_qs_2, rand_qs_3, randomized_quicksort)
    main()
