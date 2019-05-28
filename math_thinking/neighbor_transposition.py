def find_sequence(a, b, c):
    if a == b:
        return c

    for i in range(len(a)):
        i2 = b.index(a[i])

        if i != i2:
            c = neighbor_transposition(c, [i, i2])
            tmp = a[i]
            a[i] = a[i2]
            a[i2] = tmp
            find_sequence(a, b, c)

        else: continue

    return c


def neighbor_transposition(c, d):
    init = d[0]
    
    while d[0] != d[1]:
        i = d[0]
        c.append((i, i + 1))
        d[0] += 1
    
    d[1] -= 1
    
    while d[1] != init:
        c.append((d[1], d[1] - 1))
        d[1] -= 1
        
        
    return c


if __name__ == "__main__":
    a, b = input().split()
    try:
        assert(len(a) == len(b))
    except AssertionError as e:
        raise e

    print(find_sequence(list(a), list(b), []))


