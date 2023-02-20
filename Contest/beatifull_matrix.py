rows = {}
i_index = -1
j_index = -1
for i in range(0, 5):
    rows[i] = input().replace(" ", "")
    for j in range(0, len(rows[i])):
        if rows[i][j] == "1":
            i_index = i
            j_index = j
            break

print(abs(i_index - 2) + abs(j_index - 2))
