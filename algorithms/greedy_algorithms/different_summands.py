# python3
'''
The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
distinct positive integers as possible.
'''


def naive_find_n_prizes(n):
    prizes = []
    k = 0

    while n != 0:
        k += 1
        n -= k

        if n < 0:
            n += prizes.pop()

        prizes.append(k)

    return prizes


if __name__ == '__main__':
    n = int(input())
    prizes = naive_find_n_prizes(n)
    print(len(prizes))
    print(*prizes, sep=' ')
