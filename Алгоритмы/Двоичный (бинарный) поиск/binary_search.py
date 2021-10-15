def bin_search(a, x):
    '''
    Проверяет наличие элемента x в списке a
    Список a должен быть отсортирован по неубыванию
    Возвращает True если элемент есть в списке
    Иначе возвращает False
    >>> bin_search([1, 2, 3, 4, 5], 1)
    True
    >>> bin_search([1, 2, 3, 4, 5], 10)
    False
    >>> bin_search([1, 1, 1, 2, 2], 2)
    True
    >>> bin_search([1, 1, 1, 2, 2], 3)
    False
    >>> bin_search([10, 20, 30, 50, 99], 99)
    True
    >>> bin_search([10, 20, 30, 50, 99], 29)
    False
    >>> bin_search([1], 1)
    True
    >>> bin_search([1], 99)
    False
    >>> bin_search([], 99)
    False
    '''
    n = len(a)
    l = 0
    r = n

    while r > l:
        pivot = (l + r) // 2
        if a[pivot] < x:
            l = pivot + 1
        elif a[pivot] > x:
            r = pivot
        else:
            return True

    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)