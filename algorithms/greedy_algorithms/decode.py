#python3


def decode(code, d):
    res = ''
    acc = ''

    for s in code:
        acc += s
        if acc in d:
            res += d[acc]
            acc = ''
    return res


if __name__ == "__main__":
    d = {}
    n, code_len = map(int, input().split())

    for _ in range(n):
        v, k = input().split(': ')
        d[k] = v

    code = input()
    print(decode(code, d))
