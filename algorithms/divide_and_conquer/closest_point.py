# Uses python3
"""
Given n points on a plane, find the smallest distance between a pair of two (different) points.
"""
import sys
import math

# WRONG
def minimum_distance(points):
    min_distance_x = float("inf")
    min_distance_y = float("inf")

    x_sorted_points = sorted(points)
    for i in range(1, len(points)):
        x1, y1 = x_sorted_points[i - 1]
        x2, y2 = x_sorted_points[i]
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        min_distance_x = min(min_distance_x, distance)

    y_sorted_points = sorted(points, key=lambda x: x[1])
    for i in range(1, len(points)):
        x1, y1 = y_sorted_points[i - 1]
        x2, y2 = y_sorted_points[i]
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        min_distance_y = min(min_distance_y, distance)

    return min(min_distance_x, min_distance_y)


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    print("{0:.9f}".format(minimum_distance(points)))


if __name__ == '__main__':
    main()
