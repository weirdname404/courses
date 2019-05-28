# python3

# Given two sequences we need to partition them into n pairs (a, b)
# such that the sum of their products is maximized.


def func(n, a, b):
    product = 0

    for i in range(n):
        product += a[i] * b[i]

    return product


if __name__ == "__main__":
    n = int(input())
    a, b = [map(int, input().split()) for _ in range(2)]
    print(func(n, sorted(a), sorted(b)))
