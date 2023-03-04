courses_counts = int(input())
grades = 0
credits = 0
for i in range(courses_counts):
    grade = int(input())
    credit = int(input())
    credits += credit
    grades += grade * credit

print(int(grades / credits))
