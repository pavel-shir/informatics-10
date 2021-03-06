# Операции с числами

## Сложение

    print(10 + 13)  # 23

## Сложение с присвоением

    x = 10
    x += 13
    print(x)        # 23

## Вычитание

    print(10 - 13)  # -3

## Вычитание с присвоением

    x = 10
    x -= 13
    print(x)        # -3

## Умножение

    print(10 * 13)  # 130

## Умножение с присвоением

    x = 10
    x *= 13
    print(x)        # 130

## Деление

    print(7 / 2)    # 3.5
    print(6 / 2)    # 3.0
Даже если левый операнд делится на правый нацело - возвращается тип float.

## Деление с присвоением

    x = 7
    x /= 2 
    print(x)        # 3.5

## Целоцисленное деление

    print(7 // 2)   # 3
    print(6 // 2)   # 3
При целочисленном делении, в отличие от _обычного_ деления, возвращается тип int.

## Целоцисленное деление с присвоением

    x = 7
    x //= 2 
    print(x)        # 3

## Взятие остатка от деления

    print(17 % 5)   # 2

## Взятие остатка от деления с присвоением

    x = 17
    x %= 5
    print(x)        # 2

## Возведение в степень

    print(2 ** 10)      # 1024
    print(1024 ** 0.5)  # 32.0
В отличие от остальных операций возведение в степень выполняется _справа налево_: при выполнении оперции `2 ** 3 ** 4` сначала выполнится `3 ** 4` (получив результат 81), и только потом выполнится `2 ** 81`.

    print(2 ** 3 ** 4)  # 2417851639229258349412352

## Возведение в степень с присвоением

    x = 2
    x **= 10
    print(x)            # 1024
