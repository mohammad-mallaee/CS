import math

number = 1
upper_bound = 10 + 1
factors = []

for i in range(1, upper_bound):
    factors.append(i)

for i in range(2, upper_bound):
    for j in range(i + 1, math.ceil(upper_bound / i)):
        multiple_index = i * j - 1
        if factors[j - 1] != 1:
            factors[multiple_index] = 1
    if i * i < upper_bound:
        factors[i - 1] = 1

summation = 1
for i in factors:
    summation *= i
print(summation)
