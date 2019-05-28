# python3

# find the minimum number of coins needed to change the input value
# (an integer) into coins with denominations 1, 5, and 10.


def get_change(m):
    c = 0

    while m > 0:
        if m - 10 >= 0:
            m -= 10

        elif m - 5 >= 0:
            m -= 5

        elif m - 1 >= 0:
            m -= 1

        c += 1

    return c


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
