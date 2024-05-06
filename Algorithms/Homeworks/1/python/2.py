def T(n):
    if n == 1:
        return 0
    else:
        return n + max([T(k) + T(n - k) for k in range(1, n)])


num = int(input("enter your number: "))
print(f"answer of recursive approach is {T(num)}")
print(f"answer of direct approach is {sum([i for i in range(2, num + 1)])}")