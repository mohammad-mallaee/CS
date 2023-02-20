line = input().split(" ")
print(type(line))
a = int(line[0])
b = int(line[1])
i = 1
while 3**i * a <= 2**i * b:
    i += 1

print(i)
