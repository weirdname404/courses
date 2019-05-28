# python3

"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
https://leetcode.com/problems/partition-equal-subset-sum/
"""


def can_be_partitioned(nums):
    nums_sum = sum(nums)

    if len(nums) < 2 or nums_sum % 2 != 0:
        return False

    knapsack_w = nums_sum // 2
    return fill_discrete_knapsack(knapsack_w, nums)


def fill_discrete_knapsack(total_weight, weights):
    matrix = [[0] * (total_weight + 1) for _ in range(len(weights) + 1)]

    for i in range(1, len(weights) + 1):
        for knapsack_w in range(1, total_weight + 1):
            num = weights[i - 1]
            case_a = matrix[i - 1][knapsack_w]
            case_b = case_a

            if num <= knapsack_w:
                case_b = matrix[i - 1][knapsack_w - num] + num

            optimal_num = max(case_a, case_b)

            if optimal_num <= knapsack_w:
                matrix[i][knapsack_w] = optimal_num

                if knapsack_w == total_weight and optimal_num == total_weight:
                    return True

    return True if matrix[-1][-1] == total_weight else False


def main():
    print(can_be_partitioned(list(map(int, input().split()))))


if __name__ == "__main__":
    main()
