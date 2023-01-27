def bubble_sort(A):
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
