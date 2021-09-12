def sieve(n:int) -> list:
    '''
    Возвращет массив размера n + 1
    Если элемент с индексом i имеет значение True - то число i простое
    Иначе число i составное

    >>> sieve(0)
    [False]
    >>> sieve(1)
    [False, False]
    >>> sieve(2)
    [False, False, True]
    >>> sieve(3)
    [False, False, True, True]
    >>> sieve(10)
    [False, False, True, True, False, True, False, True, False, False, False]
    '''
    if n == 0:
        return [False]

    a = [True] * (n + 1)
    a[0] = a[1] = False
    i = 2
    while i * i <= n + 1:
        if a[i]:
            for j in range(2 * i, n + 1, i):
                a[j] = False
        i += 1
    return a

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
