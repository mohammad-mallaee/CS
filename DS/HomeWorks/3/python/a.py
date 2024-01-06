l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [30, 20, 11, 10, 9, 8]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7]
l4 = [1, 5, 3, 2, 1]


def find_biggest(numbers: list) -> int:
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if middle == 0:
            return max(numbers[middle], numbers[middle + 1])
        elif middle == len(numbers) - 1:
            return max(numbers[middle - 1], numbers[middle])
        if numbers[middle - 1] < numbers[middle] > numbers[middle + 1]:
            return numbers[middle]
        elif numbers[middle - 1] < numbers[middle] < numbers[middle + 1]:
            left = middle + 1
        elif numbers[middle - 1] > numbers[middle] > numbers[middle + 1]:
            right = middle - 1


from random import randint
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


def find_major(numbers: list):
    for index, number in enumerate(numbers):
        count = 1
        for j in numbers:
            if number == j:
                count += 1
        if count >= len(numbers) // 2:
            return index, number
    return -1

major = [1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,5,5,5,6,6,7,65,3,3,3,3,1,4,4,4,4,4,4,5,5,5,5,5]
print(find_major(major))