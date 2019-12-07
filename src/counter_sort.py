def counter_sort(array_to_sort):
    count = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
    }

    for i in array_to_sort:
        current = count[str(i)]
        count[str(i)] = current + 1

    result = ""
    for key in count.keys():
        result += (" " + key) * count[key]
    return result


def main():
    number_of_items = int(input())
    array = [int(i) for i in input().split(" ")]
    print(counter_sort(array)[1::])


# Examples
# 5
# 2 3 9 2 9
if __name__ == "__main__":
    main()
