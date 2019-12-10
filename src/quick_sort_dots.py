from bisect import bisect_left, bisect_right


def find(segments, dots):
    segments_asc = sorted([r[0] for r in segments])
    segments_desc = sorted([r[1] for r in segments])
    result = []
    for dot in dots:
        asc_index = bisect_right(segments_asc, dot)
        desc_index = bisect_left(segments_desc, dot)
        result.append(asc_index - desc_index)
    return result


def main():
    number_of_segments, number_of_dots = map(int, input().split())
    segments = [tuple(map(int, input().split()))
                for i in range(0, number_of_segments)]
    dots = list(map(int, input().split()))
    result = find(segments, dots)
    print(result)


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
