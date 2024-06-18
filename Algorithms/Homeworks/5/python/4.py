import math


def bisection_root(fn, eps, period, max_iters=math.inf):
    a, b = period
    iterations = 0
    while iterations <= max_iters:
        iterations += 1
        x = (a + b) / 2
        if abs(x - a) <= eps:
            return x
        if (fn(x) * fn(a)) < 0:
            b = x
        else:
            a = x


def false_position_root(fn, eps, period, max_iters=math.inf):
    a, b = period
    iterations = 0
    while iterations <= max_iters:
        iterations += 1
        x = (a * fn(b) - b * fn(a)) / (fn(b) - fn(a))
        if abs(fn(x)) <= eps:
            return x
        if fn(x) * fn(a) < 0:
            b = x
        else:
            a = x
    return x


def find_point_bisection(fn, y, eps, period):
    return bisection_root(lambda x: fn(x) - y, eps, period)


def find_point_false_p(fn, y, eps, period, max_iters=math.inf):
    return false_position_root(lambda x: fn(x) - y, eps, period, max_iters)


functions = [
    lambda x: x**2 + math.log(x),
    lambda x: math.e ** (x + 2) + math.sin(x),
    lambda x: x**3 + 2 * x**2 + 2 * x + 4,
    lambda x: x**3 - x - 1,
]

y = [3, 2, 7, 1]

periods = [(0.4, 4), (-3, -0.5), (-1, 3), (-1, 2)]

answers = [1.5921429370581, -0.9629509545352, 0.7429592021663, 1.5213797068046]

for index, fn in enumerate(functions):
    print(index, "-- y:", y[index], ", period:", periods[index])
    print("bisection: ", end="")
    print(find_point_bisection(fn, y[index], 10 ** (-14), periods[index]))
    print("false position: ", end="")
    print(find_point_false_p(fn, y[index], 10 ** (-14), periods[index]))
    print("answer :", answers[index])
    print()
