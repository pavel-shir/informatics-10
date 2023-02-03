# Лабораторная по SQL и базам данных

## Схема БД

![db schema](./assets/schema.png)

Схема описывает набор таблиц, необходимых для составления расписания уроков. 

### WEEKDAYS

Таблица дней недели

`day_id` - `PK` (PRIMARY KEY, первичный ключ)

`day_name` - _название_ дня недели (пример: `ПН`)

### LESSONS

Таблица для описания уроков

`lesson_id` - `PK`

`lesson_number` - номер урока (пример: `1`)

`start_str` - время звонка на урок (пример: `09:00`)

`stop_str` - время звонка с урока (пример `09:45`)

Время звонков хранится в типа `varchar` для упрощения работы.

### TEACHERS

Таблица с преподавателями

`teacher_id` - `PK`

`teacher_name` - ФИО преподавателя (пример: `Иванов Иван Иванович`)

### SUBJECTS

Таблица с предметами

`subject_id` - `PK`

`subjejct_name` - _название_ предмета (пример: `Литература`)

### CLASSES

Таблица с классами

`class_id` - `PK`

`class_name` - _название_ класса (пример: `11 А`)

### CABINETS

Таблица с кабинетами

`cabinet_id` - `PK`

`cabinet_name` - _название_ кабинета (пример: `к. 142`)

### TIMETABLE 

_Центральная_ таблица в которой, собственно, и хранится расписание

`timetable_id` - `PK`

`day_id` - `FK` (FOREIGN KEY, внешний ключ)

`lesson_id` - `FK`

`teacher_id` - `FK`

`subject_id` - `FK`

`class_id` - `FK`

`cabinet_id` - `FK`

### Комментарии к схеме

При создании таблиц необходимо учитывать следующие условия:

* Все поля (т.е. колонки в таблицах) должны иметь ограничение `NOT NULL`
* Все поля, обозначенные `PK` должны иметь соответствующее ограничение на таблице
* Все поля, обозначенные `FK` должны иметь ссылку на соответствующую таблицу (см. схему)

## SQL

