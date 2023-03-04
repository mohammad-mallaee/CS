import time

n = 1000
a, b, c = 1, 2, n - 3
start = time.time()
while a < b < c:
    if a * a + b * b == c * c:
        print(a, b, c)
    b += 1
    c = n - a - b
    if b == c or b == c - 1:
        a += 1
        b = a + 1
        c = n - a - b
    if b == c - 1:
        if a * a + b * b == c * c:
            print(a, b, c)

print(time.time() - start)
