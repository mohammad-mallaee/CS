numbers_count = 100
sum_of_squares = 0
square_of_sums = ((numbers_count + 1) / 2 * numbers_count) ** 2

for i in range(1, numbers_count + 1):
    sum_of_squares += (i ** 2)

print(square_of_sums - sum_of_squares)
