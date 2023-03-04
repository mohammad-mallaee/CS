import random

n = random.randint(1, 100)
win = False
for i in range(10):
    guessed_number = int(input())
    if guessed_number == n:
        win = True
        break
    elif guessed_number > n:
        print("It should be smaller")
    elif guessed_number < n:
        print("It should be bigger")

if win:
    print("You guessed it right.")
else:
    print("You lost the game, but you can always try again.")
