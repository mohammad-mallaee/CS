def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def super_gcd(a):
    if len(a) == 2:
        return gcd(a[0], a[1])
    else:
        return gcd(a[0], super_gcd(a[1:]))


def f(text, pattern):
    j = 0
    for i in range(len(text)):
        if text[i] == pattern[j]:
            j += 1
        else:
            j = 0
        if j == len(pattern):
            return i - j + 1
    return -1

print(f("hello how are you", 'how'))