# python3
"""
Compute the length of a longest common subsequence of two sequences.
"""
import sys


# the approach of building matrix is the same as in edit distance problem
# but in this case we are searching for MATCHES
# firstly, we don't need MISMATCH anymore
# let's change rewards, only MATCH gets +1 point
def get_lcs(a, b):
    a_l = len(a) + 1
    b_l = len(b) + 1
    matrix = [[0 for _ in range(b_l)] for _ in range(a_l)]

    for i in range(1, a_l):
        for j in range(1, b_l):
            insertion = matrix[i][j - 1]
            deletion = matrix[i - 1][j]
            match = matrix[i - 1][j - 1] + 1

            if a[i - 1] == b[j - 1]:
                matrix[i][j] = match
            else:
                matrix[i][j] = max(insertion, deletion)

    return matrix[-1][-1]


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(get_lcs(a, b))


def test():
    assert get_lcs([2, 7, 5], [2, 5]) == 2
    assert get_lcs([7], [1, 2, 3, 4]) == 0
    assert get_lcs([2, 7, 8, 3], [5, 2, 8, 7]) == 2


if __name__ == "__main__":
    test()
    main()
