# 1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# 2

my_str = 'blablacar'
my_symbol = 'bla'

count = my_str.count(my_symbol)
print(count)

# 2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать столько раз my_symbol, сколько он встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# bla
# bla

my_str = 'blablacar'
my_symbol = 'bla'

# count = my_str.count(my_symbol)
# for _ in range(count):
#     print(my_symbol)

count = my_str.count(my_symbol)
bla_list = [my_symbol] * count
bla = "\n".join(bla_list)
print(bla)

# 3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько
# РАЗНЫХ символов встречается в my_str.
# Большая и маленькая буква считается как один символ.
# Пробелы, запятые и т.д. считаем тоже как символы.
# Пример:  my_str="bla BLA car".
# Вывод на экран:
# 6

my_str = "bla BLA car"
my_str = my_str.lower()
# box = []
box = ""
for symbol in my_str:
    if symbol not in box:
        # box.append(symbol)
        box += symbol
result = len(box)
print(result)

# 4) Дана строка my_str и пустой список my_list.
# Заполнить my_list символами из my_str,
# которые стоят на четных местах в строке (считаем с 0)

my_str = 'string'
my_list = []

# 1a
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# # 1b
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# # 2
# my_list.extend(list(my_str[::2]))
# 3
my_list += list(my_str[::2])

print(my_list, id(my_list))

# 5) Дана строка my_str, список str_index целых чисел в диапазоне от
# 0 до длинны строки минус 1, пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на местах с
# индексами из str_index

my_str = 'string'
str_index = [0, 1, 2, 3, 4, 5, ]
my_list = []

for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
    # my_list.append(my_str[index])
print(my_list)

# 6) Дано целое число (int). Определить сколько цифр в этом числе.

number = 12345678912
result = len(str(number))
print(result)

# 7) Дано целое число. Определить наибольшую цифру в этом числе.

number = 1234567834212
result = max(str(number))
print(result)

# 8) Дано целое число. Составить число (int) с цифрами в обратном порядке.

number = 123456789145562999
result = int(str(number)[::-1])
print(result)

# 9) Дано целое число. Составить число с цифрами в порядке возрастания(убывания).

number = 12345678912

# numb_list = list(str(number))  # преобразуем число в список
# numb_list.sort(reverse=True)  # сортируем списк по возрастанию(); (reverse=True) - убыванию
# str_numb = ''.join(numb_list)  # преобразуем список в строку(без разделений)
# new_numb = int(str_numb)  # преобразуем строку в числовое значение
# print(new_numb)

number_str = str(number)
sort_number_list = sorted(number_str, reverse=True)
sort_number_str = "".join(sort_number_list)
result = int(sort_number_str)
print(result)

result = int("".join(sorted(str(number), reverse=True)))
print(result)



# 10) Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и
# my_list_2 через один, начиная с my_list_1.
# a) кол-во эл-тов одинаковое
# б) кол-во эл-тов разное

my_list_1 = [10, 2, 3, 4, 5, 6, ]
my_list_2 = [4, 5, 6, 7, 8, 10, ]
my_result = []

list_len = min(len(my_list_1), len(my_list_2))
for index in range(list_len):
    value_1 = my_list_1[index]
    value_2 = my_list_2[index]
    my_result += [value_1, value_2]

my_result += my_list_1[list_len:]
my_result += my_list_2[list_len:]
print(my_result)

# генераторы списков
# множества

my_str = "qwerty123"
my_list = []
for symbol in my_str:
    my_list.append(symbol)
my_list = [symbol for symbol in my_str]
print(my_list)

limit_value = 10
numbers = [number ** 0.5 for number in range(limit_value)]
print(numbers)

my_list = [12, 34, -54, 2, -6, 8]
result = [value ** 2 for value in my_list if value > 0]
print(result)

alphabet = [chr(index) for index in range(ord("a"), ord("z") + 1)]
print(alphabet)

#####################################################################
# генераторы списков
# множества

my_list = list('qwerty123ytrewq321')
my_set = set(my_list)  # нет повторов, не сохраняет порядок, изменяемый
print(my_set, type(my_set))


my_str = "bla BLA car"
result = len(set(my_str.lower()))
print(result)

my_list = [10, 2, 3, 2, 2, 3]
print(set(my_list))

my_set_1 = set("12345")
my_set_2 = {"1", "2", 3}

result_union = my_set_1.union(my_set_2)
print(result_union)

result_intersection = my_set_1.intersection(my_set_2)
print(result_intersection)

result_difference = my_set_2.difference(my_set_1)
print(result_difference)

my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
for symbol in set(my_str):
    print(symbol)