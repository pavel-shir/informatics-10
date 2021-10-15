def qsort(a):
    '''
    Сортирует список a
    Возвращает отсортированный список
    >>> a = [4, 1, 5, 3, 2]
    >>> qsort(a)
    [1, 2, 3, 4, 5]
    >>> a = [43, 13, 25, 3, 2, 1]
    >>> qsort(a)
    [1, 2, 3, 13, 25, 43]
    '''
    if len(a) <= 1:
        return a
    n = len(a)
    pivot = a[(len(a) - 1) // 2]    # Опорный элемент
    l = []                          # Список с элементами меньше опорного
    e = []                          # Список с элементами больше опорного
    r = []                          # Список с элементами равными опорному
    for i in range(n):
        if a[i] < pivot:
            l.append(a[i])
        elif a[i] > pivot:
            r.append(a[i])
        else:
            e.append(a[i])

    return qsort(l) + e + qsort(r)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
