# python3

"""
You are given a set
of segments on a line and your goal is to mark as few points on a line as possible
so that each segment contains at least one marked point.
"""

import sys
import random as r
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


# return optimal intersection points
def optimal_points(segments):
    opt_point = segments[0].end
    points = [opt_point]

    for i in range(1, len(segments)):
        seg_start, seg_end = segments[i].start, segments[i].end

        if opt_point > seg_end or opt_point < seg_start:
            opt_point = segments[i].end
            points.append(opt_point)

    return points


def generate_test_sample():
    lim = 10 ** 9 + 1
    n = r.randrange(1, 100)
    segs = []

    for _ in range(n):
        a = r.randrange(0, lim)
        b = r.randrange(a, lim)
        segs.append(Segment(a, b))

    return segs


if __name__ == '__main__':
    raw_inp = sys.stdin.read()
    n, *data = map(int, raw_inp.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(sorted(segments, key=lambda x: x.end))
    print(len(points))
    for i in points:
        print(i, end=' ')
