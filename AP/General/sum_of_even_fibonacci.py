# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

previous_1 = 1
previous_2 = 1
num = previous_1 + previous_2
summation = 2
while num < 4000000:
    previous_1 = previous_2
    previous_2 = num
    num = previous_1 + previous_2
    if num % 2 == 0:
        summation += num

print(summation)
