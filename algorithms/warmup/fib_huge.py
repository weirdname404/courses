#python3

# Given two integers n and m, output Fn mod m
# 1 ≤ n ≤ 10**18 , 2 ≤ m ≤ 10**3

# calculate and extend pisano_period till we find its end(!) and then return pisano_
def fib_mod(n, m):
    # m >= 2
    a = [0, 1, 1]
    pp = 3

    if m == 2:
        return a[n % pp]

    # (we didn't find the beginning of the next pisano period) xor (pisano period is 3)
    while (a[:3] != a[-3:]) != (pp == 3):
        a.append((a[-1] + a[-2]) % m)
        pp += 1

    return a[n % (pp - 3)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
