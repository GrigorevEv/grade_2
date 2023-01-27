def merge_two_lists(a: list, b: list):
    """Функция слияния двух отсортированных массивов"""
    c = [0] * (len(a) + len(b))
    i = k = n = 0

    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1

    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1

    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(a):
    """Рекурсивная функция сортировки"""
    if len(a) <= 1:
        return a

    middle = len(a) // 2

    l = merge_sort(a[0:middle])
    r = merge_sort(a[middle:len(a)])

    return merge_two_lists(l, r)
