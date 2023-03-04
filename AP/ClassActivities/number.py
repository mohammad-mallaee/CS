def is_number(s):
    print(s[:-1])
    if s[0] == '+' or s[0] == '-':
        s = s[1:]
    point_index = s.find('.')
    return s[:point_index].isdigit() and s[point_index + 1:].isdigit()


def count_digits(s):
    sum = 0
    for char in s:
        if char.isdigit():
            sum += int(char)
    return sum


def replace_not_digits(s):
    s1 = ''
    for char in s:
        if not char.isdigit():
            char = "#"
        s1 += char
    return s1


def change_upper_lower(s):
    upper_counts = 0
    lower_counts = 0
    for ch in s:
        if ch.isupper():
            upper_counts += 1
        elif ch.islower():
            lower_counts += 1
    if upper_counts > lower_counts:
        return s.upper()
    else:
        return s.lower()


def is_palindrome(s):
    return s[::-1] == s
