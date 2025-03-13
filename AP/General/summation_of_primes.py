import time
import math

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def is_prime(num):
    if num == 1 or num == 0:
        return False
    if num % 2 == 0:
        return False
    r = int(math.sqrt(num))
    for j in range(3, r + 1, 2):
        if num % j == 0:
            return False
    return True


def get_sum(num):
    summation_of_primes = 0
    nums = [False] * num
    root = int(math.sqrt(num))
    for i in range(1, root + 1):
        print(i)
        if not nums[i]:
            for j in range(2 * i * (i + 1), num + 1, 2 * i):
                print(j)
                nums[j] = True
            print()
    for i in range(1, num + 1):
        if not nums[i]:
            summation_of_primes += i

    return summation_of_primes


def get_sum2(num):
    summation_of_primes = 2
    for i in range(3, num, 2):
        if (is_prime(i)):
            summation_of_primes += i
    return summation_of_primes


num = 10
start = time.time()
print(get_sum(num))
print(time.time() - start)
