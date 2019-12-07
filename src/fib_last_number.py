def resolution(n, m):
    a = gcd(n, m)
    return fib_digit(int(a))


def fib_digit(n):
    k = 0
    table = [0, 1]
    for i in range(2, n + 1):
        next_value = (table[i - 1] + table[i - 2]) % 10
        table.append(next_value)
        k += 1
    return table[n]


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def main():
    n, m = map(int, input().split())
    print(resolution(n, m))


if __name__ == "__main__":
    main()
