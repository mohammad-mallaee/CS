def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m):
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            return i
    return -1


def brute_force_string_match_2(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m):
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            return i + m - 1
    return -1


def brute_force_string_match_3(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m):
        j = m - 1
        while j > 0 and pattern[j] == text[i + j]:
            j -= 1
        if j == 0:
            return i
    return -1


def brute_force_string_match_4(text, pattern):
    n = len(text)
    m = len(pattern)

    count = 0
    i = 0

    while i < n - m:
        j = m - 1
        while j > 0 and pattern[j] == text[i + j]:
            j -= 1
        if j == 0:
            i += m
            count += 1
        i += 1
    return count


t = "The package includes adaptations wowowow use with many other commonly-used packages."
p = "wow"
count = brute_force_string_match_4(t, p)
print(count)
