number = 1000
number -= 1

first_multiple = 3
second_multiple = 5
combined_multiple = first_multiple * second_multiple

upperbound_first = number - (number % first_multiple)
upperbound_second = number - (number % second_multiple)
upperbound_combined = number - (number % combined_multiple)

count_first = number // first_multiple
count_second = number // second_multiple
count_combined = number // combined_multiple

sum_first = ((upperbound_first + first_multiple) / 2) * count_first
sum_second = ((upperbound_second + second_multiple) / 2) * count_second
sum_combined = ((upperbound_combined + combined_multiple) / 2) * count_combined

summation = sum_first + sum_second - sum_combined
print(summation)
