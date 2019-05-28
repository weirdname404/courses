# python3

import sys


def get_intersections(starts, ends, points):
    res = [0] * len(points)
    # (value, point_type, index)
    starts = [(a, 0, -1) for a in starts]
    points = [(b, 1, i) for i, b in enumerate(points)]
    ends = [(c, 2, -1) for c in ends]

    coordinates = starts + ends + points
    coordinates.sort()

    counter = 0
    for point in coordinates:
        coord, point_type, i = point
        # start
        if point_type == 0:
            counter += 1
        # end
        elif point_type == 2:
            counter -= 1
        # point
        else:
            res[i] = counter

    return res


def test():
    test_cases = (([0, 7], [5, 10], [1, 6, 11], [1, 0, 0]),
                  ([-10], [10], [-100, 100, 0], [0, 0, 1]),
                  ([-3, 0, 7], [2, 5, 10], [1, 6], [2, 0]),
                  ([-6, 3], [0, 3], [3, 1], [1, 0])
                  )

    for test_case in test_cases:
        starts, ends, points, correct_answ = test_case
        assert get_intersections(starts, ends, points) == correct_answ

    print("OK")


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    res = get_intersections(starts, ends, points)

    for x in res:
        print(x, end=' ')


if __name__ == '__main__':
    test()
    main()
