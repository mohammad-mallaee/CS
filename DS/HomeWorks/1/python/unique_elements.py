import copy
a = [1, 2, 6, 3, 5, 4, 7]


def sort(A, low, high):
    if low < high:
        if A[low] % 2 == 1:
            A[high - 1], A[low] = A[low], A[high - 1]
            sort(A, low, high - 1)
        else:
            sort(A, low + 1, high)


# sort(a, 0, len(a))
# print(a)

c_count = 0


def unique_elements(li):
    global c_count
    n = len(li)
    c_count += 1
    if n == 1:
        return True
    elif not unique_elements(copy.deepcopy(li[0 : n - 1])):
        return False
    elif not unique_elements(copy.deepcopy(li[1:n])):
        return False
    else:
        return li[0] != li[len(li) - 1]


def unique_elements2(li):
    global c_count
    n = len(li)
    c_count += 1
    if n == 1:
        return True
    elif li[0] in li[1:]:
        return False
    else:
        return unique_elements2(li[1:])


print(unique_elements2([2, 3, 4, 5, 6]))
print(c_count)
