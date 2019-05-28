# python3
import random
import time
import functools


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"{func.__name__.split('_')[-1]!r} in {run_time:.5f} secs")
        return value

    return wrapper_timer


@timer
def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


@timer
def max_pairwise_product_sort(test_nums):
    nums = sorted(test_nums)
    return nums[-1] * nums[-2]


@timer
def max_pairwise_product_faster_1for(numbers):
    if numbers[0] > numbers[1]:
        max_value_i1, max_value_i2 = 0, 1
    else:
        max_value_i1, max_value_i2 = 1, 0

    for i in range(2, len(numbers)):
        if numbers[i] > numbers[max_value_i1] and numbers[i] > numbers[max_value_i2]:
            max_value_i2 = max_value_i1
            max_value_i1 = i

        elif numbers[max_value_i2] < numbers[i] <= numbers[max_value_i1]:
            max_value_i2 = i

    return numbers[max_value_i1] * numbers[max_value_i2]


@timer
def max_pairwise_product_faster_2for(numbers):
    max_value_i1 = 0
    n = len(numbers)

    for i in range(1, n):
        if numbers[i] > numbers[max_value_i1]:
            max_value_i1 = i

    max_value_i2 = 0 if max_value_i1 != 0 else 1

    for i in range(0, n):
        if numbers[i] > numbers[max_value_i2] and i != max_value_i1:
            max_value_i2 = i

    return numbers[max_value_i1] * numbers[max_value_i2]


@timer
def max_pairwise_product_max(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 * max2


@timer
def max_pairwise_product_mem(n):
    a, b = max(n[0], n[1]), min(n[0], n[1])

    for i in n[2:]:
        if i > a:
            b = a
            a = i

        elif i > b:
            b = i

    return a * b


def run_test_cases(max_value, max_n_values, max_n_tests):
    for _ in range(max_n_tests):
        test_nums = []

        for _ in range(max_n_values):
            test_nums.append(random.randrange(2, max_value))

        # naive_res = max_pairwise_product_naive(test_nums.copy())
        faster_res = max_pairwise_product_faster_1for(test_nums.copy())
        alternative_res = max_pairwise_product_faster_2for(test_nums.copy())
        sort_res = max_pairwise_product_sort(test_nums.copy())
        fastest_res = max_pairwise_product_max(test_nums.copy())
        mem_res = max_pairwise_product_mem(test_nums.copy())

        if fastest_res == faster_res == alternative_res == sort_res == mem_res:
            print("OK", max_n_values)
            max_n_values *= 5
        else:
            print(f'{test_nums} Wrong answer! {faster_res} {alternative_res} {fastest_res} {sort_res} {mem_res}')


def start_naive_from_input(input_numbers):
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_naive(input_numbers))


if __name__ == '__main__':
    run_test_cases(10000000, 2000, 3)
    # input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product_mem(input_numbers))
