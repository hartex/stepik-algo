from operator import itemgetter, attrgetter, methodcaller


def find(segments, dots):
    segments_asc = sorted(segments, key=itemgetter(0))
    segments_desc = sorted(segments, key=itemgetter(1))
    print(segments_asc)
    print(segments_desc)
    return dots


def main():
    # number_of_segments, number_of_dots = map(int, input().split())
    # segments = [tuple(map(int, input().split()))
    #             for i in range(0, number_of_segments)]
    # dots = list(map(int, input().split()))

    segments = [(6, 6), (0, 3), (1, 3), (2, 3), (3, 4), (3, 5), (3, 6)]
    dots = [1, 2, 3, 4, 5, 6]
    result = find(segments, dots)
    # print(segments)
    # print(dots)


# Task https://stepik.org/lesson/68403/step/6?unit=45400
# Input:
# 2 3
# 0 5
# 7 10
# 1 6 11
# Output:
# 1 0 0
if __name__ == "__main__":
    main()
