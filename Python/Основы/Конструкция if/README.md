# Конструкция if ... elif ... else

В самом простом виде после ключевого слова `if` идет логическое выражение. Если это логическое выражение возвращает `True`, то выполняется последующий блок инструкций, выделенный отступами:

    age = 25
    if age > 18:
        print('Hello')
        print('Access granted')

В Python поддерживается вложенная конструкция `if`:

    age = 25
    height = 190
    if age >= 18:
        if height >= 180:
            print('Access granted')

Указанный выше пример приведен для демонстрации вложенности, его можно записать и короче:

    age = 25
    height = 190
    if age >= 18 and height >= 180:
        print('Access granted')

Если небходимо определить альтернативное решение на тот случай, если условное выражение возвратит `False`, то мы можем использовать блок `else`:

    age = 25
    if age > 18:
        print('Access granted')
    else:
        print('Access denied')

Если необходимо ввести несколько альтернативных условий, то можно использовать дополнительные блоки `elif`:

    score = 95
    if score >= 80:
        print('Excellent')
    elif score >= 60:
        print('Good')
    elif score >= 40:
        print('Bad')
    else: 
        print('Terrible')
