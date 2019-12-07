def binary_search(where_to_search, value):
    def inner(list_to_search, item, start, end):
        if start > end:
            return -1

        middle_index = (end + start) // 2
        middle_item = list_to_search[middle_index]
        if middle_item == item:
            return middle_index
        elif item < middle_item:
            return inner(list_to_search, item, start, middle_index - 1)
        else:
            return inner(list_to_search, item, middle_index + 1, end)

    return inner(where_to_search, value, 0, len(where_to_search) - 1)


def main():
    sorted_array = [int(i) for i in input().split(" ")][1::]
    values_to_search = [int(i) for i in input().split(" ")][1::]
    result = ""
    for value in values_to_search:
        index = binary_search(sorted_array, value)
        result += " " + str(index + 1 if index >= 0 else index)

    print(result[1::])


# Examples
# 9 1 2 5 8 12 13 24 30 99
# 7 8 1 23 1 11 0 99
if __name__ == "__main__":
    main()
