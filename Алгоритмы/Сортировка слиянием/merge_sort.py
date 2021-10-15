def merge(a, b):
    '''
    Cливает два отсортированных списка в один отсортированный список
    Возвращает итоговый список
    >>> merge([1], [5])
    [1, 5]
    >>> merge([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> merge([13, 94], [42, 50])
    [13, 42, 50, 94]
    >>> merge([2, 4, 6], [1, 3, 5])
    [1, 2, 3, 4, 5, 6]
    '''
    c = []
    n = len(a)
    m = len(b)
    i = j = 0

    while i < n or j < m:
        if j == m or (i < n and a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    return c

def merge_sort(a):
    '''
    Сортирует список a
    Возвращает отсортированный список
    >>> merge_sort([4, 1, 5, 3, 2])
    [1, 2, 3, 4, 5]
    >>> merge_sort([49, 21, 22, 35, 60, 49, 93, 28, 42, 90])
    [21, 22, 28, 35, 42, 49, 49, 60, 90, 93]
    >>> merge_sort([2, 2, 1, 2, 1, 2, 1, 1, 1])
    [1, 1, 1, 1, 1, 2, 2, 2, 2]
    '''
    n = len(a)
    if n <= 1:
        return a
    p = n // 2

    return merge(merge_sort(a[:p]), merge_sort(a[p:]))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
