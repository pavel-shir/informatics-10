# Стандартный ввод и вывод

## Ввод данных. Функция `input()`

Функция `input()` отвечает за ввод в программу данных с клавиатуры. При вызове `input()` программа останавливает исполнение и ждет, пока пользователь введёт текст. Этот текст можно сохранить в переменную и использовать в программе:

    >>> name = input()
    John
    >>> print('Hello', name)
    Hello John

В данном примере пользователь ввёл с клавиатуры `John` и нажал `Enter`.
Символ переноса строки при этом не будет записан в переменную `name`.

Функция `input()` принимает один необязаятельный параметр - строку, которая будет *приглашением* к вводу с клавиатуры:

    >>> name = input('Enter your name: ')
    Enter your name: John
    >>> print('Hello ' + name)
    Hello John

Данный параметр особо полезен в случаях, когда в программе предполагается ввод нескольких параметров - *приглашение* поможет пользователю понять, что программа ожидает от него ввода, и что необходимо ввести.

Функция `input()` возвращает тип `str`:

    >>> n = input()
    42
    >>> print(type(n))
    <class 'str'>
    >>> print(n + 1)
    TypeError: can only concatenate str (not "int") to str

В данном примере функция `type()` возвращает тип переменной `n`. Можно заметить, что переменная `n` имеет тип `string`, даже если пользователь пытается ввести *число*.

Если нужно работать с вводом как с числом, то необходимо провести преобразование типа - к примеру, через функцию `int()` (приведение к целому числу) или `float()` (приведение к числу с плавающей точкой):

    >>> n = int(input())
    42
    >>> print(type(n))
    <class 'int'>
    >>> print(n + 1)
    43

В данном примере результат `input()` сразу приводится к целому числу, а результат записывается в переменную `n`.

Стоит отметить, что если результат невозможно привести к целому числу - программа выбросит исключение:

    >>> n = int(input())
    Hello
    ValueError: invalid literal for int() with base 10: 'Hello'

### Примеры ввода

#### 1. Ввод списка целых чисел, записанных через пробел

Напишем программу, которая получает из ввода список типа `int`.

Допуcтим, что ввод в этом примере выглядит так:

    1 2 3 4 5

Сначала получим введённую строку:

    >>> s = input()
    1 2 3 4 5
    >>> print(s)
    1 2 3 4 5

Тип переменной `s` - `str`. Для того, чтобы получить из `s` список, воспользуемся методом `split()`:

    >>> a = s.split()
    >>> print(a)
    ['1', '2', '3', '4', '5']

Если в метод `split()` не передавать параметров - то по умолчанию *разделителем* считается символ пробела.
Метод `split()` принимает два параметра - первый это *разделитель*, второй - максимальное количество разбиений.
Примеры использования `split()` с параметрами:

    >>> '1,2,3'.split()
    ['1,2,3']
    >>> '1,2,3'.split(',')
    ['1', '2', '3']
    >>> '1,2,3'.split(',', 1)
    ['1', '2,3']

С помощью `split()` мы получили список `a`, но видно, что это список строк.

Теперь необходимо привести каждый элемент списка к типу `int` - сделать это можно пробежав по всем элементам списка, применить к каждому функцию `int()` и записав полученные значения в новый список:

    >>> b = []
    >>> for i in range(len(a)):
    >>>     b.append(int(a[i]))
    >>> print(b)
    [1, 2, 3, 4, 5]

Данная операция выглядит несколько громоздко. В Python мы можем воспользоваться функцией `map()` если хотим сделать какое-то преобразование сразу со всеми элементами списка:

    >>> b = map(int, a)
    >>> print(b)
    <map object at 0x0000022E45550FA0>

`map()` принимает два параметра - *название применяемой функции* и *итерируемый объект*. В примере выше *применямой функцией* является `int`, а *итерируемым объектом* - список `a`.
Возвращает данная функция не список, а итерируемый `map object`, который можно преобразовать в список с помощью функции `list()`:

    >>> c = list(b)
    >>> print(c)
    [1, 2, 3, 4, 5]

В итоге код будет выглядеть так:

    s = input()
    a = s.split()
    b = map(int, a)
    c = list(b)

Данный код можно записать и короче:

    c = list(map(int, input().split()))

Стоит отметить, что нигде явно не задавалось количество вводимых чисел - и программа будет работать с любым их количеством (до тех пор, пока программе будет хватать памяти).

#### 2. Ввод двух целых чисел через пробел

Допуcтим, что ввод в этом примере выглядит так:

    10 50

Иногда нам заранее известно количество вводимых через пробел чисел - и не совсем удобно работать с ними в списке, а хочется дать каждому из них свою переменную.

Оглядываясь на прошлый пример, легко написать код для этого случая:

    c = list(map(int, input().split()))
    n = c[0]    # 10
    m = c[1]    # 50
    print(n * m)

В результате программа выведет `500`.

Этот пример можно записать короче:

    c = list(map(int, input().split()))
    n, m = c
    print(n * m)

В данном случае происходит *деструктурирование* списка - значение первого (с индексом `0`) элемента будет записано в `n`, а значение второго (с индексом `1`) будет записано в `m`. Работает это с любым количеством переменных - главное, чтобы количество переменных слева от оператора `=` и количество элементов массива было одинаковым.

