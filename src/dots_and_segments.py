def sort_by_right(segment):
    return segment[1]


def find_dots(segments):
    segments.sort(key=sort_by_right)
    right_most = segments[0][1]
    dots = [right_most]
    for i in range(1, len(segments)):
        left_part = segments[i][0]
        if left_part > right_most:
            right_most = segments[i][1]
            dots.append(right_most)

    return dots


def main():
    number_of_segments = int(input())
    segments = []
    for i in range(0, number_of_segments):
        left, right = map(int, input().split())
        segments.append((left, right))

    dots = find_dots(segments)
    print(len(dots))
    print(' '.join(str(i) for i in dots))


# Examples
# 4
# 4 7
# 1 3
# 2 5
# 5 6
if __name__ == "__main__":
    main()
