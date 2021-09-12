def gcd(a:int, b:int) -> int:
    '''
    Возвращает наибольший общий делитель чисел a и b

    >>> gcd(100, 75)
    25
    >>> gcd(75, 100)
    25
    >>> gcd(3571, 1733)
    1
    >>> gcd(100, 98)
    2
    '''
    if b > a:
        return gcd(b, a)

    while b > 0:
        a, b = b, a % b 
    return a

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
