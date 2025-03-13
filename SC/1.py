import math

# A.
# Input: matrix A and vector b
# Problem: Find the answer of Least squares problem using Cholesky Decomposition (min ||Ax - b||)
# Output: x (answer), R, eps (error)

# B.
# Input: matrix A and vector b
# Problem: Solve the system of linear equations using QR decomposition (gram schmidt)
# Output: x (answer), Q, R


def print_matrix(A, name=""):
    matrix = [[None] * len(A[0]) for _ in range(len(A))]
    for i in range(len(A[0])):
        max_j_length = 0
        for j in range(len(A)):
            max_j_length = max(max_j_length, len(str(A[j][i])))
        for j in range(len(A)):
            matrix[j][i] = str(A[j][i]).rjust(max_j_length)
    w = len("[ " + "  ".join(matrix[0]) + " ]")
    print(f"{name:^{w}}")
    for i in range(0, len(matrix)):
        print("[ " + "  ".join(matrix[i]) + " ]")
    print()


def multiply(A, B):
    if len(B) != len(A[0]):
        raise Exception("Matrix dimensions are not compatible")

    C = []
    n = len(A)
    for i in range(n):
        row = []
        for j in range(len(B[0])):
            index = 0
            for k in range(len(B)):
                index += A[i][k] * B[k][j]
            row.append(index)
        C.append(row)
    return C


def transpose(A):
    C = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        C.append(row)
    return C


def scale(A, a):
    m, n = len(A), len(A[0]) if len(A) > 0 else 0
    B = [[A[i][j] * a for j in range(n)] for i in range(m)]
    return B


def equals(A, B, eps=0):
    if 0 == len(A) == len(B):
        return True
    if len(A) != len(B):
        return False
    if len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if abs(A[i][j] - B[i][j]) > eps:
                return False
    return True


def norm(A):
    return math.sqrt(sum([A[i][0] ** 2 for i in range(len(A))]))


def get_column(A, index):
    c = []
    for i in range(len(A)):
        c.append([A[i][index]])
    return c


def add_in_place(A, B):
    if len(A) != len(B):
        raise Exception("Matrix dimensions are not compatible")
    m, n = len(A) or 0, len(A[0]) or 0
    for i in range(m):
        for j in range(n):
            A[i][j] = A[i][j] + B[i][j]


def add(*matrices):
    m = len(matrices[0]) if len(matrices) > 0 else 0
    n = len(matrices[0][0]) if len(matrices) > 0 and len(matrices[0]) > 0 else 0
    result = [[0] * n for _ in range(m)]
    for matrix in matrices:
        add_in_place(result, matrix)
    return result


