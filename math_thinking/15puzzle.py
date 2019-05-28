#bin/python3

import sys


def count_transpositions(p, c):

    if len(p) <= 1:
        return p, c

    min_v = min(p)
    min_vi = p.index(min_v)

    if p[0] != min_v:
        # swap
        tmp = p[0]
        p[0] = min_v
        p[min_vi] = tmp
        c += 1

    res, c = count_transpositions(p[1:], c)

    return [min_v] + res, c


# swap tile a and b
def swap_tiles(p, a, b):
    pass


def find_solution(p):
    # check if all elements are on their right places (it is enough to check N - 1 elements)
    for i in range(len(p) - 1):
        # houston, we have a problem... hostile element spotted
        if p[i] != i + 1:
            correct_element_i = p.index(i + 1)
            new_p = move_element(p, correct_element_i, i)


def change_empty_space(p, a):
    if a:
        p[p.index(0)] = 16
    else:
        p[p.index(16)] = 0

    return p 


if __name__ == "__main__":
    config = input()
    config = config.split(",") if "," in config else config.split()
    init_perm = list(map(int, config))
    perm = change_empty_space(init_perm.copy(), True)

    # check if initial permutation has solution or not
    # N of transpositions should be even
    res, c = count_transpositions(perm, 0)
    
    try:
        assert c % 2 == 0
        
    except AssertionError:
        sys.exit("N of transpositions is odd. Perm does not have a solution")

    print(change_empty_space(res, False), c)

