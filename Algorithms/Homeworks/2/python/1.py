import time
import random


def brute_force_multiply(x, y):
    strx = list(reversed(str(x)))
    stry = list(reversed(str(y)))
    y_length = len(stry)
    value = 0
    for n in range(len(strx)):
        xn = int(strx[n])
        for m in range(y_length):
            ym = int(stry[m])
            power = 10 ** (n + m)
            value += xn * ym * power
    return value


def karatsuba(a, b):
    if a < 10 and b < 10:
        return a * b
    else:
        a_str = str(a)
        b_str = str(b)
        n = max(len(a_str), len(b_str))
        a_str = "0" * (n - len(a_str)) + a_str
        b_str = "0" * (n - len(b_str)) + b_str
        m = n // 2
        a0 = int(a_str[m:])
        a1 = int(a_str[:m])

        b0 = int(b_str[m:])
        b1 = int(b_str[:m])

        c2 = karatsuba(a1, b1)
        c0 = karatsuba(a0, b0)
        c1 = karatsuba(a1 + a0, b1 + b0) - c2 - c0

        return c2 * 10 ** (2 * (n - m)) + c1 * 10 ** (n - m) + c0


def time_functions():
    for i in range(1, 60):
        magnitude = 10**i
        naive_time = 0
        karatsuba_time = 0

        for _ in range(100):
            start = time.time()
            a = random.randint(magnitude / 10, magnitude)
            b = random.randint(magnitude / 10, magnitude)
            k = karatsuba(a, b)
            end = time.time()
            karatsuba_time += end - start
            start = time.time()
            n = brute_force_multiply(a, b)
            end = time.time()
            naive_time += end - start
            if k != n:
                raise Exception(f"Results don't match for {a} and {b}")

        print(
            i,
            karatsuba_time < naive_time,
            "- BruteForce:",
            naive_time / 100,
            "- Karatsuba:",
            karatsuba_time / 100,
        )


time_functions()
