def diff(char1, char2):
    if char1 == char2:
        return 0
    else:
        return 1


def edit_distance(s1, s2):
    len1, len2 = len(s1), len(s2)
    double_d = [[None for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    def calculate(i, j):
        if double_d[i][j]:
            return double_d[i][j]
        else:
            if i == 0:
                double_d[i][j] = j
                return j
            elif j == 0:
                double_d[i][j] = i
                return i
            else:
                ins = calculate(i, j - 1) + 1
                deletion = calculate(i - 1, j) + 1
                sub = calculate(i - 1, j - 1) + diff(s1[i - 1], s2[j - 1])
                minimum = min(ins, deletion, sub)
                double_d[i][j] = minimum
                return minimum

    return calculate(len1, len2)


def main():
    first_string = input()
    second_string = input()
    print(edit_distance(first_string, second_string))


# Examples
# short
# ports
if __name__ == "__main__":
    main()
