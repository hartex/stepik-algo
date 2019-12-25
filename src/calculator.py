def calc_rec(n):
    cache = {}

    def inner(value, intermediates):
        if value == n:
            return intermediates
        else:
            x3 = value * 3
            x2 = value * 2
            x_plus_1 = value + 1

            if x3 <= n:
                x3_res = inner(x3, intermediates.append(x3))
                x2_res = inner(x2, intermediates.append(x2))
                x_plus_1_res = inner(x_plus_1, intermediates.append(x_plus_1))
                min_res = min([
                    (len(x3_res), x3_res),
                    (len(x2_res), x2_res),
                    (len(x_plus_1_res), x_plus_1_res)
                 ], key=lambda v: v[0])
                return inner(f, min_res[1])
            elif x2 <= n:
                x2_res = inner(x2, intermediates.append(x2))
                x_plus_1_res = inner(x_plus_1, intermediates.append(x_plus_1))
                return x2_res if len(x2_res) < len(x_plus_1_res) else x_plus_1_res
            else:
                return inner(x_plus_1, intermediates.append(x_plus_1))

    return inner(1, [1])


def main():
    value = int(input())
    result = calc_rec(value)
    print(*result)


# https://stepik.org/lesson/68418/step/5?unit=45415
# Examples:
# 96234
# Result:
# 14
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
if __name__ == "__main__":
    main()
