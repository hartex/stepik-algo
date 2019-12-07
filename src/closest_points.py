from typing import NamedTuple
from math import sqrt
from itertools import combinations


class Point(NamedTuple):
    x: float
    y: float


def filter_dots_in_strip(strip, points):
    """
    Filters dots that lay only inside the strip
    :param strip: strip denotes range where dots must lay down
    :param points: list of dots to filter
    :return: filtered list of dots
    """
    return [point for point in points if strip[0] <= point.x <= strip[1]]


def calc_distance(point_1, point_2):
    return (point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2


def strip_closest(x_sorted, y_sorted, best_pair):
    """
    Finds minimum distance between dots in the strip
    :param x_sorted: list of dots sorted by x
    :param y_sorted: list of dots sorted by y
    :param best_pair: two dots closest to each other founded by previous computations and their distance
    :return: best pair and it's minimum distance
    """
    minimum = best_pair[2]
    size = len(x_sorted)
    middle_x = x_sorted[size // 2].x  # middle x in x_sorted
    strip = (middle_x - minimum, middle_x + minimum)
    in_strip = filter_dots_in_strip(strip, y_sorted)
    strip_len = len(in_strip)

    min_in_strip = min(((in_strip[i], in_strip[j], calc_distance(in_strip[i], in_strip[j]))
                        for i in range(strip_len - 1)
                        for j in range(i + 1, min(i + 7, strip_len))), key=pair_key, default=best_pair)

    return min(best_pair, min_in_strip, key=pair_key)


def pair_key(pair):
    return pair[2]


def brute_force(points):
    """
    Brute force algorithm to calculate minimum distance between points
    It seem like this algorithm works for O(n*n) but actually it works for O(1)
    :param points: list of points which length is <= 3
    :return: minimum distances between two dots
    """
    if len(points) == 2:
        return points[0], points[1], calc_distance(points[0], points[1])

    return min(((pair[0], pair[1], calc_distance(pair[0], pair[1]))
                for pair in combinations(points, 2)), key=pair_key)


def find_min_distance(x_sorted, y_sorted):
    size = len(x_sorted)
    if size < 16:
        return brute_force(x_sorted)

    middle = size // 2
    middle_x = x_sorted[middle].x
    left_x_part, right_x_part = x_sorted[:middle], x_sorted[middle:]

    left_y_part, right_y_part = [], []
    for item in y_sorted:  # split array sorted by "y" into 2 arrays to use them later
        if item.x <= middle_x:
            left_y_part.append(item)
        else:
            right_y_part.append(item)

    # recursively finds minimum distance in sub arrays
    left_result = find_min_distance(left_x_part, left_y_part)
    right_result = find_min_distance(right_x_part, right_y_part)
    resulted_pair = min(left_result, right_result, key=pair_key)

    # finds minimum distance inside strip
    strip_result = strip_closest(x_sorted, y_sorted, resulted_pair)
    resulted_pair = min(resulted_pair, strip_result, key=pair_key)
    return resulted_pair


def main():
    number_of_points = int(input())
    array_of_points = [Point(*map(int, input().split(" "))) for _ in range(0, number_of_points)]

    # let's sort by x and y beforehand to achieve O(n * log n) performance
    x_sorted = sorted(array_of_points, key=lambda point: point.x)
    y_sorted = sorted(array_of_points, key=lambda point: point.y)
    _, _, min_distance = find_min_distance(x_sorted, y_sorted)
    print("%.9f" % sqrt(min_distance))


# Input example
# 11
# 4 4
# -2 -2
# -3 -4
# -1 3
# 2 3
# -4 0
# 1 1
# -1 -1
# 3 -1
# -4 2
# -2 4
if __name__ == "__main__":
    main()
