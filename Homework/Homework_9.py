# Для задания 1-7 за основу можете взять код из предідущих ДЗ.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
print('>exercise # 1< \n')

my_list = ['qwe', 'rty', 'str', 'ing', 'big']


def mix_list(my_list):
    new_list = my_list.copy()
    for index, str_ in enumerate(my_list):
        if index % 2 == 0:
            new_list[index] = str_[::-1]
    return new_list


result_1 = mix_list(my_list)
print(result_1)
################################################################################################################
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
print('>exercise # 2< \n')

my_list = ['apple', 'orange', 'banana', 'cherry', 'avocado']


def find_fruits(my_list):
    new_list = []
    for word in my_list:
        if word.startswith('a'):
            new_list.append(word)
    return new_list


result_2 = find_fruits(my_list)
print(result_2)
################################################################################################################
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
print('>exercise # 3< \n')

my_list = ['apple', 'orange', 'banana', 'cherry', 'avocado', ]


def find_fruits_with_a(my_list):
    new_list = []
    for word in my_list:
        if word.count('a'):
            new_list.append(word)
    return new_list


result_3 = find_fruits_with_a(my_list)
print(result_3)
################################################################################################################
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
print('>exercise # 4< \n')

my_list = [1, 2, 3, "qwe", "rty", 33, ]


def find_string(my_list):
    result = [symbol for symbol in my_list if type(symbol) == str]
    return result


result_4 = find_string(my_list)
print(result_4)
################################################################################################################
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
print('>exercise # 5< \n')

my_str = 'millenium'


def find_single_letter(my_str):
    my_list = []
    for letter in set(my_str):
        if my_str.count(letter) == 1:
            my_list.append(letter)
    return my_list


result_5 = find_single_letter(my_str)
print(result_5)
################################################################################################################
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
print('>exercise # 6< \n')

my_str_1 = 'qwerty123'
my_str_2 = 'python_3.8'


def two_strings(my_str_1, my_str_2):
    result = list(set(my_str_1).intersection(set(my_str_2)))

    return result


result_6 = two_strings(my_str_1, my_str_2)
print(result_6)
################################################################################################################
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
print('>exercise # 7< \n')

my_str_1 = 'aaaasdf1'
my_str_2 = 'asdfff2'


def letters_in_2(my_str_1, my_str_2):
    my_list = []
    for symbol in set(my_str_1).intersection(set(my_str_2)):
        if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
            my_list.append(symbol)

    return my_list


result_7 = letters_in_2(my_str_1, my_str_2)
print(result_7)
################################################################################################################
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
print('>exercise # 8< \n')

import random
import string

names = ['Zelensky', 'Kim', 'Arestovich', 'Petrov', 'Ivanov', ]
domains = ['com', 'net', 'ua', 'gov', ]


def create_email(names, domains):
    choose_name = random.choice(names) + '.' + str(random.randint(100, 1000)) + '@'
    various_letters = "".join([random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 7))])
    # alphabet = string.ascii_lowercase
    # len_string = random.randint(5,7)
    # letters_list = [random.choice(alphabet) for _ in range(len_string)]
    # various_letters = "".join(letters_list)
    choose_domain = various_letters + '.' + random.choice(domains)
    result = choose_name + choose_domain
    return result


e_mail = create_email(names, domains)
print(e_mail)
