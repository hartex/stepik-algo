def find_terms(n):
    if n == 1 or n == 2:
        return '{}'.format(n), 1
    else:
        numbers = []
        result = 0
        for i in range(1, n):
            if result < n:
                if result + i > n:
                    what_to_add = result + i - n
                    result = n
                    next_number = int(numbers.pop()) + i - what_to_add
                    numbers.append(str(next_number))
                else:
                    result += i
                    numbers.append(str(i))

        return ' '.join(numbers), len(numbers)


def main():
    n = int(input())
    result1 = find_terms(n)
    print(result1[1])
    print(result1[0])


# Examples
# 42
if __name__ == "__main__":
    main()
