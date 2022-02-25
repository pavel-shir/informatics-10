# Метод `pack`

Остановимся на вопросе расположения виджетов в окне. Это важный вопрос, так как от продуманности интерфейса во многом зависит удобство использования программы. Организуя виджеты в пространстве, программист отчасти становится дизайнером, разработчиком интерфейсов.

В Tkinter существует три так называемых менеджера геометрии – упаковщик (`pack`), сетка (`grid`) и размещение по координатам (`place`). В этой статье будет рассмотрен первый как наиболее простой и часто используемый.

Упаковщик (packer) вызывается методом `pack`, который имеется у всех виджетов-объектов. Если к элементу интерфейса не применить какой-либо из менеджеров геометрии, то он не отобразится в окне. При этом в одном окне (или любом другом родительском виджете) нельзя комбинировать разные менеджеры. Если вы начали размещать виджеты методом `pack`, не пытайтесь тут же использовать методы `grid` и `place`.

Если в упаковщики не передавать аргументы, то виджеты будут располагаться вертикально, друг над другом. Тот объект, который первым вызовет `pack`, будет вверху. Который вторым – под первым, и так далее.

У метода `pack` есть параметр `side` (сторона), который принимает одно из четырех значений-констант `tkinter` – `tk.TOP`, `tk.BOTTOM`, `tk.LEFT`, `tk.RIGHT` (верх, низ, лево, право). По умолчанию, когда в `pack` не указывается `side`, его значение равняется `tk.TOP`. Из-за этого виджеты располагаются вертикально.

Создадим четыре раскрашенные метки:

    l1 = Label(width=7, height=4, bg='yellow', text='1')
    l2 = Label(width=7, height=4, bg='orange', text='2')
    l3 = Label(width=7, height=4, bg='lightgreen', text='3')
    l4 = Label(width=7, height=4, bg='lightblue', text='4')

Рассмотрим разные комбинации значений `side`.

Сверху вниз:

    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()

Снизу вверх:

    l1.pack(side=tk.BOTTOM)
    l2.pack(side=tk.BOTTOM)
    l3.pack(side=tk.BOTTOM)
    l4.pack(side=tk.BOTTOM)

Слева направо:

    l1.pack(side=tk.LEFT)
    l2.pack(side=tk.LEFT)
    l3.pack(side=tk.LEFT)
    l4.pack(side=tk.LEFT)

Справа налево:

    l1.pack(side=tk.RIGHT)
    l2.pack(side=tk.RIGHT)
    l3.pack(side=tk.RIGHT)
    l4.pack(side=tk.RIGHT)

Рассмотрим ещё один пример:

    l1.pack(side=tk.LEFT)
    l2.pack(side=tk.LEFT)
    l3.pack(side=tk.BOTTOM)
    l4.pack(side=tk.LEFT)

Проблема этого варианта в том, что если не распологать виджеты в одну линию (строго горизонтально или строго вертикально) то их расположение становится несколько непредсказуемым.

Если надо разместить виджеты квадратом, т. е. два сверху, два снизу ровно под двумя верхними, то сделать это проблематично. Поэтому прибегают к вспомогательному виджету – рамке, который порождается от класса `Frame`.

Фреймы размещают на главном окне, а уже в фреймах – виджеты:

    import tkinter as tk

    root = tk.Tk()
    f_top = tk.Frame(root)
    f_bot = tk.Frame(root)
    l1 = tk.Label(f_top, width=7, height=4, bg='yellow', text='1')
    l2 = tk.Label(f_top, width=7, height=4, bg='orange', text='2')
    l3 = tk.Label(f_bot, width=7, height=4, bg='lightgreen', text='3')
    l4 = tk.Label(f_bot, width=7, height=4, bg='lightblue', text='4')
    
    f_top.pack()
    f_bot.pack()
    l1.pack(side=tk.LEFT)
    l2.pack(side=tk.LEFT)
    l3.pack(side=tk.LEFT)
    l4.pack(side=tk.LEFT)
    
    root.mainloop()

Кроме `Frame` существует похожий класс `LabelFrame` – фрейм с подписью. В отличие от простого фрейма у него есть свойство `text`:

    import tkinter as tk

    root = tk.Tk()
    f_top = tk.LabelFrame(root, text='Верх')
    f_bot = tk.LabelFrame(root, text='Низ')
    l1 = tk.Label(f_top, width=7, height=4, bg='yellow', text='1')
    l2 = tk.Label(f_top, width=7, height=4, bg='orange', text='2')
    l3 = tk.Label(f_bot, width=7, height=4, bg='lightgreen', text='3')
    l4 = tk.Label(f_bot, width=7, height=4, bg='lightblue', text='4')
    
    f_top.pack()
    f_bot.pack()
    l1.pack(side=tk.LEFT)
    l2.pack(side=tk.LEFT)
    l3.pack(side=tk.LEFT)
    l4.pack(side=tk.LEFT)
    
    root.mainloop()

