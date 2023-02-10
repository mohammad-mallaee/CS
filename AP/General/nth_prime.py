import math

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
