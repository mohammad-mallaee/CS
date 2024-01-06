v1 = [5, 8, 4, 2]


def add_vectors(v1, v2, coefficient=1):
    return [v1[i] + (coefficient) * v2[i] for i in range(len(v1))]


def hadamard_times_v(v):
    n = len(v)
    if n == 1:
        return v
    else:
        first_half = hadamard_times_v(v[: n // 2])
        second_half = hadamard_times_v(v[(n - 1) // 2 + 1 :])

        top = add_vectors(first_half, second_half)
        bottom = add_vectors(first_half, second_half, coefficient=-1)
        return top + bottom


print(hadamard_times_v(v1))  # The answer should be [19, -1, 7, -5]
