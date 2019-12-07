def find_subsequence(items):
    d = [1 for _ in range(len(items))]
    for i in range(len(items)):
        d[i] = 1
        for j in range(i):
            if items[i] % items[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)


def main():
    number_of_items = int(input())
    array = [int(i) for i in input().split(" ")]
    print(find_subsequence(array))


# Examples
# 4
# 3 6 7 12
if __name__ == "__main__":
    main()


