def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("first number: "))
b = int(input("second number: "))
print("gcd:", gcd(a, b))