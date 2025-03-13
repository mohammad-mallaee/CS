import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

n = 10001


def is_prime(num):
    if num == 1 | num == 0:
        return False
    if num % 2 == 0:
        return False
    r = int(math.sqrt(num))
    for j in range(3, r + 1, 2):
        if num % j == 0:
            return False
    return True


primeCounter = 1
number = 1
while primeCounter < n:
    number += 2
    if is_prime(number):
        print(number)
        primeCounter += 1

print(number)
