def sieve(n:int) -> list[int]:
    '''
    Возвращет массив размера n + 1
    В массиве элемент с индексом i имеет значение минимального делителя числа i
    В 0-м и 1-м элементах будут указаны 0
    a[i] == i означает что число i простое (для всех i > 1)

    >>> sieve(0)
    [0]
    >>> sieve(1)
    [0, 0]
    >>> sieve(3)
    [0, 0, 2, 3]
    >>> sieve(10)
    [0, 0, 2, 3, 2, 5, 2, 7, 2, 3, 2]
    '''
    if n == 0:
        return [0]

    s = [0] * (n + 1)
    primes = []
    
    for i in range(2, n + 1):
        if s[i] == 0:
            s[i] = i
            primes.append(i)
        for pr in primes:
            if pr > s[i] or i * pr > n:
                break
            s[i * pr] = pr
    return s

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
