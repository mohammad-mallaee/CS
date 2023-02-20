n = int(input())
numbers = input().split(" ")
last_digit = int(numbers[0])
moves = 0
for i in range(1, len(numbers)):
    number = int(numbers[i])
    if number <= last_digit:
        new_moves = last_digit - number + 1
        moves += new_moves
        last_digit = number + new_moves
    else:
        last_digit = number
print(moves)
