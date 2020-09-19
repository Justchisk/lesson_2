"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа
данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать
у пользователя, а указать явно, в программе.
"""
# list = [1, 3.14, None, True, print]
# l_append = input('Введите все что угодно: ')
# list.append(l_append)
# for el in list:
#     print(el, type(el))
"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""
numbers = list(map(int, input('Введите числа для обмена значений: ').split()))
print(numbers)
j = 0
for i in range(int(len(numbers) / 2)):
    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    j += 2
print(numbers)
"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц 
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# Через list
season = int(input('Введите месяц года: '))
season_years = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']  # зима 2 раза т.к декабрь 12 месяц
if season <= 2 or season == 12:
    print(season_years[0] or season_years[4])
elif season < 3 or season <= 5:
    print(season_years[1])
elif season < 6 or season <= 8:
    print(season_years[2])
elif season < 9 or season <= 11:
    print(season_years[3])
# Через dict
season = None
season = int(input('Введите месяц года: '))
season_years = {
    '1': 'Зима',
    '2': 'Весна',
    '3': 'Лето',
    '4': 'Осень',
}  # зима 2 раза т.к декабрь 12 месяц
if season <= 2 or season == 12:
    if season == 1:
        print(season_years.setdefault('1'), ' Месяц январь')
    elif season == 2:
        print(season_years.setdefault('1'), ' Месяц февраль')
    elif season == 12:
        print(season_years.setdefault('1'), ' Месяц декабрь')

elif season < 3 or season <= 5:
    if season == 3:
        print(season_years.setdefault('2'), ' Месяц март')
    if season == 4:
        print(season_years.setdefault('2'), ' Месяц апрель')
    if season == 5:
        print(season_years.setdefault('2'), ' Месяц май')

elif season < 6 or season <= 8:
    if season == 6:
        print(season_years.setdefault('3'), ' Месяц июнь')
    if season == 7:
        print(season_years.setdefault('3'), ' Месяц июль')
    if season == 8:
        print(season_years.setdefault('3'), ' Месяц август')

elif season < 9 or season <= 11:
    if season == 9:
        print(season_years.setdefault('4'), ' Месяц сентябрь')
    if season == 10:
        print(season_years.setdefault('4'), ' Месяц октябрь')
    if season == 5:
        print(season_years.setdefault('4'), ' Месяц ноябрь')
"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""
input_user = input('Введите несколько слов: ').split()
for i, string in enumerate(input_user):
    if len(string) > 10:
        string = string[:10]
    print(f'{i + 1}) {string}')
"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
  с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
"""
my_list = [7, 5, 3, 3, 2]
new_num = int(input('Введите число: '))
my_list.append(new_num)
my_list.sort()
my_list.reverse()
print(my_list)

"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и 
словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""
goods = int(input('Введите кол-во товара: '))
n = 1
my_dict = []
my_list = []
my_analys = []
while n <= goods:
    my_dict = dict({'название': input("Введите название: "), 'цена': input("Введите цену: "),
                    'количество': input('Введите количество: '), 'eд': input("Введите единицу измерения: ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)
