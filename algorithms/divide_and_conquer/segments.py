# python3
import sys
import time


# O(nlogn)
def count_intersections(segments, points):
    print(segments, points)
    if len(points) < 2:
        counter = 0
        # O(n)
        for segment in segments:
            start, end = segment
            if start <= points[0] <= end:
                counter += 1

        return [counter]

    if len(segments) < 2:
        res = [0] * len(points)
        if not segments:
            return res

        start, end = segments[0]
        # O(n)
        for i in range(len(points)):
            if start <= points[i] <= end:
                res[i] += 1

        return res

    segments_pivot = len(segments) // 2
    _pivot_seg_start, pivot_seg_end = segments[segments_pivot - 1]

    right_part_i = 0
    left_part = []

    # O(n)
    for p in points:
        if p <= pivot_seg_end:
            left_part.append(p)
            right_part_i += 1

    left_intersections = count_intersections(segments[:segments_pivot], left_part)
    right_intersections = count_intersections(segments[segments_pivot:], points[right_part_i:])

    return left_intersections + right_intersections


def count_intersections2(segments, points):
    print(segments, points)
    if len(points) == 0:
        return []

    elif len(segments) == 0:
        return [0] * len(points)

    elif len(points) == 1:
        counter = 0
        # O(n)
        for segment in segments:
            start, end = segment
            if start <= points[0] <= end:
                counter += 1

        return [counter]

    elif len(segments) == 1:
        res = [0] * len(points)
        start, end = segments[0]
        # O(n)
        for i in range(len(points)):
            if start <= points[i] <= end:
                res[i] += 1

        return res

    pivot = len(points) // 2
    print("PIVOT IS", points[pivot])

    m = 0
    # O(n)
    for _, end in segments:
        if end < points[pivot]:
            m += 1
        else:
            break

    left_intersections = count_intersections2(segments[:m], points[:pivot])
    right_intersections = count_intersections2(segments[m:], points[pivot:])

    return left_intersections + right_intersections


def timed(f):
    def wrapper(*args):
        t0 = time.perf_counter()
        res = f(*args)
        t1 = time.perf_counter()
        print("%s finished in %.5f" % (f.__name__, (t1 - t0)))
        return res

    return wrapper


def count_intersecs(starts, ends, points):
    res = [0] * len(points)
    points = list(enumerate(points))
    # O(n)
    endpoints = [(start, True) for start in starts]
    # O(n)
    endpoints.extend((end, False) for end in ends)
    # O(nlogn)
    endpoints.sort()
    points.sort(key=lambda x: x[1])

    counter, i = 0, 0
    # O(m + n)
    for index, pt in points:
        while i < len(endpoints) and endpoints[i][0] <= pt:
            counter += 1 if endpoints[i][1] else -1
            i += 1

        res[index] = counter

    return res


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    _m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    # segments = list(zip(starts, ends))

    # O(nlogn)
    # segments.sort()

    # res = count_intersections(segments, points)
    res = count_intersecs(starts, ends, points)

    for i in res:
        print(i, end=' ')


def short_test(*funcs):
    test_cases_endpoints = (([0, 7], [5, 10], [1, 6, 11], [1, 0, 0]),
                            ([-10], [10], [-100, 100, 0], [0, 0, 1]),
                            ([-3, 0, 7], [2, 5, 10], [1, 6], [2, 0]),
                            ([-6, 3], [0, 3], [3, 1], [1, 0])
                            )

    for f in funcs:
        for test_case in test_cases_endpoints:
            starts, ends, points, correct_answ = test_case
            res = f(starts, ends, points)
            try:
                assert res == correct_answ
            except AssertionError as e:
                print("{} gave wrong output".format(f.__name__))
                print(starts, ends, points)
                print("result - {}\ncorrect answer - {}".format(res, correct_answ))
                sys.exit(e)

            else:
                print("{} did good".format(f.__name__))

    print("SHORT DONE")


def long_test(*funcs):
    import random

    for _ in range(20):
        n, m = random.randint(1, 1000), random.randint(1, 1000)
        starts, ends = [], []

        for _ in range(n):
            start = random.randint(-(10 ** 8), 10 ** 8)
            starts.append(start)
            ends.append(random.randint(start + 1, 10 ** 8))

        points = []
        for i in range(1, m):
            points.append(random.randint(-(10 ** 8), 10 ** 8))

        results = []

        for f in funcs:
            # f = timed(f)
            results.append(f(starts, ends, points))

        try:
            assert results[0] == results[1]
        except AssertionError as e:
            for res in results:
                print(res)
            sys.exit(e)

    print("LONG DONE")


if __name__ == '__main__':
    # short_test(naive_count_segments, count_intersecs)
    # long_test(count_intersecs, naive_count_segments)
    main()
