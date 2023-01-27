def insertion_sort(A):
    n = len(A)
    for top in range(1, n):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
