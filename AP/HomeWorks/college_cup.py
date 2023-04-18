def count_goals(score):
    goals = ""
    for char in score:
        if char.isdigit():
            goals += char
    return int(goals)


def print_winner(am, cs, st):
    if am >= cs and am >= st:
        print("AM")
    elif cs > am and cs >= st:
        print("CS")
    elif st > am and st > cs:
        print("ST")


games = input().split("-")
games.extend(input().split("-"))
games.extend(input().split("-"))

st, am, cs = 0, 0, 0

for score in games:
    if "ST" in score:
        st += count_goals(score)
    elif "AM" in score:
        am += count_goals(score)
    elif "CS" in score:
        cs += count_goals(score)

print_winner(am, cs, st)
