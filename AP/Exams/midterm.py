import random
import re

board = {'tl': ' ', 'tm': ' ', 'tr': ' ',
         'ml': ' ', 'mm': ' ', 'mr': ' ',
         'll': ' ', 'lm': ' ', 'lr': ' '}


def print_board():
    print()
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])


'''
this a generator that each time called return the inputs in one line of the file
the output is (username,address) 
'''


def file_reader(file_name):
    with open(file_name, "r") as file:
        while True:
            line = file.readline()
            if line == "":
                break
            else:
                yield line


def save_user(username, address):
    with open("user.txt", "a+") as f:
        f.write("\n" + username + "-" + address)


def validate_address(address):
    pattern = r"([\dA-F]{4}:){5}[\dA-F]{4}"
    return re.match(pattern, address) is not None


def validate_username(username):
    for line in file_reader("user.txt"):
        if len(line.split("-")) != 2:
            continue
        saved_username = line.split("-")[0]
        if saved_username == username:
            return False

    return True


def get_user_inputs():
    while True:
        print("Enter your username and address:")
        username, address = input().split()
        if not validate_address(address):
            print("Your address is in wrong format. Please try again")
            continue
        if not validate_username(username):
            print("This username is already used. Try another one")
            continue
        save_user(username, address)
        return username, address


def choose_random_place():
    empty_places = [key for key in board if board[key] == " "]
    random_index = random.randint(0, len(empty_places) - 1)
    return empty_places[random_index]


def get_choice(turn):
    if turn == "X":
        print_board()
        while True:
            place = input("\nChoose a place: ")
            if place not in board:
                print("Incorrect Input. Try again")
                continue
            if board[place] != " ":
                print("This place is already taken. Try another one.")
                continue
            return place
    elif turn == "O":
        random_place = choose_random_place()
        print("Computer's turn:", random_place)
        return random_place


def choose_first_turn():
    random_num = random.randint(1, 2)
    return "X" if random_num == 1 else "O"


def who_win():
    if board["tl"] != " " and board["tl"] == board["tm"] == board["tr"]:
        return board["tl"]
    if board["ml"] != " " and board["ml"] == board["mm"] == board["mr"]:
        return board["ml"]
    if board["ll"] != " " and board["ll"] == board["mm"] == board["lr"]:
        return board["ll"]
    if board["tl"] != " " and board["tl"] == board["mm"] == board["lr"]:
        return board["tl"]
    if board["tr"] != " " and board["tr"] == board["mm"] == board["ll"]:
        return board["tr"]
    if board["tl"] != " " and board["tl"] == board["ml"] == board["ll"]:
        return board["ll"]
    if board["tm"] != " " and board["tm"] == board["mm"] == board["lm"]:
        return board["tl"]
    if board["tr"] != " " and board["tr"] == board["mr"] == board["lr"]:
        return board["tr"]
    return None


def print_ending(winner):
    if winner == "X":
        print("\nYou Won!!\n")
    elif winner == "O":
        print("\nYou lost the game.\n")
    elif winner is None:
        print("\nYou ran over turns and the game is a tie\n")


def confirm():
    while True:
        confirmation = input("Do you want to start a new game (y/n)? ")
        if confirmation.lower() == "y":
            return True
        if confirmation.lower() == "n":
            return False
        print("Incorrect input. Try again")


user, addr = get_user_inputs()
first_turn = choose_first_turn()
turn = choose_first_turn()
x_turns = 3
y_turns = 3
wins = 0

while True:
    move = get_choice(turn)
    board[move] = turn
    if turn == 'X':
        x_turns -= 1
        turn = 'O'
    else:
        y_turns -= 1
        turn = 'X'

    winner = who_win()
    game_ended = True if winner else False
    game_ended = True if x_turns == 0 and y_turns == 0 else game_ended

    if game_ended:
        print_board()
        print_ending(winner)
        if winner == "X":
            wins += 1
        print(f"You have won {wins} game(s)")
        if confirm():
            x_turns = 3
            y_turns = 3
            for key in board:
                board[key] = " "
        else:
            break
