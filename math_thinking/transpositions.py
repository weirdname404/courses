def find_sequence(a, b, c):
    if a == b:
        return c
    
    for i in range(len(a)):
        i2 = b.index(a[i])

        if i != i2: 
            c.append((i, i2))
            tmp = a[i]
            a[i] = a[i2]
            a[i2] = tmp
            print(''.join(a))
            find_sequence(a, b, c)


    return c


if __name__ == "__main__":
    a, b = input().split()
    try:
        assert(len(a) == len(b))
    except AssertionError as e: 
        raise e

    print(find_sequence(list(a), list(b), []))

