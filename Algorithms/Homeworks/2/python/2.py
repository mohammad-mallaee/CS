def max_value(list, start, end):
    if start == end:
        return list[start]
    coin_values = sum(list[start : end + 1])
    return coin_values - min(
        max_value(list, start + 1, end),
        max_value(list, start, end - 1),
    )


def coin_values_table(A: list):
    D = [[0] * len(A) for i in range(len(A))]
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(A)):
            if i > j:
                D[i][j] = 0
            elif i == j:
                D[i][j] = A[i]
            else:
                s = sum(A[i : j + 1])
                D[i][j] = s - min(D[i + 1][j], D[i][j - 1])
    return D


def get_moves(A, D):
    moves = []
    domain = (0, len(A) - 1)
    for _ in range(len(A)):
        first_coin = D[domain[0] + 1][domain[1]]
        last_coin = D[domain[0]][domain[1] - 1]
        if first_coin < last_coin:
            moves.append(A[domain[0]])
            domain = (domain[0] + 1, domain[1])
        else:
            moves.append(A[domain[1]])
            domain = (domain[0], domain[1] - 1)
    first_player = [moves[i] for i in range(0, len(moves), 2)]
    second_player = [moves[i] for i in range(1, len(moves), 2)]
    return sum(first_player), first_player, second_player


A = [2, 5, 8, 6, 9, 2, 10, 5, 7, 4]
table = coin_values_table(A)
print(get_moves(A, table))
# print(max_value(A, 0, len(A)-1))
