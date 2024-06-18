import math
import random
from time import time

MAX_TIME = 30


def get_tour_length(G, tour):
    length = 0
    for i in range(len(tour) - 1):
        length += G[tour[i]][tour[i + 1]]
    return length


def validate_tour(G, tour):
    for i in range(len(tour) - 1):
        if G[tour[i]][tour[i + 1]] == 0:
            return False
    return True


def nearest_neighbor(G, v=0):
    visited = [v]
    for _ in range(len(G) - 1):
        row = G[visited[-1]]
        min = (-1, math.inf)
        for j in range(len(G)):
            if 0 < row[j] < min[1] and j not in visited:
                min = (j, row[j])
        if min[0] == -1:
            return None
        visited.append(min[0])

    if G[visited[-1]][v] == 0:
        return None

    return visited + [v]


def two_opt(G, T):
    last_tour_length = get_tour_length(G, T)
    start = time()
    while True:
        tour_length = last_tour_length
        for i in range(len(T) - 2):
            for j in range(i + 2, len(T) - 1):
                new_tour = T[: i + 1] + [T[j]] + T[i + 2 : j] + [T[i + 1]] + T[j + 1 :]
                new_tour_length = get_tour_length(G, new_tour)
                if new_tour_length < tour_length and validate_tour(G, new_tour):
                    T = new_tour
                    tour_length = new_tour_length
                if time() - start > MAX_TIME:
                    return T
        if tour_length == last_tour_length:
            return T
        last_tour_length = tour_length


def test():
    sizes = [5, 10, 20, 30, 50, 100, 200, 300, 500, 1000]
    for size in sizes:
        g = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(i):
                if i != j:
                    g[i][j] = random.randint(10, 100)
                    g[j][i] = g[i][j]

        start = time()
        tour = nearest_neighbor(g)
        end = time()
        print("N =", size)
        if tour is None:
            print("No Solution\n")
            continue
        print(
            "Nearest Neighbor:",
            get_tour_length(g, tour),
            "-- time:",
            round(end - start, 6),
        )
        start = time()
        tour = two_opt(g, tour)
        end = time()
        print("TWO_OPT:", get_tour_length(g, tour), "-- time:", round(end - start, 6))
        print()


test()


# A = [
#     [0, 4, 8, 9, 12],
#     [4, 0, 6, 8, 9],
#     [8, 6, 0, 10, 11],
#     [9, 8, 10, 0, 7],
#     [12, 9, 11, 7, 0],
# ]

# B = [
#     [0, 2, 3, 3, 8, 7],
#     [2, 0, 3, 8, 6, 8],
#     [3, 8, 0, 4, 3, 6],
#     [3, 2, 4, 0, 3, 2],
#     [8, 6, 3, 3, 0, 5],
#     [7, 8, 6, 2, 5, 0],
# ]

# C = [
#     [0, 2, 3, 5, 8, 4, 0],
#     [2, 0, 7, 0, 0, 3, 0],
#     [3, 1, 0, 5, 0, 6, 3],
#     [5, 0, 5, 0, 3, 5, 7],
#     [8, 0, 0, 3, 0, 0, 8],
#     [4, 3, 6, 5, 0, 0, 3],
#     [0, 0, 3, 7, 8, 3, 0],
# ]

# D = [
#     [0, 2, 3, 5, 8, 9],
#     [1, 0, 2, 4, 6, 8],
#     [3, 2, 0, 4, 5, 6],
#     [5, 3, 1, 0, 2, 3],
#     [8, 7, 4, 2, 0, 1],
#     [9, 8, 6, 4, 2, 0],
# ]

# graphs = [A]

# for g in graphs:
#     tour = nearest_neighbor(g)
#     if tour is None:
#         print("No Solution\n")
#         continue
#     print(tour, get_tour_length(g, tour))
#     tour = two_opt(g, tour)
#     print(tour, get_tour_length(g, tour))
#     print()
