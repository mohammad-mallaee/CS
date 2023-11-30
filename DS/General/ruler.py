def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        print("-" * center_length)
        draw_interval(center_length - 1)


def draw_ruler(m, n):
    print(m * "-" + " 0")
    for i in range(n):
        draw_interval(m)
        print(m * "-" + f" {i + 1}")


draw_ruler(int(input()), int(input()))
