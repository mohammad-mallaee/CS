a = [1, 2, 1, 2]

def find_majority(arr, n):
    candidate = 0
    votes = 0

    for i in range(len):
        if votes == 0:
            candidate = arr[i]
            votes = 1
        else:
            if arr[i] == candidate:
                votes += 1
            else:
                votes -= 1
    count = 0