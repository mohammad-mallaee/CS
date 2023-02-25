import random

print("ROCK, PAPER, SCISSORS")
wins, losses, ties = 0, 0, 0


def print_stats():
    print(wins, "Wins,", losses, "Losses,", ties, "Ties")


def get_move():
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uite. Type one : ")
    move = input()
    if move == "r":
        return "ROCK"
    elif move == "p":
        return "PAPER"
    elif move == "s":
        return "SCISSORS"
    elif move == "q":
        return "QUIT"
    else:
        print("Type one of r, p, s, or q")
        return get_move()


def make_random_move():
    random_num = random.randint(1, 3)
    if random_num == 1:
        return "ROCK"
    elif random_num == 2:
        return "PAPER"
    elif random_num == 3:
        return "SCISSORS"


def is_winning(user_move, pc_move):
    if user_move == pc_move:
        return 0

    if user_move == "ROCK":
        if pc_move == "SCISSORS":
            return 1
        elif pc_move == "PAPER":
            return -1
    if user_move == "SCISSORS":
        if pc_move == "PAPER":
            return 1
        elif pc_move == "ROCK":
            return -1
    if user_move == "PAPER":
        if pc_move == "ROCK":
            return 1
        elif pc_move == "SCISSORS":
            return -1


while True:
    user_move = get_move()
    if user_move == "QUIT":
        break

    random_move = make_random_move()
    print(user_move, "versus ...")
    print(random_move)

    winning = is_winning(user_move, random_move)
    if winning == 1:
        wins += 1
        print("You win!")
    elif winning == -1:
        losses += 1
        print("You loss!")
    elif winning == 0:
        ties += 1
        print("It's a tie.")

    print_stats()
