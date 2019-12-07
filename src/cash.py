def find_change(n):
    changes = {
        '25': 0,
        '10': 0,
        '5': 0,
        '1': 0
    }

    while n:
        remaining = 0
        if n >= 25:
            remaining = n % 25
            changes['25'] = (n - remaining) / 25
        elif n >= 10:
            remaining = n % 10
            changes['10'] = (n - remaining) / 10
        elif n >= 5:
            remaining = n % 5
            changes['5'] = (n - remaining) / 5
        else:
            changes['1'] = n
            remaining = 0
        n = remaining
    return changes


def main():
    n = int(input())
    result = find_change(n)
    print(result)


# Examples
# 4
if __name__ == "__main__":
    main()
