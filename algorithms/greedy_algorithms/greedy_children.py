# python3


def func(a):
    c, youngest_boi = 0, 0
    max_gap = 12
    max_age = a[youngest_boi] + max_gap

    for i in range(len(a)):
        if a[i] > max_age:
            c += 1
            max_age = a[i] + max_gap

    return c + 1


if __name__ == "__main__":
    a = list(map(int, input().split(',')))
    print(func(sorted(a)))
