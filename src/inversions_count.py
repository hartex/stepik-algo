def merge(array_to_count, array1, array2):
    inversions = 0
    i, j = 0, 0
    len1 = len(array1)
    len2 = len(array2)
    while i < len1 or j < len2:
        if i == len1:
            array_to_count[i + j] = array2[j]
            j += 1
        elif j == len2:
            array_to_count[i + j] = array1[i]
            i += 1
        elif array1[i] <= array2[j]:
            array_to_count[i + j] = array1[i]
            i += 1
        else:
            array_to_count[i + j] = array2[j]
            inversions += len1 - i
            j += 1
    return inversions


def inv_count(array_to_count):
    length = len(array_to_count)
    if length < 2:
        return 0
    else:
        middle = length // 2
        left = array_to_count[:middle]
        right = array_to_count[middle:]
        return inv_count(left) + inv_count(right) + merge(array_to_count, left, right)


def main():
    number_of_items = int(input())
    array = [int(i) for i in input().split(" ")]
    print(inv_count(array))


# Examples
# 8
# 6 2 4 3 11 9 2 9
if __name__ == "__main__":
    main()
