def qsort(a, start, stop):
    '''
    Сортирует часть списка a начиная со start заканчивая stop
    Элементы с индексами start и stop включаются в сортировку
    Не возвращает ничего, сортирует массив "на месте"
    >>> a = [4, 1, 5, 3, 2]
    >>> qsort(a, 0, len(a) - 1)
    >>> print(a)
    [1, 2, 3, 4, 5]
    >>> a = [43, 13, 25, 3, 2, 1]
    >>> qsort(a, 0, 2)
    >>> print(a)
    [13, 25, 43, 3, 2, 1]
    '''
    if start >= stop:
        return
    
    l = start
    r = stop
    pivot = a[(l + r) // 2]
    while l <= r:
        while a[l] < pivot:
            l += 1
        while a[r] > pivot:
            r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    qsort(a, start, r)
    qsort(a, l, stop)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
