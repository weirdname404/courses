# python3
"""
Given n gold bars, find the maximum weight of gold that fits into a bag of capacity W
"""
import sys


def get_optimal_w_of_gold(W, w):
    # matrix of values for all knapsack weight states and for every item
    matrix = [[0 for _ in range(W + 1)] for _ in range(len(w) + 1)]

    for i in range(1, len(w) + 1):
        for knapsack_w in range(1, W + 1):
            gold_w = w[i - 1]

            # due to finite number of elements we have to check 2 cases
            # A: n-th item is NOT TAKEN (it's might be too heavy or not that valuable)
            # in this case let's just stick to the optimal solution we already have (i - 1)
            case_a = matrix[i - 1][knapsack_w]

            # if we are ABLE to take n-th item -> consider case B
            if gold_w <= knapsack_w:
                # B: n-th item is TAKEN
                # in this case, we took knapsack state which is definitely without n-th item
                # and added n-th item weight to it
                case_b = matrix[i - 1][knapsack_w - gold_w] + gold_w
            else:
                # n-th item is too heavy, we definitely didn't take it
                case_b = case_a

            # choose case which is more valuable
            acc_gold_w = max(case_a, case_b)

            # if accumulated gold weight fits in our CURRENT knapsack
            if acc_gold_w <= knapsack_w:
                # put it
                matrix[i][knapsack_w] = acc_gold_w

    return matrix[-1][-1]


def test():
    assert get_optimal_w_of_gold(10, [1, 4, 8]) == 9
    assert get_optimal_w_of_gold(8, [3, 4, 6]) == 7


def main():
    input = sys.stdin.read()
    W, n, *w = map(int, input.split())
    print(get_optimal_w_of_gold(W, w))


if __name__ == "__main__":
    test()
    main()
