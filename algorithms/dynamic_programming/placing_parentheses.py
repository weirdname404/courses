# python3
"""
In this problem, your goal is to add parentheses to a given arithmetic
expression to maximize its value.
"""


def get_max_value(nums, ops):
    ops_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }

    n = len(nums)

    # create 2 matrices (for min and max values)
    min_matrix = [[0] * n for _ in range(n)]
    max_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        min_matrix[i][i] = nums[i]
        max_matrix[i][i] = nums[i]

    for s in range(1, n):
        for i in range(n - s):
            """
            s is the number of diagonal (j - i = s)

            **** <- s = 3 (1)
            -*** <- s = 2 (1, 1)
            --** <- this diagonal (1, 1, 1) where s = 1
            ---* <- s = 0 (we already have it => skip)

            we are iterating diagonally
            """
            j = i + s
            min_matrix[i][j], max_matrix[i][j] = get_min_max(i, j, (ops, ops_dict), (min_matrix, max_matrix))

    return max_matrix[0][n - 1]


def get_min_max(i, j, operations, matrices):
    ops, ops_dict = operations
    min_matrix, max_matrix = matrices
    min_v = float("inf")
    max_v = float("-inf")

    for k in range(i, j):
        operation = ops_dict[ops[k]]

        a = operation(max_matrix[i][k], max_matrix[k + 1][j])
        b = operation(max_matrix[i][k], min_matrix[k + 1][j])
        c = operation(min_matrix[i][k], max_matrix[k + 1][j])
        d = operation(min_matrix[i][k], min_matrix[k + 1][j])

        min_v = min(min_v, a, b, c, d)
        max_v = max(max_v, a, b, c, d)

    return min_v, max_v


def parse_equation(eq):
    operations = {'-', '+', '*'}
    nums = []
    ops = []
    num = ""

    for ch in eq:
        if ch in operations:
            ops.append(ch)
            nums.append(int(num))
            num = ""

        else:
            num += ch

    nums.append(int(num))

    return nums, ops


def test():
    nums, ops = parse_equation("5-8+7*4-8+9")
    assert get_max_value(nums, ops) == 200


def main():
    nums, ops = parse_equation(input())
    print(get_max_value(nums, ops))


if __name__ == "__main__":
    test()
    main()
