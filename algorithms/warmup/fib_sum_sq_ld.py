#python3
# Compute the last digit of the sum of squares of Fibonacci numbers till Fn

def fib_mod_sum(n):
    mod_seq = [0, 1]
    # mod is 10 -> pisano period is 60
    pp = 60
    fib_i = n % pp

    for _ in range(1, fib_i):
        mod_seq.append((mod_seq[-1] + mod_seq[-2]))

    fn_seq = mod_seq[:fib_i + 1]

    return sum([i**2 for i in fn_seq]) % 10


def main():
    n = int(input())
    print(fib_mod_sum(n))


if __name__ == "__main__":
    main()
