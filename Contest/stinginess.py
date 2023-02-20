inputs = input().split(" ")
n = int(inputs[0])
m = int(inputs[1])
a = int(inputs[2])
b = int(inputs[3])

if b / m < a:
    m_prices = (n // m) * b
    r_prices = (n - (m * (n // m))) * a
    print(m_prices + r_prices)
else:
    print(n * a)
