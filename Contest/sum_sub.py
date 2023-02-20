n = int(input())
answers = []
for i in range(0, n):
    numbers = input().split(" ")
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    if first_number == second_number:
        answers.append(0)
    elif first_number < second_number:
        if first_number % 2 == second_number % 2:
            answers.append(2)
        else:
            answers.append(1)
    elif first_number > second_number:
        if first_number % 2 == second_number % 2:
            answers.append(1)
        else:
            answers.append(2)

for answer in answers:
    print(answer)
