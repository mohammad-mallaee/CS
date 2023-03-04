import math


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def compare(d_class, d_dorm, e):
    return "Class" if d_class * e <= d_dorm else "Dorm"


x_start = float(input())
y_start = float(input())

x_class = float(input())
y_class = float(input())

x_dorm = float(input())
y_dorm = float(input())

e = float(input())

class_distance = distance(x_start, y_start, x_class, y_class)
dorm_distance = distance(x_start, y_start, x_dorm, y_dorm)

print(compare(class_distance, dorm_distance, e))