def backward_substitute(A, b):
    n = len(b)
    x = [[0] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        m = 0
        for j in range(i + 1, n):
            m += A[i][j] * x[j][0]
        x[i][0] = (b[i][0] - m) / A[i][i]
    return x


def forward_substitute(A, b):
    x = [[0] for _ in range(len(b))]
    for i in range(len(b)):
        m = 0
        for j in range(i):
            m += A[i][j] * x[j][0]
        x[i][0] = (b[i][0] - m) / A[i][i]
    return x


def cholesky(A):
    n = len(A)
    R = [[0] * len(A) for _ in range(n)]
    R_T = [[0] * len(A) for _ in range(n)]
    for i in range(n):
        if A[i][i] < 0:
            raise Exception("Matrix is not positive definite")
        R[i][i] = math.sqrt(A[i][i] - sum(R[j][i] ** 2 for j in range(i)))
        R_T[i][i] = R[i][i]
        for k in range(i + 1, n):
            R[i][k] = (A[i][k] - sum(R[j][i] * R[j][k] for j in range(i))) / R[i][i]
            R_T[k][i] = R[i][k]
    return R, R_T


def gram_schmidt(A):
    m, n = len(A), len(A[0])
    A_columns = [get_column(A, i) for i in range(n)]
    R = [[0] * n for _ in range(m)]
    R[0][0] = norm(A_columns[0])
    Q_columns = [scale(A_columns[0], 1 / R[0][0])]
    Q = [[0] * n for _ in range(m)]

    for k in range(1, n):
        for i in range(k):
            R[i][k] = multiply(transpose(Q_columns[i]), A_columns[k])[0][0]
        qh_k = add(*[scale(Q_columns[i], R[i][k]) for i in range(k)])
        qh_k = add(A_columns[k], scale(qh_k, -1))
        R[k][k] = norm(qh_k)
        Q_columns.append(scale(qh_k, 1 / R[k][k]))

    for k in range(n):
        for j in range(m):
            Q[j][k] = Q_columns[k][j][0]

    return Q, R


def least_squares(A, b):
    At = transpose(A)
    b_ = multiply(At, b)
    AtA = multiply(At, A)
    R, R_T = cholesky(AtA)
    y = forward_substitute(R_T, b_)
    x = backward_substitute(R, y)
    Ax = multiply(A, x)
    eps = add(b, scale(Ax, -1))
    return x, R, eps


def qr_equations_system(A, b):
    Q, R = gram_schmidt(A)
    Qt = transpose(Q)
    Qtb = multiply(Qt, b)
    x = backward_substitute(R, Qtb)
    return x, Q, R


def least_squares_program():
    print("\n-- Least Squares Problem --")
    dimesions = input("Enter the Matrix dimensions (seperated by space): ")
    m, n = list(map(lambda d: int(d.strip()), dimesions.split()))
    print(f"Matrix dimensions: rows = {m}, columns = {n}")
    A = []
    print("Enter each row in a line (seperated by space) : ")
    for _ in range(m):
        row = list(map(lambda x: float(x.strip()), input().split()))
        if len(row) != n:
            print(f"Each row should have {n} element(s)!!")
            exit()
        A.append(row)
    print()
    print_matrix(A, "Matrix A")
    vector = input("Enter the vector (seperated by space, in one line):\n")
    b = []
    for element in map(lambda x: float(x.strip()), vector.split()):
        b.append([element])
    if len(b) != m:
        print(f"Vector should have {m} elements")
        return
    print()
    print_matrix(b, "Vector b")
    x, R, eps = least_squares(A, b)
    print("-" * 40)
    print_matrix(x, "Answer")
    print_matrix(R, "Matrix R")
    print_matrix(eps, f"Error Vector (size = {norm(eps)})")


def qr_program():
    print("\n-- QR decomposition --")
    n = int(input("Enter matrix dimension: "))
    A = []
    print("Enter each row in a line (seperated by space) : ")
    for _ in range(n):
        row = list(map(lambda x: float(x.strip()), input().split()))
        if len(row) != n:
            print(f"Each row should have {n} element(s)!!")
            exit()
        A.append(row)
    print()
    print_matrix(A, "Matrix A")
    vector = input("Enter the vector (seperated by space, in one line):\n")
    b = []
    for element in map(lambda x: float(x.strip()), vector.split()):
        b.append([element])
    if len(b) != n:
        print(f"Vector should have {n} elements")
        return
    print()
    print_matrix(b, "Vector b")
    x, Q, R = qr_equations_system(A, b)
    Ax = multiply(A, x)
    print("-" * 40)
    if not equals(Ax, b, 10 ** (-12)):
        print(">> No Solution Exists !!\n")
    else:
        print_matrix(x, "Answer")
    print_matrix(Q, "Matrix Q")
    print_matrix(R, "Matrix R")


if __name__ == "__main__":
    print("-" * 40)
    c = int(
        input(
            "1. Least Squares (Cholesky)    2. Linear Equations System (QR) \nChoose a program: "
        )
    )
    if c == 1:
        least_squares_program()
    elif c == 2:
        qr_program()
    else:
        print("Invalid number")
