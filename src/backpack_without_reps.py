def fill_backpack(weight_limit, items):
    table = [[0 for _ in range(len(items))] for _ in range(weight_limit + 1)]
    for i in range(0, len(items)):
        current_item = items[i]
        for w in range(1, weight_limit + 1):
            table[w][i] = table[w][i - 1]
            if current_item <= w:
                table[w][i] = max(table[w][i], table[w - current_item][i - 1] + current_item)
    return table[weight_limit][len(items) - 1]


def main():
    weight_limit, _ = map(int, input().split())
    weights = map(int, input().split())
    result = fill_backpack(weight_limit, list(weights))
    print(result)


# Examples
# 10 3
# 1 4 8

# 10 4
# 6 3 4 2
if __name__ == "__main__":
    main()
