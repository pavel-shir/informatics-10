def fast_pow(a:int, n:int) -> int:
    '''
    Возводит a в степень n

    >>> fast_pow(2, 4)
    16
    >>> fast_pow(1, 100)
    1
    >>> fast_pow(2, 30)
    1073741824
    >>> fast_pow(0, 5)
    0
    >>> fast_pow(3, 10)
    59049
    '''
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n //= 2
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
