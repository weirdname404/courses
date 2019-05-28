# python3
"""
You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
each point, the number of segments that contain this point.
"""
import sys
import random
import time


def cool_count_p_s(starts, ends, points):
    segments = {}
    res = []

    # O(n)
    for i in range(len(starts)):
        segments[starts[i]] = ends[i]

    # O(n)
    for point in points:
        segments[point] = None

    # O(n)
    starts += points

    # O(nlogn)
    starts.sort()

    # O(n**2)
    for point in points:
        m = binary_search(starts, point)
        count = 0
        for i in starts[:m]:
            if segments[i] and segments[i] >= point:
                count += 1

        res.append(count)

    return res


def count_p_s(starts, ends, points):
    res = []

    for point in points:
        a = starts + [point]
        b = ends + [point]
        a.sort()
        b.sort()
        start_m = binary_search(a, point)
        end_m = binary_search(b, point)
        x = a[:start_m]
        y = b[end_m + 1:]
        print(x, y)

        res.append(min(len(x), len(y)))

    return res


def binary_search(arr, point):
    left, right = 0, len(arr) - 1

    while left <= right:
        m = (left + right) // 2

        if point == arr[m]:
            return m
        elif point > arr[m]:
            left = m + 1
        else:
            right = m - 1

    return None

# def binary_search(ranges, point):
#     left, right = 0, len(ranges) - 1
#
#     while left <= right:
#         m = (left + right) // 2
#         start, end = ranges[m]
#
#         if point == start:
#             return m
#
#         elif point < start:
#             right = m - 1
#
#         elif point > end:
#             left = m + 1
#
#     return None


def fast_count_segments(starts, ends, points):
    cnt = [0 for _ in range(len(points))]
    ranges = sorted(zip(starts, ends))
    for i in range(len(points)):
        point = points[i]
        start_p = binary_search(ranges, point - 1)
        end_p = binary_search(ranges, point + 1)

    return cnt


def fast_count_segments2(ranges, points):
    points_l = len(points)

    if points_l < 2:
        if points_l == 0:
            return []
        cnt = 0
        for start, end in ranges:
            if start <= points[0] <= end:
                cnt += 1
        return [cnt]

    left = fast_count_segments2(ranges, points[:points_l // 2])
    right = fast_count_segments2(ranges, points[points_l // 2:])

    return left + right


def count_intersections2(segments, points):
    print("\n", segments, points, "\n")
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


def naive_count_segments2(ranges, points):
    cnt = [0] * len(points)

    for i in range(len(points)):
        for start, end in ranges:
            if start <= points[i] <= end:
                cnt[i] += 1
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def time_test(a, *f):
    time_arr1 = []
    time_arr2 = []
    f1, f2 = f

    for _ in range(a):
        n, m = random.randint(1, 10), random.randint(1, 10)
        ranges = []

        for _ in range(n):
            start = random.randint(-100, 100)
            ranges.append((start, random.randint(start + 1, 130)))

        points = [random.randint(-100, 100)]
        for i in range(1, m):
            points.append(random.randint(points[i - 1], 130))

        ranges.sort(key=lambda x: x[1])

        t0 = time.perf_counter()
        res1 = f1(ranges, points)
        t1 = time.perf_counter()
        time_arr1.append(t1 - t0)

        t0 = time.perf_counter()
        res2 = f2(ranges, points)
        t1 = time.perf_counter()
        time_arr2.append(t1 - t0)

        try:
            assert res1 == res2
        except AssertionError:
            print(ranges, points, end="\n")
            print(f"f1.__name__ has following res {res1}")
            print(f"f2.__name__ has following res {res2}")

    print("%s %.5f secs" % (f1.__name__, sum(time_arr1) / a))
    print("%s %.5f secs" % (f2.__name__, sum(time_arr2) / a))


def test(n):
    time_test(n, naive_count_segments2, count_intersections2)


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    # ranges = list(zip(starts, ends))
    # use fast_count_segments
    cnt = cool_count_p_s(starts, ends, points)
    # cnt = fast_count_segments2(ranges, points)
    for x in cnt:
        print(x, end=' ')


if __name__ == '__main__':
    test(5)
    #main()
