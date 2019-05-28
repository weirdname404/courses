# python3
"""
Compute the length of a longest common subsequence of three sequences.
"""

import sys


def lcs3(a, b, c):
    a_l = len(a) + 1
    b_l = len(b) + 1
    c_l = len(c) + 1

    # 3d array
    matrix = [[[0 for _ in range(c_l)] for _ in range(b_l)] for _ in range(a_l)]

    for x in range(1, a_l):
        for y in range(1, b_l):
            for z in range(1, c_l):
                insert_1 = matrix[x][y - 1][z]
                insert_2 = matrix[x][y][z - 1]
                insert_3 = matrix[x][y - 1][z - 1]
                del_1 = matrix[x - 1][y][z - 1]
                del_2 = matrix[x - 1][y][z]
                match = matrix[x - 1][y - 1][z - 1] + 1

                if a[x - 1] == b[y - 1] == c[z - 1]:
                    matrix[x][y][z] = match
                else:
                    matrix[x][y][z] = max(del_1, del_2, insert_1, insert_2, insert_3)

    return matrix[-1][-1][-1]


def test():
    assert lcs3([1, 2, 3], [2, 1, 3], [1, 3, 5]) == 2
    assert lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]) == 3


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # parsing data
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    print(lcs3(a, b, c))


if __name__ == '__main__':
    test()
    main()
