from time import time


def generate_string(alphabet, length, forbidden, prefix=""):
    if length == 0:
        return [""]
    else:
        result = []
        for char in alphabet:
            new_prefix = prefix + char
            if not any(str in new_prefix for str in forbidden):
                for string in generate_string(
                    alphabet, length - 1, forbidden, new_prefix
                ):
                    result.append(char + string)
        return result


def test():
    alphabets = ["01", "01", "abc", "abc", "123456", "abcdefghijklmnopqrstuvwxyz"]
    lengths = [5, 20, 5, 25, 12, 5]
    forbiddens = [
        ["001", "11"],
        ["0101", "1100"],
        ["aa", "acb", "abcabc", "b"],
        ["aabb", "b", "ccaa"],
        ["1", "2", "3", "45"],
        ["hello", "ae", "ua", "akw"],
    ]

    for i in range(len(alphabets)):
        print(f"alphabet = {alphabets[i]},", f"length = {lengths[i]}")
        print("forbidden =", forbiddens[i])
        start = time()
        strings = generate_string(alphabets[i], lengths[i], forbiddens[i])
        print("Generated", len(strings), "strings")
        if len(strings) < 15:
            print("strings =", strings)
        print(round(time() - start, 6), "seconds")
        print()

test()