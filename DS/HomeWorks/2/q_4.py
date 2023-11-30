S = [10, 14, 23, 8, 4]
F = [15, 17, 27, 12, 7]

A = []


def power_set(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in power_set(seq[1:]):
            yield [seq[0]] + item
            yield item


X = [i for i in range(5)]

for subset in power_set(X):
    subset_length = len(subset)
    if subset_length > len(A):
        iEqual = True
        for i in range(subset_length):
            jEqual = True
            for j in range(subset_length):
                x_i = subset[i]
                x_j = subset[j]
                if x_i != x_j and S[x_j] <= S[x_i] <= F[x_j]:
                    jEqual = False
                    break
            if jEqual is False:
                iEqual = False
                break
        if iEqual is True:
            A = subset


print(A)
