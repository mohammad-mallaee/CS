import math

inf_list = [i for i in range(5, 300, 3)]
inf_list += [math.inf for _ in range(100000)]

def find_k(numbers: list, k: int) -> int:
    left = 1
    right = len(numbers) - 1
    while numbers[left] < k:
        left *= 2
    right = left
    left //= 2

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == k:
            return middle
        elif numbers[middle] < k:
            left = middle + 1
        else:
            right = middle - 1
        
    return -1


print(find_k(inf_list, 101))
