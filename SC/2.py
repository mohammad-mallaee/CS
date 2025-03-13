# Input: points x_0, x_1, ..., x_n, function values f_0,f_1, ..., f_n,
# derivative values f'_0, f'_1, ..., f'_n and the point alpha
# Problem:
# A. Proximate the value of the function at the point alpha using the Hermite-Lagrange polynomial
# B. Proximate the value of the integral of the function from a to b using Trapozoidal rule and in the i-th subinterval

def L(i, alpha, x):
    result = 1
    for j in range(len(x)):
        if i != j:
            result *= (alpha - x[j]) / (x[i] - x[j])
    return result


def L_prime(i, alpha, x):
    result = 0
    for j in range(len(x)):
        if j != i:
            r = 1
            for k in range(len(x)):
                if k != i and k != j:
                    r *= alpha - x[k]
                if k != i:
                    r /= x[i] - x[k]
            result += r
    return result


def h_0(i, alpha, x):
    return (1 - 2 * (alpha - x[i]) * L_prime(i, x[i], x)) * (L(i, alpha, x) ** 2)


def h_1(i, alpha, x):
    return (alpha - x[i]) * (L(i, alpha, x) ** 2)


def H(alpha, x, f, f_prime):
    n = len(x)
    result = 0
    for i in range(n):
        result += f[i] * h_0(i, alpha, x)
    for i in range(n):
        result += f_prime[i] * h_1(i, alpha, x)
    return result


def get_inputs():
    x = input("Enter the x points: (seperate them by space) \n")
    x = list(map(lambda x: float(x.strip()), x.split()))

    f = input("Enter the f(x) values: (seperate them by space) \n")
    f = list(map(lambda x: float(x.strip()), f.split()))

    f_prime = input("Enter the f'(x) values: (seperate them by space) \n")
    f_prime = list(map(lambda x: float(x.strip()), f_prime.split()))

    alpha = input("Enter the alpha value: ")
    alpha = float(alpha.strip())

    if len(x) != len(f) and len(x) != len(f_prime):
        print("x, f(x) and f'(x) should have the same length")
        exit()
    return x, f, f_prime, alpha


def integrate(x, f):
    h = abs(x[0] - x[-1]) / (len(x) - 1)
    result = 0
    for i in range(len(x) - 1):
        result += f[i] + f[i + 1]
    result *= h / 2
    return result


def main(x, f, f_prime, alpha):
    print(f"H({alpha}) = {H(alpha, x, f, f_prime)}")
    print(f"Integral of f(x) from {x[0]} to {x[-1]} is {integrate(x, f)}")
    i = int(input("Enter the i : "))
    h = abs(x[0] - x[-1]) / (len(x) - 1)
    integral = h / 2 * (f[i] + f[i + 1])
    print(f"Integral of f(x) from {x[i]} to {x[i + 1]} is {integral}")


try:
    main(*get_inputs())
except KeyboardInterrupt:
    print()
