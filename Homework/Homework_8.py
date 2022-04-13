# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

print('>exercise # 1< \n')

my_list = ['qwe', 'rty', 'str', 'ing', 'big']
new_list = []

list_odd = my_list[::2]
odd_str = ', '.join(list_odd)
# str_reverse = odd_str[::-1]
str_reverse = (', '.join(my_list[::2]))[::-1]  # short code

print(str_reverse)

for index in enumerate(my_list):
    if index == my_list[::2]:
        new_list.append(str_reverse)

print(new_list)

################################################################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

print('>exercise # 2< \n')

my_list = ['apple', 'orange', 'banana', 'cherry', 'avocado']
new_list = []

for word in my_list:
    if word.startswith('a'):
        new_list.append(word)

print(f'{new_list} \n')
################################################################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

print('>exercise # 3< \n')

my_list = ['apple', 'orange', 'banana', 'cherry', 'avocado', ]
new_list = []

for word in my_list:
    if word.count('a'):
        new_list.append(word)

print(f'{new_list} \n')
################################################################################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# в) Посчитать среднее количество лет всех людей из начального списка.

print('>exercise # 4< \n')

persons = [{'name': 'John', 'age': 11},
           {'name': 'Patrick', 'age': 5},
           {'name': 'Jonathan', 'age': 7},
           {'name': 'Sam', 'age': 14},
           {'name': 'Leonardo', 'age': 5},
           {'name': 'Bill', 'age': 12},
           {'name': 'Jack', 'age': 32},
           ]

ages = []
longest_name = []

for key in persons:
    ages.append(key['age'])
    longest_name.append(len(key['name']))

min_age = min(ages)
max_len_name = max(longest_name)

print('<Youngest person>')

for key in persons:
    if key['age'] == min_age:
        print(key['name'])

print('<Longest name>')

for key in persons:
    if len(key['name']) == max_len_name:
        print(key['name'])

average_age = sum(ages) / len(ages)  # средний возраст людей
print(f'Average age = {average_age} \n')
################################################################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

print('>exercise # 5< \n')

my_dict_1 = {'key1': 1, 'key2': 2, 'key3': 3}
my_dict_2 = {'key11': 11, 'key2': 22, 'key33': 13}
same_key = []
different_key = []
my_dict_3 = dict()
merge_dict = dict()
values = []

print('key in the both dicts')
for key in my_dict_1:
    if key in my_dict_2:
        same_key.append(key)
print(same_key)

print('key not in the second dict')
for key in my_dict_1:
    if key not in my_dict_2:
        different_key.append(key)
print(different_key)

print('key & value not in the second dict')
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        my_dict_3[key] = value
print(my_dict_3)

print('merge two dicts')

merge_dict = my_dict_1.copy()
for key, value in my_dict_2.items():
    if key not in merge_dict:
    #     values = list(merge_dict.values())
    #     values.append(value)

print(values, merge_dict)