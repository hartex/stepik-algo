def ladder_rec(values):
    last_index = len(values) - 1
    calcs = [None] * len(values)

    def inner(index, total):
        if index == last_index:
            return total
        # a last but one element
        elif index + 1 == last_index:
            calcs[index + 1] = values[index + 1]
            return inner(index + 1, total + values[index + 1])
        else:
            one_step_total = 0
            two_step_total = 0
            if calcs[index + 1]:
                one_step_total = calcs[index + 1]
            else:
                one_step_total = values[index + 1] + inner(index + 1, total)
                calcs[index + 1] = one_step_total

            if calcs[index + 2]:
                two_step_total = calcs[index + 2]
            else:
                two_step_total = values[index + 2] + inner(index + 2, total)
                calcs[index + 2] = two_step_total

            return max(one_step_total, two_step_total)

    return inner(-1, 0)


def main():
    _ = int(input())
    values = list(map(int, input().split()))
    result = ladder_rec(values)
    print(result)


# https://stepik.org/lesson/68418/step/4?unit=45415
# Examples:
# 7
# 1 1 -2 -4 -6 2 2
# Result:
# 2
if __name__ == "__main__":
    main()
