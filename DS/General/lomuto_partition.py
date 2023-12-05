def lomuto_partition(A, left, right):
    pivot = A[left]
    s = left
    for i in range(left, right + 1):
        if A[i] < pivot:
            s += 1
            A[s], A[i] = A[i], A[s]
    A[left], A[s] = A[s], A[left]
    return s

def quick_select(A, k, left, right):
    s = lomuto_partition(A, left, right)
    if s - left == k - 1:
        return A[s]
    elif s > left + k - 1:
        return quick_select(A, k, left, s-1)
    else:
        return quick_select(A, k + left - 1 - s, s + 1, right)

arr = [ 10, 4, 5, 8, 6, 11, 26 ] 
n = len(arr)
k = 4
print("K-th smallest element is ", end = "") 
print(quick_select(arr, k, 0, n - 1)) 
