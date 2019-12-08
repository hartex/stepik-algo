
def main():
    number_of_segments, number_of_dots = map(int, input().split())
    segments = [tuple(map(int, input().split())) for i in range (0, number_of_segments)]
    dots = list(map(int, input().split()))
    print(segments)
    print(dots)


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