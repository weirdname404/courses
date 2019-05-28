# python3
# Compose the largest number out of a set of integers.

import functools
import random as r


def strange_less(a, b):
    v1 = a + b
    v2 = b + a

    if v1 > v2:
        return -1

    if v1 == v2:
        return 0

    return 1


def largest_number(nums):
    nums.sort(key=functools.cmp_to_key(strange_less))

    return ''.join(nums)


def is_greater(a, b):
    v1 = a + b
    v2 = b + a

    return v1 > v2


def naive_largest_number(nums):
    largest_number = ''

    while len(nums) != 0:
        max_num_i = 0

        for i in range(1, len(nums)):
            if is_greater(nums[i], nums[max_num_i]):
                max_num_i = i

        largest_number += nums[max_num_i]
        del nums[max_num_i]

    return largest_number


def generate_test_sample():
    n = r.randrange(1, 10)
    return list(map(str, [r.randrange(1, 1001) for _ in range(n)]))


def test():
    while True:
        nums = generate_test_sample()
        res1 = largest_number(nums.copy())
        res2 = naive_largest_number(nums.copy())
        print(nums, '\n')
        print(f"{res1}\n{res2}\n")
        assert res1 == res2


if __name__ == '__main__':
    n = input()
    nums = input().split()
    print(largest_number(nums))
    # test()
