n = int(input())
p1 = 0
p2 = 1
p3 = 1
number = 0
if n > 0 & n < 3:
    number = 1

for i in range(3, n + 1):
    number = p1 + p2 + p3
    p1 = p2
    p2 = p3
    p3 = number
print(number)
