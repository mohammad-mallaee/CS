import random
import time


def better_forward_eliminate(matrix):
    n = len(matrix)
    for i in range(n):
        full_pivot(matrix, i)
        for j in range(i + 1, n):
            if matrix[i][i] == 0:
                return
            co_effiecent = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= co_effiecent * matrix[i][k]


def full_pivot(matrix, k):
    n = len(matrix)
    max_position = (k, k)
    max_value = matrix[k][k]
    for i in range(k, n):
        for j in range(k, n):
            if abs(matrix[i][j]) > max_value:
                max_position = (i, j)
                max_value = abs(matrix[i][j])
    row, column = max_position
    for p in range(k, n + 1):
        matrix[k][p], matrix[row][p] = matrix[row][p], matrix[k][p]
    for p in range(k, n):
        matrix[p][k], matrix[p][column] = matrix[p][column], matrix[p][k]


def backward_substitute(matrix):
    n = len(matrix)
    infinit_solutions = False
    for i in range(n):
        if all(matrix[i][j] == 0 for j in range(0, n - 1)):
            if matrix[i][n] == 0:
                return "No Solution"
            else:
                infinit_solutions = True
    if infinit_solutions:
        return "Infinite Solutions"
    x = [0] * len(matrix)
    for i in range(n - 1, -1, -1):
        m = 0
        for j in range(i + 1, n):
            m += matrix[i][j] * x[j]
        x[i] = (matrix[i][n] - m) / matrix[i][i]
    return x


def augment_matrix(A, b):
    for i in range(len(A)):
        A[i].append(b[i])


def print_matrix(A):
    for i in range(len(A)):
        print(A[i])


def test():
    for i in range(20, 300, 20):
        start = time.time()
        for _ in range(5):
            A = [[random.randint(0, 20) for _ in range(i)] for _ in range(i)]
            b = [random.randint(0, 20) for _ in range(i)]
            augment_matrix(A, b)
            better_forward_eliminate(A)
            backward_substitute(A)
        end = time.time()
        print(f"n = {i}, execution: {round((end - start) / 5, 8)}")


test()
