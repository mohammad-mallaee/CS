import math
import random


def is_prime(num):
    if num == 1 or num == 0: return False
    if num % 2 == 0: return False
    root = int(math.sqrt(num)) + 1
    for i in range(3, root, 2):
        if num % i == 0:
            return False
    return True


def is_relative_prime(num1, num2):
    return False if math.gcd(num1, num2) == 1 else True


def pick_exponent(phi):
    random.seed(17)
    i = random.randint(2, phi - 1)
    while not is_relative_prime(phi, i):
        i = random.randint(2, phi - 1)
    return i


def public_key(e, q, p):
    n = p * q
    return e, n


def private_key(e, q, p):
    phi = (p - 1) * (q - 1)
    random.seed(17)
    k = random.randint(2, phi - 1)
    d = math.floor(((k * phi) + 1) / e)
    e, n = public_key(e, q, p)
    return d, n


p = int(input())
q = int(input())

if is_prime(p) is False or is_prime(q) is False:
    print(False)
else:
    phi = (p - 1) * (q - 1)
    e = pick_exponent(phi)
    e, n = public_key(e, q, p)
    print(n, e)
    d, n = private_key(e, q, p)
    print(n, d)
