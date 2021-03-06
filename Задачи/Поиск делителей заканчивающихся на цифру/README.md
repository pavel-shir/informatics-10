# Поиск делителей заканчивающихся на цифру

## Постановка задачи

> Даны числа N и k, 1 ≤ N ≤ 10^6, 1 ≤ k ≤ 9
>
> Напишите программу, которая перебирает целые числа, бoльшие N, в порядке возрастания и ищет среди них такие, среди делителей которых есть числа, оканчивающиеся на k, но не равные k и самому числу.
>
> Необходимо вывести первые 5 таких чисел, и наименьший делитель, оканчивающийся на k, не равный k и самому числу.

## Решение с комментариями

    # Читаем данные из ввода
    n, k = list(map(int, input().split()))

    # Счетчик найденных чисел
    counter = 0

    # Массив, в котором будем хранить пары чисел (в виде кортежей):
    #   1. Найденное число
    #   2. Его делитель, оканчивающийся на k
    a = []

    # Бежим в цикле до тех пор, пока не найдем нужно количество чисел
    # В данной задаче явно указано что нужно найти 5 чисел, но это мог быть и входной параметр
    while counter < 5:
        # В каждой итерации увеличиваем n на 1
        n += 1

        # Пробегаем по всем числам от 2 до n // 2, каждое из них это потенциальный делитель n
        # Стоит отметить, что в range второй параметр указан как "n // 2 + 1", иначе можем не учесть n // 2
        for i in range(2, n // 2 + 1):
            # Для очередного числа i проверяем условия:
            #   1. Последней цифрой i является k
            #   2. i не равняется k
            #   3. n делится на i (т.е. i является делителем n)
            if i % 10 == k and i != k and n % i == 0:
                # Если условия выполнились - добавляем найденную пару в массив
                a.append((n, i))
                # Увеличиваем счетчик найденных чисел
                counter += 1
                # Выходим из цикла, т.к. если мы нашли нужный делитель i то остальные нам не интересны
                break

    # В цикле выводим ответ - по паре чисел в каждой строке, используя распаковку кортежей
    for x in a:
        print(*x)

## То же решение, без комментариев

    n, k = list(map(int, input().split()))
    counter = 0

    a = []

    while counter < 5:
        n += 1
        for i in range(2, n // 2 + 1):
            if i % 10 == k and i != k and n % i == 0:
                a.append((n, i))
                counter += 1
                break

    for x in a:
        print(*x)
