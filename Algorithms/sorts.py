import random
from time import time


comparisons = 0
swaps = 0

def lomuto_partition(A, left, right):
    pivot = A[left]
    s = left
    for i in range(left, right + 1):
        if A[i] < pivot:
            s += 1
            A[s], A[i] = A[i], A[s]
    A[left], A[s] = A[s], A[left]
    return s

def hoare_partition(A: list, left: int, right: int):
    pivot = A[left]
    i, j = left, right

    while i < j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        A[i], A[j] = A[j], A[i]

    A[i], A[j] = A[j], A[i]
    return j


def quick_sort(A: list, left: int, right: int):
    if left < right:
        s = hoare_partition(A, left, right)
        quick_sort(A, left, s - 1)
        quick_sort(A, s + 1, right)


def selection_sort(A: list):
    n = len(A)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]


def bubble_sort(A: list):
    global comparisons, swaps
    n = len(A)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            comparisons += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swaps += 1


def insertion_sort(A: list):
    n = len(A)
    for i in range(1, n):
        j = i
        v = A[i]
        while j > 0 and A[j - 1] > v:
            A[j] = A[j - 1]
            j -= 1
        A[j] = v


def merge(A, B, C):
    i, j = 0, 0
    k = 0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1

    if k < len(B) + len(C):
        if i < len(B):
            A[k:] = B[i:]
        else:
            A[k:] = C[j:]


def merge_sort(A: list):
    n = len(A)
    if n > 1:
        B = A[0 : n // 2].copy()
        C = A[n // 2 : n].copy()
        merge_sort(B)
        merge_sort(C)
        merge(A, B, C)


# random_list = [random.randint(1, 100) for _ in range(20)]
# print(random_list)
# start_time = time()
# quick_sort(random_list, 0, len(random_list) - 1)
# end_time = time()
# print("Exec Time:", end_time - start_time)
# print(random_list)
# print("Length:", len(random_list), ", comparisons:", comparisons, ", swaps", swaps)

for i in [10, 100, 1000, 10000, 100000]:
   random_list = [random.randint(1, 1000) for _ in range(i)]
   start_time = time()
   quick_sort(random_list, 0, i - 1)
   end_time = time()
   print(f"Length: {len(random_list)}, comparisons: {comparisons}, swaps: {swaps}")
   print("Exec Time:", end_time - start_time)
   print()
