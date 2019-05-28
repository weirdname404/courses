import random as r
import time
import functools


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"{func.__name__.split('_')[-1]!r} in {run_time:.5f} secs")
        return value
    return wrapper_timer


@timer
def count_transitions(p):
    global c1

    p_len = len(p)

    # permutation is surely balanced if there is 1 or 0 elements
    if p_len <= 1:
         return p

    pivot_i = p_len // 2

    # lets balance the permutation
    # first of all we should turn given perm into [X, pivot, Y] model
    # where all x from subset X < pivot and every y from subset Y is > pivot
    for i in p:
        value_i = p.index(i)
        pivot = p[pivot_i]

        # if the value is on the wrong side according to the pivot -> swap them
        if (i > pivot and value_i < pivot_i) or (i < pivot and value_i > pivot_i):
            tmp = i
            p[value_i] = pivot
            p[pivot_i] = tmp
            # +1 transition
            c1 += 1

            return count_transitions(p)

        else:
            continue

    # at this step we assume that our perm is balanced, time to balance subsets recursively
    return count_transitions(p[:pivot_i]) + [pivot] + count_transitions(p[pivot_i + 1:])


@timer
def count_transitions_fast(p):
    global c2

    if len(p) <= 1:
        return p

    min_v = min(p)
    min_vi = p.index(min_v)

    if p[0] != min_v:
        # swap
        tmp = p[0]
        p[0] = min_v
        p[min_vi] = tmp
        c2 += 1

    return [min_v] + count_transitions_fast(p[1:])


def test_compare(func1, func2):
    r_p = r.sample(range(50), 30)
    print(f"random perm - {r_p}")
    res1, res2 = func1(r_p[:]), func2(r_p)

    assert res1 == res2
    assert res1 == list(set(r_p))

    return res1, res2


if __name__ == "__main__":
    c2 = 0
    perm = list(map(int, input().split()))
    print(count_transitions_fast(perm), c2)

