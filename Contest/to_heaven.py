n = int(input())
ways = 0


def factorial(n):
    answer = 1
    for j in range(1, n + 1):
        answer *= j
    return answer


for i in range(n // 2, -1, -1):
    ones = n - (2 * i)
    ways += factorial(i + ones) / (factorial(i) * factorial(ones))

print(int(ways))
