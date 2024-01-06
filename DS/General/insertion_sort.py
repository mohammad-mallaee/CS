def sort(A: list):
    for i in range(len(A)):
        for j in range(i):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]

def sort_2(A: list):
    for i in range(1, len(A)):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v

my_list = [12, 5, 18, 9, 20]
sort_2(my_list)
print(my_list)
