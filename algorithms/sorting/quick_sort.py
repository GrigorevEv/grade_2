def quick_sort(a: list):
    if len(a) <= 1:
        return a

    barrier = a[0]
    l, m, r = [], [], []

    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    return quick_sort(l) + m + quick_sort(r)

# def quick_sort(A):
#     if len(A) <= 1:
#         return A

#     barrier = A[0]

#     left = list(filter(lambda x: x < barrier, A))
#     center = [i for i in A if i == barrier]
#     right = list(filter(lambda x: x > barrier, A))

#     return quick_sort(left) + center + quick_sort(right)

