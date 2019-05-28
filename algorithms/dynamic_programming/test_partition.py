# python3

"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
https://leetcode.com/problems/partition-equal-subset-sum/
"""

"""
строим несколько матриц
рассматриваем все рюкзаки для всех чисел

для всех матриц рассматриваем 2 случая
текущее число было взято или нет
вычислем оптимальное значение для всех матриц

как только в одной матрице достигается желаемое значение, сразу выписываем используемые числа (таблица истинности)
"""


def can_be_partitioned(nums, k=3):
    nums_sum = sum(nums)
    knapsack_w, module = divmod(nums_sum, k)

    if len(nums) < k or module or max(nums) > knapsack_w:
        return False

    return fill_discrete_knapsack(knapsack_w, nums, k)


def fill_discrete_knapsack(total_weight, weights, k):
    matrix = [[[0] * (total_weight + 1) for _ in range(len(weights) + 1)] for _ in range(k - 1)]

    for m in range(k - 1):
        for item in range(1, len(weights) + 1):
            for knapsack_w in range(1, total_weight + 1):
                num = weights[item - 1]

                case_a1 = matrix[m][item - 1][knapsack_w]

                case_b = case_a

                if num <= knapsack_w:
                    case_b = matrix[i - 1][knapsack_w - num] + num

                optimal_num = max(case_a, case_b)

    return 1


def test():
    assert can_be_partitioned([6, 5, 2, 1, 1, 3]) == 1
    assert can_be_partitioned([3, 3, 3, 3]) == 0
    assert can_be_partitioned([40]) == 0
    assert can_be_partitioned([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) == 1
    assert can_be_partitioned([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6]) == 1
    assert can_be_partitioned([1, 1, 1]) == 1
    assert can_be_partitioned([0, 0, 0]) == 1
    assert can_be_partitioned([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]) == 1
    print("OK")


def main():
    print(can_be_partitioned(list(map(int, input().split()))))


if __name__ == "__main__":
    test()
    main()
