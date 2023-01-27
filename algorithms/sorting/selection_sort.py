def selection_sort(A):
    n = len(A)
    for pos in range(n-1):
        for k in range(pos+1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
