l1 = [1,2,3,4,5,6,7,8,9]
l2 = [30,20,11,10,9,8]
l3 = [1,2,3,4,5,6,7,8,9,8,7]
l4 = [1, 5, 3, 2, 1]

def find_biggest(numbers: list) -> int:
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = (left+right)//2
        if middle == 0:
            return max(numbers[middle], numbers[middle + 1])
        elif middle == len(numbers) - 1:
            return max(numbers[middle - 1], numbers[middle])
        if (numbers[middle - 1] < numbers[middle] > numbers[middle + 1]):
            return numbers[middle]
        elif numbers[middle - 1] < numbers[middle] < numbers[middle + 1]:
            left = middle + 1
        elif numbers[middle - 1] > numbers[middle] > numbers[middle + 1]:
            right = middle - 1


print(find_biggest(l1))
