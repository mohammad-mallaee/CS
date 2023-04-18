import re
# import math
import math
import time

# print("Hello, World!!")
# name = input("Enter your name : ")
# print(f"Your name has {len(name)} characters")

# (a, b, c) = map(float, input("Enter triangle sides : ").split())
# if a + b <= c or a + c <= c or b + c <= c:
#     print("This is not a triangle")
# else:
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     print(f"The area of the triangle is {area}")

# summation, count, minimum, maximum = 0, 0, math.inf, -math.inf
# while (num := int(input())) != 0:
#     summation += num
#     count += 1
#     minimum = num if num < minimum else minimum
#     maximum = num if num > maximum else maximum
#
# average = summation / (count - 1 if count > 1 else 1)
# print(f"maximum: {maximum}, minimum: {minimum},"
#       f" sum: {summation} average: {average}")

# count = 0
# while (n := int(input())) != -99:
#     first_digit = int(str(n)[0])
#     length = len(str(n))
#     if length == 1 or n / first_digit == (10 ** length - 1) / 9:
#         count += 1
#
# print(f"There was {count} palindrome(s)")

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end="\t")
#     print()

# def reverse(n):
#     if n < 10: return n
#     return str(n % 10) + str(reverse(n // 10))

# my_list = ["amir", "ali", "amir", "ali", "hasan", "abbas", "ali"]
# for item in my_list:
#     count = my_list.count(item)
#     for _ in range(count - 1): my_list.remove(item)
#
# print(" ".join(my_list))


s = "fmanso2ori@gmail.com,f_mansoori@ut.ac.fdh.ir,fmansoori@gmail..com"
print(re.findall(r"\w+@(?:[a-zA-Z][a-zA-Z0-9]*\.)+[a-zA-Z]{2,3}", s))
