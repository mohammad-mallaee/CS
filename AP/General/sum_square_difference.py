# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numbers_count = 100
sum_of_squares = 0
square_of_sums = ((numbers_count + 1) / 2 * numbers_count) ** 2

for i in range(1, numbers_count + 1):
    sum_of_squares += (i ** 2)

print(square_of_sums - sum_of_squares)
