def get_data_structure(list):
    list_size = len(list)
    Matrix = [[0] * list_size for _ in range(list_size)]
    for i in range(0, len(list)):
        for j in range(i + 1):
            min_ij = get_min(list, j, i)
            Matrix[j][i] = min_ij
            Matrix[i][j] = min_ij
    return Matrix


def get_min(list, start, end):
    min = list[start]
    for k in range(start, end + 1):
        min = list[k] if list[k] < min else min
    return min


for a in get_data_structure([1, 8, 9, 2, 3]):
    print(a)
