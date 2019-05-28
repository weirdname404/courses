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
    matrices = []
    truth_table = []
    for _ in range(k - 1):
        matrix = [[0] * (total_weight + 1) for _ in range(len(weights) + 1)]
        matrices.append(matrix)
        truth_table.append(False)

    for i in range(1, len(weights) + 1):
        for knapsack_w in range(1, total_weight + 1):
            options = []
            num = weights[i - 1]
            for matrix_i in range(k - 1):
                if truth_table[matrix_i]:
                    continue

                case_a = matrices[matrix_i][i - 1][knapsack_w]
                case_b = case_a

                if num <= knapsack_w:
                    case_b = matrices[matrix_i][i - 1][knapsack_w - num] + num

                # print(num, knapsack_w, case_a, case_b)

                options.append((case_a + case_b, (case_a, case_b), matrix_i))

            # print(options)

            if not options and all(truth_table):
                return True

            _, (case_a, case_b), index = max(options)
            optimal_num = max(case_a, case_b)

            if optimal_num <= knapsack_w:
                matrices[index][i][knapsack_w] = optimal_num

                for option in options:
                    _, (case_a, case_b), matrix_i = option
                    if matrix_i == index:
                        continue

                    matrices[matrix_i][i][knapsack_w] = case_a

                # print(matrices[0][i][knapsack_w], matrices[1][i][knapsack_w])

                if knapsack_w == total_weight and optimal_num == total_weight:
                    truth_table[index] = True

    # res = []

    for m in matrices:
        for row in m:
            print(row)

        print("\n")

    return True if all(truth_table) else False


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
