import math

number = 600851475143
biggest_prime_multiple = 0
first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


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


for prime in reversed(first_primes):
    if number % prime == 0:
        biggest_prime_multiple = prime
        break

root = int(math.sqrt(number))
for i in range(root, 97, -1):
    if number % i == 0:
        if is_prime(i):
            biggest_prime_multiple = i
            break

print(biggest_prime_multiple)
