#python3

def fib(n):
    if n < 2:
        return n

    f_nums = [0, 1]

    for _ in range(1, n):
        res = f_nums[-1] + f_nums[-2]
        f_nums.append(res)

    return f_nums


if __name__ == "__main__":
    a = int(input())
    print(fib(a))

