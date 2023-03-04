def move(n, source, target, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(get_bar(source), "->", get_bar(target))

        # Move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)


# Initiate call from source A to target C with auxiliary B

def get_bar(bar):
    if bar == A:
        return "A"
    elif bar == B:
        return "B"
    elif bar == C:
        return "C"


n = int(input())
A = []
B = []
C = []
for i in range(n, 0, -1):
    A.append(i)
print("It will be done in", 2 ** n - 1, "moves")
move(n, A, C, B)
