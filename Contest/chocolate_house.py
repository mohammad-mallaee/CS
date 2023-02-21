inputs = input().split(" ")
n = int(inputs[0])
m = int(inputs[1])
works = input().split(" ")
moves = 0
index = 1
for work in works:
    work = int(work)
    if work > index:
        moves += work - index
    elif work < index:
        moves += (n - index + work)
    index = work
print(moves)
