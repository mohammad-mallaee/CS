def move(n, a, b, c):
    if n == 1:
        print(f"{a} -> {c}")
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


disks_count = int(input("Number of disks: "))
print(f"{2 ** disks_count - 1} moves required")
move(disks_count, "A", "B", "C")
