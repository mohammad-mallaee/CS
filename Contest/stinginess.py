inputs = input().split(" ")
n = int(inputs[0])
m = int(inputs[1])
a = int(inputs[2])
b = int(inputs[3])

if b / m < a:
    b_count = n // m
    a_count = n - (b_count * m)
    price = b_count * b
    price += a_count * a if a_count * a < b else b
    print(price)
else:
    print(n * a)
