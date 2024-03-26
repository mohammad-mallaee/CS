def grid_ways(m, n):
    if m == 1 or n == 1:
        return 1

    return grid_ways(m - 1, n) + grid_ways(m, n - 1)


def grid_ways_2(m, n):
    memo = {}
    for i in range(1, m + 1):
        memo[(i, 1)] = 1
    for j in range(1, n + 1):
        memo[(1, j)] = 1

    for i in range(2, m + 1):
        for j in range(2, n + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]

    return memo[(m, n)]


print(grid_ways_2(75, 19))