Лабораторная выполняется с использованием [SQLite](https://sqlite.org/docs.html) в [Google Colab](https://colab.research.google.com/).

### Расширение sql для Colab

Подключить расширение можно следующей командой:
```
%load_ext sql
```
После выполнения этой команды и использовании директивы `%sql` (для однострочного кода) и `%%sql` (для многострочного кода) можно выполнять SQL команды

Когда расширение подключено - можно попробовать подключиться к новой БД `lab.db`

```
%sql sqlite:///lab.db
```
В случае успеха в файлах появится `lab.db`

Если на подключении возникнет ошибка:
```
__init__() got an unexpected keyword argument 'bind'
Connection info needed in SQLAlchemy format, example:
               postgresql://username:password@hostname/dbname
               or an existing connection: dict_keys([])
```
значит, в Google опять что-то намудрили.

Починить это можно выполнив команду:
```
!pip install sqlalchemy==1.3.9
```
И перезапустив среду выполнения.

**Внимание:** после отключения от среды выполнения данные (т.е. БД и информация в ней) в неё не сохранятся (но сохранится код)

Писать код нужно так, чтобы восстановить все данные в БД если они будут утеряны.

Также перед работой необходимо включить валидацию `FOREIGN KEY` следующей командой:
```
%%sql
PRAGMA foreign_keys = ON;
```

### Создание таблицы

Таблицы создаются с помощью команды `CREATE`

Пример простой таблицы:
```
%%sql
create table movie(
    title varchar,
    year integer,
    score number
);
```

Если оказалось, что таблица создана неправильно - удалить её (вместе со всеми данными) можно командой `DROP`:

```
%%sql
drop table movie;
```

Пример создания таблицы с ограничением `NOT NULL`:
```
%%sql
create table some_table(
    some_id integer not null,
    some_name varchar
);
```

Пример таблицы с ограничением `PRIMARY KEY` на одном из полей:
```
%%sql
create table customers(
    customer_id integer primary key,
    customer_name varchar
);
```

Пример таблицы с `AUTOINCREMENT` на первичном ключе:
```
%%sql
create table customers(
    customer_id integer primary key autoincrement,
    customer_name varchar
);
```

Пример таблицы с `AUTOINCREMENT` на первичном ключе + `NOT NULL`:
```
%%sql
create table customers(
    customer_id integer primary key autoincrement not null,
    customer_name varchar
);
```

Пример таблицы с ограничением `FOREIGN KEY`:
```
%%sql
create table orders(
    order_id integer primary key autoincrement,
    customer_id integer not null,
    order_cost integer not null,
    foreign key (customer_id) references customers (customer_id)
);
```

### Добавление данных

Записи добавляются в таблицу командой `INSERT`

Пример добавления данных без указания столбцов (данные должны идти в том же порядке, что и столбцы в таблице):

```
%%sql
insert into customers values
    (1, 'aaa')
```

Пример добавления данных с указанием конкретных столбцов:
```
%%sql
insert into customers (customer_name) values
    ('bbb')
```

Пример добавления нескольких записей:
```
%%sql
insert into customers values
    (3, 'ccc'),
    (4, 'ddd'),
    (5, 'eee')
```

### Изменение данных

Записи в таблице модифицируются командой `UPDATE`

Пример изменения одной записи:
```
%%sql
update customers 
set customer_name = 'fff'
where customer_id = 3
```

Пример изменения нескольких записей:
```
%%sql
update customers 
set customer_name = 'ggg'
where customer_id > 3
```

Пример изменения всех записей:
```
%%sql
update customers 
set customer_name = 'hhh'
```

### Удаление данных

Записи в таблице модифицируются командой `DELETE`

Пример удаления одной записи:
```
%%sql
delete from customers 
where customer_id = 3
```

Пример удаления нескольких записей:
```
%%sql
delete from customers 
where customer_id < 3
```

Пример изменения всех записей:
```
%%sql
delete from customers
```

### Чтение / выборка данных

Записи из таблиц можно запрашивать с помощью команды `SELECT`

Пример запроса всех данных из таблицы:
```
%%sql
select *
from customers
```
`*` означает выборку всех столбцов

Пример с указанием конкретных столбцов:
```
%%sql
select
    customer_id,
    customer_name
from customers
```

Пример с использованием алиасов столбцов:
```
%%sql
select
    customer_id id,
    customer_name name
from customers
```

Пример с использованием алиаса таблицы:
```
%%sql
select
    c.customer_id,
    c.customer_name
from customers c
```

Пример с использованием фильтра:
```
%%sql
select
    c.customer_id,
    c.customer_name
from customers c
where c.customer_id = 3
```

Пример с использованием сортировки по одному полю:
```
%%sql
select
    c.customer_id,
    c.customer_name
from customers c
order by c.customer_name
```
По умолчанию поле сортируется по возрастанию

Пример с использованием сортировки по нескольким полям:
```
%%sql
select
    c.customer_id,
    c.customer_name
from customers c
order by c.customer_name asc,
    c.customer_id desc
```
`ASC` - по возрастанию

`DESC` - по убыванию

Для примера с несколькими таблицами сначала наполним их данными:
```
%%sql
delete from customers;
delete from orders;
insert into customers (customer_id, customer_name) values 
    (1, 'aaa'),
    (2, 'bbb');
insert into orders (order_id, customer_id, order_cost) values 
    (1, 1, 3000),
    (2, 1, 5000),
    (3, 2, 4000),
    (4, 2, 1000),
    (5, 2, 2000);
```

Пример выборки с соединением двух таблиц:

```
%%sql
select *
from customers c
inner join orders o
    on o.customer_id = c.customer_id
```

Пример выборки с соединением двух таблиц с указанием столбцов:

```
%%sql
select c.customer_name,
    o.order_id,
    o.order_cost
from customers c
inner join orders o
    on o.customer_id = c.customer_id
```

Пример выборки с соединением двух таблиц с указанием фильтра:

```
%%sql
select c.customer_name,
    o.order_id,
    o.order_cost
from customers c
inner join orders o
    on o.customer_id = c.customer_id
where o.order_cost > 3000
```

Пример выборки с функциями агрегации:
```
%%sql
select max(o.order_cost) max_cost, 
    count(o.order_cost) total_orders
from customers c
inner join orders o
    on o.customer_id = c.customer_id
```

Пример выборки с функциями агрегации и фильтром:
```
%%sql
select max(o.order_cost) max_cost, 
    count(o.order_cost) total_orders
from customers c
inner join orders o
    on o.customer_id = c.customer_id
where o.order_cost <= 3000
```

Пример агрегации с группировкой по определенным полям:
```
%%sql
select
    c.customer_name,
    max(o.order_cost) max_cost, 
    count(o.order_cost) total_orders
from customers c
inner join orders o
    on o.customer_id = c.customer_id
group by c.customer_name
```

Стоит отметить, что значение функций агрегаций нельзя использовать в блоке `WHERE`, для этого нужно использовать конструкцию `HAVING`, которая идет после `GROUP BY`:
```
%%sql
-- Так не работает
select
    c.customer_name,
    max(o.order_cost) max_cost, 
    count(o.order_cost) total_orders
from customers c
inner join orders o
    on o.customer_id = c.customer_id
where count(o.order_cost) > 2
group by c.customer_name
```

```
%%sql
-- Так работает
select
    c.customer_name,
    max(o.order_cost) max_cost, 
    count(o.order_cost) total_orders
from customers c
inner join orders o
    on o.customer_id = c.customer_id
group by c.customer_name
having count(o.order_cost) > 2
```

## Что необходимо сделать в работе

1. Создать таблицы по схеме, указанной в начале документа
2. Наполнить таблицы данными: в каждой таблице должно быть не менее 5 записей, а для `TIMETABLES` - не менее 30 записей.
3. Сделать следующие выборки:
   1. Выбрать все записи расписания со следующими столбцами:
      * `day_name`
      * `lesson_number`
      * `start_str`
      * `start_str`
      * `teacher_name`
      * `subjejct_name`
      * `class_name`
      * `cabinet_name`
   2. Выбрать всех учителей и посчитать их количество уроков, в выборке должны быть столбцы:
      * `teacher_name`
      * количество уроков
   3. Выбрать всех учителей и посчитать их количество уроков по конкретным предметам, в выборке должны быть столбцы:
      * `teacher_name`
      * `subject_name`
      * количество уроков
   4. Выбрать всех учителей, у которых есть несколько уроков в один день с одинаковым номером урока. В выборке должны быть:
      * `teacher_name`
      * `day_name`
      * `lesson_number`
      * количество уроков
   5. Выбрать все кабинеты, в которых есть несколько уроков в один день с одинаковым номером урока. В выборке должны быть:
       * `cabinet_name`
       * `day_name`
       * `lesson_number`
       * количество уроков
   6. Выбрать все классы, у которых есть несколько уроков в один день с одинаковым номером урока. В выборке должны быть:
       * `class_name`
       * `day_name`
       * `lesson_number`
       * количество уроков
   7. Посчитать количество различных предметов, которые ведет конкретный (по заданному `teacher_id`) преподаватель. В выборке должно быть:
       * `teacher_name`
       * `subject_name`
   8. Сделать выборку 1, но теперь отсортировать все уроки сначала по дням, потом по номерам уроков, потом по кабинетам. Из выборки отфильтровать все уроки, у которых номер <= 2.
   9. ...прочие выборки, которые может ещё придет в голову принимающему.

### Рекомендации

1. Включить валидацию `FOREIGN KEY`
2. Все выборки делать в отдельных ячейках и подписывать, что делает каждая.
3. Включить `AUTOINCREMENT` на центральной таблице `TIMETABLE` и не включать на остальных.
4. Отдельно оформить все скрипты, которые заполняют словарные таблицы.
5. Попробовать автоматизировать рандомное заполнение `TIMETABLE` (но не остальных таблиц). Для этого может помочь python и модуль [sqlite3](https://docs.python.org/3/library/sqlite3.html) 