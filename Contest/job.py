n = int(input())
salaries = list(map(int, input().split()))
longest_sequence = 0
sequence = 1
for i in range(1, len(salaries)):
    if salaries[i] >= salaries[i - 1]:
        sequence += 1
        if sequence > longest_sequence:
            longest_sequence = sequence
    else:
        sequence = 1
print(longest_sequence)
