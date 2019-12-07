def fib_digit(n):
    k = 0
    table = [0, 1]
    for i in range(2, n + 1):
        next_value = (table[i - 1] + table[i - 2]) % 10
        table.append(next_value)
        k += 1
    return table[n]


def fib_mode(n, m):
    k = 0
    table = [0, 1]
    for i in range(2, n):
        next_value = (table[i - 1] + table[i - 2]) % m
        table.append(next_value)
        k += 1
        if table[i] == 1 and table[i - 1] == 0:
            break
    return table[n % k]


print(fib_mode(10, 2))
