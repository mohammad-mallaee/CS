import time
import random
from itertools import chain, combinations


def find_most_valuable_subset(elements, W):
    p = [[]]
    subset = []
    subset_value = 0
    for element in elements:
        for i in range(len(p)):
            new_subset = p[i] + [element]
            p.append(new_subset)

            if sum([x[1] for x in new_subset]) <= W:
                new_subset_value = sum([x[0] for x in new_subset])
                if new_subset_value > subset_value:
                    subset_value = new_subset_value
                    subset = new_subset

    return subset, subset_value


def powerset(elements: list):
    p = [[]]
    for element in elements:
        for i in range(len(p)):
            p.append(p[i] + [element])
    return p

def faster_powerset(elements):
    s = list(elements)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def faster_most_valuable_subset(elements, W):
    best_subset = []
    best_subset_value = 0
    for subset in faster_powerset(elements):
        if sum([x[1] for x in subset]) <= W:
            subset_value = sum([x[0] for x in subset])
            if subset_value > best_subset_value:
                best_subset_value = subset_value
                best_subset = subset
    return best_subset, best_subset_value


n = 26
W = 150

# elements will be in paris of (value, weight)
elements = [(random.randint(10, 100), random.randint(10, 100)) for _ in range(n)]
print(f"elements: \n{elements}")
start = time.time()
subset, subset_value = faster_most_valuable_subset(elements, W)
print(f"most valuable subset: {subset}\nsubset value: {subset_value}")
end = time.time()
print("execution time:", end - start)
