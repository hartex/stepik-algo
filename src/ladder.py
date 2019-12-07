import itertools

def ladder(values):
    result = 0
    length = len(values)
    i = 0
    while i < length:
        if i == length - 1 or i == length - 2:
            result += values[i]
        else:
            current_value = values[i]
            next_value = values[i + 1]
            if result + next_value > result + current_value:
                i += 1
                current_value = next_value
            result += current_value
        i += 1

    return result


def main():
    _ = int(input())
    # values = list(map(int, input().split()))
    values = input().split()
    # result = ladder(values)
    result = list(itertools.combinations(values, 2))
    print(result)


# Examples
# 3
# -1 2 1
if __name__ == "__main__":
    main()