Кроме `side` у `pack` есть другие параметры-свойства. Можно задавать внутренние (`ipadx` и `ipady`) и внешние (`padx` и `pady`) отступы:

    import tkinter as tk

    root = tk.Tk()
    f_top = tk.LabelFrame(root, text='Верх')
    f_bot = tk.LabelFrame(root, text='Низ')
    l1 = tk.Label(f_top, width=7, height=4, bg='yellow', text='1')
    l2 = tk.Label(f_top, width=7, height=4, bg='orange', text='2')
    l3 = tk.Label(f_bot, width=7, height=4, bg='lightgreen', text='3')
    l4 = tk.Label(f_bot, width=7, height=4, bg='lightblue', text='4')

    f_top.pack(padx=10, pady=10)
    f_bot.pack(ipadx=10, ipady=10)
    l1.pack(side=tk.LEFT)
    l2.pack(side=tk.LEFT)
    l3.pack(side=tk.LEFT)
    l4.pack(side=tk.LEFT)
    
    root.mainloop()

Когда устанавливаются внутренние отступы, то из-за того, что `side` прибивает виджет к левой границе, справа получаем отступ в 20 пикселей, а слева – ничего. Можно частично решить проблему, заменив внутренние отступы рамки на внешние отступы у меток.

    import tkinter as tk

    root = tk.Tk()
    f_top = tk.LabelFrame(root, text='Верх')
    f_bot = tk.LabelFrame(root, text='Низ')
    l1 = tk.Label(f_top, width=7, height=4, bg='yellow', text='1')
    l2 = tk.Label(f_top, width=7, height=4, bg='orange', text='2')
    l3 = tk.Label(f_bot, width=7, height=4, bg='lightgreen', text='3')
    l4 = tk.Label(f_bot, width=7, height=4, bg='lightblue', text='4')

    f_top.pack(padx=10, pady=10)
    f_bot.pack()
    l1.pack(side=tk.LEFT)
    l2.pack(side=tk.LEFT)
    l3.pack(side=tk.LEFT, padx=10, pady=10)
    l4.pack(side=tk.LEFT, padx=10, pady=10)
    
    root.mainloop()

Но тут появляется промежуток между самими метками. Чтобы его убрать, пришлось бы каждый виджет укладывать в свой собственный фрейм. Отсюда делаем вывод, что упаковщик Tkinter удобен только для относительно простых интерфейсов.

Следующие два свойства – `fill` (заполнение) и `expand` (расширение). По-умолчанию `expand` равен нулю (другое значение – единица), а `fill` – `tk.NONE` (другие значения `tk.BOTH`, `tk.X`, `tk.Y`). Создадим окно с одной меткой:

    import tkinter as tk

    root = tk.Tk()
    l1 = tk.Label(text='This is a label', width=30, height=10, bg='lightgreen')
    l1.pack()
    root.mainloop()

Если начать расширять окно или сразу раскрыть его на весь экран, то метка окажется вверху по вертикали и в середине по горизонтали. Причина, по которой метка не в середине по вертикали заключается в том, что `side` по-умолчанию равен `tk.TOP`, и метку прибивает к верху.

Если установить свойство `expand` в 1, то при расширении окна метка будет всегда в середине:

    import tkinter as tk

    root = tk.Tk()
    l1 = tk.Label(text='This is a label', width=30, height=10, bg='lightgreen')
    l1.pack(expand=1)
    root.mainloop()

Свойство `fill` заставляет виджет заполнять все доступное пространство. Заполнить его можно во всех направлениях или только по одной из осей:

    import tkinter as tk

    root = tk.Tk()
    l1 = tk.Label(text='This is a label', width=30, height=10, bg='lightgreen')
    l1.pack(expand=1, fill=tk.Y)
    root.mainloop()

Ещё одна важная опция метода `pack` – `anchor` (якорь) – может принимать значения `tk.N` (north – север), `tk.S` (south – юг), `tk.W` (west – запад), `tk.E` (east – восток) и их комбинации:

    import tkinter as tk

    root = tk.Tk()
    l1 = tk.Label(text='This is a label', width=30, height=10, bg='lightgreen')
    l1.pack(expand=1, anchor=tk.SE)
    root.mainloop()

В последнем пример метка будет прибиваться к _юго-восточному_ (нижнему правому) углу.