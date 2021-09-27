# Функции преобразования типов

Python не делает _неявных_ приведений типов.
К примеру, следующий код вызовет исключение:

    >>> x = '10'
    >>> y = 20
    >>> print(x + y)

    TypeError: can only concatenate str (not "int") to str
В Python есть ряд встроенных функций, позволяющих переводит значения из одного типа в другой:

    x = '10'
    y = 20
    summ = int(x) + y
    print(summ)         # 30

Если привести тип не получается - интерпретатор выбросит исключение:

    >>> x = 'abcd'
    >>> print(int(x))

    ValueError: invalid literal for int() with base 10: 'abcd'

## `int()` - приведение к целому числу

    x = '1234'
    print(int(x))   # 1234

    x = '000314'
    print(int(x))   # 314

    x = '  34   '
    print(int(x))   # 34

    x = 3.14
    print(int(x))   # 3

## `float()` - приведение к числу с плавающей точкой

    x = '3.14'
    print(float(x)) # 3.14
    
    x = 3
    print(float(x)) # 3.0
