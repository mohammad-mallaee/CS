def print_nums(n, i=1):
    if i < n:
        print(i, end="")
        print_nums(n, i + 1)
    print(i, end="")


def print_row(n, i):
    print(" " * (n - i), end="")
    print_nums(i)
    print()


def print_rows(n, i=1):
    if i < n:
        print_row(n, i)
        print_rows(n, i + 1)
    print_row(n, i)


print_rows(int(float(input())))
