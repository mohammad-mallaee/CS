n = int(input())
numbers_str = input().split(" ")
numbers = []
for num_str in numbers_str:
    numbers.append(int(num_str))

numbers.sort()
summation = 0
for i in range(0, 2 * n, 2):
    summation += numbers[i]
print(summation)