В итоге можно вообще отказаться от лишней переменной, записав пример так:

    n, m = list(map(int, input().split()))
    print(n * m)

#### 3. Ввод целых чисел, записанных в отдельных строках

В случае, если несколько чисел записаны в отдельных строках - необходимо заранее знать сколько их, ведь в этом случае на каждое число понадобится отдельный вызов `input()`.
Обычно в таких случаях в первой строке ввода дают количество чисел, а потом уже сам список.

Допуcтим, что ввод в этом примере выглядит так:

    4
    31
    68
    12
    9

В первой строке дано количество чисел (`n`), которые необходимо прочитать - а потом дано `n` чисел.

Код в этом случае выглядит так:

    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    print(a)

В результате программа выведет полученный массив:

    [31, 68, 12, 9]

#### 4. Ввод строк

Как и в прошлом примере - сначала задается количетво вводимых строк, а потом идут значения строк.

Допуcтим, что ввод в этом примере выглядит так:

    2
    Hello
    World

Код в этом случае выглядит так:

    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    print(a)

В результате программа выведет полученный массив:

    ['Hello', 'World']

К типу `int` в данном примере нужно приводить только введённое количество строк.
Раз `input()` уже отдает строки, то внутри `for` никаких специальных преобразований с вводом проводить не нужно.

## Вывод данных. Функция `print()`

Функция `print()` выводит в терминал то, что передано в неё с помощью параметров:

    >>> print(42)
    42
    >>> print(3.14)
    3.14
    >>> print('Hello')
    Hello

У строк при выводе опускаются кавычки.

Выводить с помощью `print()` можно также списки, кортежи, и более сложные объекты:

    >>> print([1, 2, 3])
    [1, 2, 3]
    >>> print(('Hello', 'World'))
    ('Hello', 'World')

Функция `print()` работает не только с *литералами* (например `42` или `'Hello'`) но и с переменными:

    >>> a = 100
    >>> print(a)
    100

В `print()` можно передавать сразу несколько параметров, перечислив их через запятую:

    >>> a = 100
    >>> b = 200
    >>> print(a, b)
    100 200

В данном случае `print()` выведет их, разделив пробелом.

Разделитель можно поменять - для этого у функции `print()` есть *именованный параметр* `sep`. К примеру, если нужно использовать символ подчеркивания (`'_'`) вместо пробела в качестве разделителя, то код будет выглядеть так:

    >>> a = 1
    >>> b = 2
    >>> c = 'Hello'
    >>> print(a, b, c, sep='_')
    1_2_Hello

Если вызовать `print()` несколько раз - каждый вывод будет происходить в новой строке.

К примеру, у следующей программы:

    a = 1
    b = 2
    print(a)
    print(b)

Будет такой вывод:

    1
    2

Это происходит потому, что `print()` добавляет в конце вывода символ переноса строки (`'\n'`).
Это поведение `print()` тоже можно поменять, передав при вызове именованный параметр `end`:

    a = 1
    b = 2
    print(a, end='***')
    print(b, end='^^^')

Результат будет следующий:

    1***2^^^

Параметры `end` и `sep` можно использовать одновременно:

    >>> a = 1
    >>> b = 2
    >>> print(a, b, sep='-', end='***')
    1-2***

### Примеры вывода

#### 1. Вывод двух чисел через запятую

Пример достаточно тривиален:

    a = 100
    b = 500
    print(a, b, sep=',')

В результате будет выведено:

    100,500

#### 2. Вывод чисел из массива в отдельных строках

В данном случае необходимо пройти по массиву и вывести каждый его элемент отдельным вызовом `print()`.

    a = [1, 2, 3]
    for i in range(len(a)):
        print(a[i])

Результатом будет:

    1
    2
    3

В данном примере за последней строкой также идет символ переноса строки.
Если перенос строки нужно вывести только *между* элементами массива, но не в конце - то можно поступить так: привести все элементы массива к типу `str`, а после *склеить* символом `'\n'` с помощью метода `join()`:

    a = [1, 2, 3]
    b = '\n'.join(list(map(str, a)))
    print(b, end='')

В итоге в выводе не будет переноса строки после последней строки. На практике вывод переноса строки в конце не воспрещается, а иногда даже считается *хорошим тоном* - и необходимость в подобных манипуляциях появляется довольно редко.

#### 3. Вывод чисел из массива в одной строке

В данном примере можно поступить как в прошлом - выводить по одному числу, но при этом используя пробел в качестве параметра `end`:

    a = [1, 2, 3]
    for i in range(len(a)):
        print(a[i], end=' ')

Более простым способом будет вывод с использованием *распаковки*:

    a = [1, 2, 3]
    print(*a)

Символ `*` используетя для *распаковки* списка `a` - запись `print(*a)` эквивалентна записи `print(a[0], a[1], a[2])` (в случае, когда в массиве три элемента).

В обоих примерах вывод будет выглядеть так:

    1 2 3

Отличие только в том, что при выводе в цикле после последнего элемента идет символ пробела и не будет переноса строки, в то время как при выводе с распаковкой лишнего пробела нет, но перенос строки в конце появится (так как при вызове `print()` мы его не переопределяли).
