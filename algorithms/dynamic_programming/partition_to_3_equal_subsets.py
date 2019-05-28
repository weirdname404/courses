# python3
"""
Check whether it is possible to partition natural integers into
three subsets with equal sums
EX: [5, 2, 3, 1, 6, 1] -> [5, 1], [6], [2, 3, 1]
"""


def backtrack(matrix, nums):
    used_items = []
    unused_items = []
    knapsack_w = matrix[-1][-1]
    i = len(matrix) - 1

    while knapsack_w > 0:
        if matrix[i][knapsack_w] != matrix[i - 1][knapsack_w]:
            used_items.append(i - 1)
            knapsack_w -= nums[i - 1]

        else:
            unused_items.append(nums[i - 1])

        i -= 1

    return used_items, unused_items + nums[len(matrix):]


def fill_discrete_knapsack(total_weight, weights):
    matrix = [[0] * (total_weight + 1) for _ in range(len(weights) + 1)]

    for i in range(1, len(weights) + 1):
        for knapsack_w in range(1, total_weight + 1):
            num = weights[i - 1]

            case_a = matrix[i - 1][knapsack_w]

            if num <= knapsack_w:
                case_b = matrix[i - 1][knapsack_w - num] + num
            else:
                case_b = case_a

            optimal_num = max(case_a, case_b)

            if optimal_num <= knapsack_w:
                matrix[i][knapsack_w] = optimal_num

                if knapsack_w == total_weight and optimal_num == total_weight:
                    return matrix[:i + 1]

    return matrix if matrix[-1][-1] == total_weight else None


def can_be_partitioned(nums):
    nums_sum = sum(nums)
    groups = []

    if len(nums) < 3 or nums_sum % 3 != 0:
        return 0

    knapsack_w = nums_sum // 3

    # try to fulfil 3 discrete knapsacks (without repetitions)
    for _ in range(3):
        knapsack = fill_discrete_knapsack(knapsack_w, nums)
        if knapsack is None:
            return 0

        used_items, unused_items = backtrack(knapsack, nums)
        groups.append(tuple(nums[i] for i in used_items))
        print(groups, unused_items, nums)
        nums = [num for i, num in enumerate(nums) if i not in set(used_items)]

    # print(groups)

    return 1


def test():
    assert can_be_partitioned([3, 3, 3, 3]) == 0
    assert can_be_partitioned([40]) == 0
    assert can_be_partitioned([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]) == 1
    assert can_be_partitioned([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) == 1
    # assert can_be_split([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6]) == 1
    assert can_be_partitioned([1, 1, 1]) == 1
    assert can_be_partitioned([0, 0, 0]) == 1
    print("OK")


def main():
    _n, nums = input(), list(map(int, input().split()))
    print(can_be_partitioned(nums))


if __name__ == "__main__":
    test()
    main()
