a = int(input())
b = int(input())
x = int(input())
y = int(input())

sum = 0
for i in range(x, y):
    if i % a == 0 or i % b == 0:
        sum += i

print(sum)
