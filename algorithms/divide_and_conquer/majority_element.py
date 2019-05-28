# python3
"""
The goal in this code problem is to check whether an input sequence contains a majority element.
"""
import sys
from collections import Counter


# O(nlogn)
def get_majority_element(a, left, right):
    return
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    # return -1


# O(n)
def has_majority_element(a):
    items = Counter(a).items()
    for ch, freq in items:
        if freq > len(a) // 2:
            return 1
    return 0


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(has_majority_element(a))


def test():
    test_cases = [([2, 3, 9, 2, 2], 1), ([1, 2, 3, 4], 0), ([1, 2, 3, 1], 0)]
    for arr, answer in test_cases:
        assert has_majority_element(arr) == answer


if __name__ == "__main__":
    test()
    main()
