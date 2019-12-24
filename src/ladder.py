def ladder_rec(values):
    val_len = len(values)
    calcs = [None] * len(values)

    def inner(index, total):
        if index == val_len:
            return total
        elif index + 1 == val_len:
            calcs[index] = values[index]
            return inner(index + 1, total + values[index])
        else:
            one_step = calcs[index]
            if one_step is not None:
                if calcs[index] else inner(index + 1)
            calcs[index] = one_step
            two_step = calcs[index + 1] if calcs[index + 1] else inner(index + 2)
            calcs[index] = two_step
            return inner(one_step if one_step > two_step else two_step)

    return inner(0, 0)


# Подсказка: можно создать вектор D, в котором D[i] - максимальная сумма первых i чисел,
# и на каждой итерации брать максимум из двух вариантов перехода по лестнице.

def main():
    # _ = int(input())
    # values = list(map(int, input().split()))
    values = [1, 1, -2, -4, -6, 2, 2]
    result = ladder_rec(values)
    print(result)


# Examples
# 3
# -1 2 1
if __name__ == "__main__":
    main()
