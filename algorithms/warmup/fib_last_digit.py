# Given an integer n, find the last digit of the nth Fibonacci number

def fib_digit(n):
    a, b = 0, 1
    for _ in range(1, n):
        res = (a + b) % 10
        a, b = b, res
    
    return res


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

