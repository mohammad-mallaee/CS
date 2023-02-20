n = int(input())
answers = []


def is_passable(path):
    keys = []
    for item in path:
        if item.islower():
            keys.append(item)
        elif item.lower() not in keys:
            return "NO"
    return "YES"


for i in range(0, n):
    answers.append(is_passable(input()))
for answer in answers:
    print(answer)
