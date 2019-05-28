# python3
"""
The goal of this problem is to implement the algorithm for 
computing the edit distance between two strings.
"""


def get_edit_distance(a, b):
    a_l = len(a) + 1
    b_l = len(b) + 1
    matrix = create_matrix(a_l, b_l)

    for i in range(1, a_l):
        for j in range(1, b_l):
            insertion = matrix[i][j - 1] + 1
            deletion = matrix[i - 1][j] + 1
            match = matrix[i - 1][j - 1]
            mismatch = matrix[i - 1][j - 1] + 1

            if a[i - 1] == b[j - 1]:
                matrix[i][j] = min(insertion, deletion, match)
            else:
                matrix[i][j] = min(insertion, deletion, mismatch)

    print(reconstruct_alignment(a, b, matrix))

    return matrix[-1][-1]


def reconstruct_alignment(a, b, matrix):
    from collections import deque

    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    str_a = deque()
    str_b = deque()

    while i > 0 and j > 0:
        # insert, delete, (mis)match
        _v, index = min((matrix[i][j - 1], 0), (matrix[i - 1][j], 1), (matrix[i - 1][j - 1], 2))
        if index == 0:
            j -= 1
            str_a.appendleft('-')
            str_b.appendleft(b[j])
        elif index == 1:
            i -= 1
            str_a.appendleft(a[i])
            str_b.appendleft('-')
        else:
            i -= 1
            j -= 1
            str_a.appendleft(a[i])
            str_b.appendleft(b[j])

    return "".join(str_a), "".join(str_b)


def create_matrix(a_l, b_l):
    matrix = []
    for i in range(a_l):
        row = []
        for j in range(b_l):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(0)
        matrix.append(row)

    return matrix


def main():
    print(get_edit_distance(input(), input()))


def test():
    assert get_edit_distance("ab", "ab") == 0
    assert get_edit_distance("short", "ports") == 3
    assert get_edit_distance("editing", "distance") == 5


if __name__ == "__main__":
    test()
    main()
