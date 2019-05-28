# python3
import sys
import random


def binary_search(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        m = (left + right) // 2

        if a[m] == x:
            return m

        elif x > a[m]:
            left = m + 1

        else:
            right = m - 1

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def test():
    for _ in range(50):
        n = random.randint(1, 10 ** 4)
        arr = sorted([random.randint(0, 10 ** 9) for _ in range(n)])
        for _ in range(10):
            x = random.randint(0, 10 ** 9)
            assert linear_search(arr, x) == binary_search(arr, x)


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')


if __name__ == '__main__':
    test()
    main()
