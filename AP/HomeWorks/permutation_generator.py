def permutations(iterable):
    n = len(iterable)
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    yield iterable
    while True:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield list(iterable[i] for i in indices[:n])
                break
        else:
            return


numbers = list(map(int, input().split()))
for p in permutations(numbers):
    print(p)
