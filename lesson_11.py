# параметры по умолчанию
# позиционные и именнованные аргументы
# типы переменных | аннотация типов
# импорт функций

############################################################################
import os
from utils.reading_file import read_txt_file_as_str  # функция которая умеет читать

path = "Homeworks"
list_dir = os.listdir(path)  # выводит содержимое папки
print(list_dir)

filename = 'lesson_4_test.txt'
base_dir = ''
data = read_txt_file_as_str(f"{path}/{base_dir}/{filename}")
# data = read_txt_file_as_str(os.path.join(path, base_dir, filename)) # приемущества если мы работаем с разными операционными системами
print(data)
############################################################################
for filename in list_dir:
    filepath = os.path.join(path, filename)  # печатает пути/файлы в папке(соединяет - join)
    if os.path.isdir(filepath):  # вычисляет есть ли папка в данном каталоге(isdir)
        print(filepath)
############################################################################
from utils.reading_file import read_txt_file_as_str, \
    DEBUG_MODE  # чтобы импортировать несколько данных, нужжно их перечислить через запятую. Если поставить * то можно использовать все(но не рекомендуется)

# в момент импорта происходит замена всех строки на весь файл(нужно его держать только с функциями и переменными, без доп. кодов и принта)
data = read_txt_file_as_str('lesson_test.txt')
print(f"{__name__=}")
print(data)
print(DEBUG_MODE)


#######################################################################################
def get_args(*args,
             **kwargs):  # *args(собирают в котреж) - все параметры позиционные.*kwargs - иенные параметры(собирают в списки)
    for arg_value in args:
        print(arg_value)
    for kwarg_value in kwargs:
        print(kwarg_value, kwargs[kwarg_value])


# работает * и ** . название может быть любое
get_args(1, 2, 'qwe', name="John", age=12)  # позиционные и именные параметры
############################################################################
from random import choice, randint
from string import ascii_lowercase as alphabet

DEBUG_MODE = True  # режим отладки, работает когда включен на TRUE, дает разверешине на действие IF


def create_email(domains, names,
                 debug_mode=DEBUG_MODE):  # режим отладки, работает когда включен на TRUE, дает разверешине на действие IF
    name = choice(names)
    number = randint(100, 999)
    some_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
    domain = choice(domains)
    e_mail = f"{name}.{number}@{some_str}.{domain}"
    if debug_mode:
        print(e_mail)
    return e_mail


names_list = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names=names_list)  # позиционные аргументы(важен порядок), иначе каша)))


# именнованые аргументы позволяют перемешать порядок, благодаря именнам переменных, делают для того чтобы не следить за порядком введения функции
# если начали писать именнованные переменные, то должны и продолжать их вводить. Но можно также и комбинировать их
def read_txt_file(filename="TEST.txt", debug_mode=DEBUG_MODE):
    with open(filename, 'r',
              encoding='utf-8') as my_file:  # первые обычно идут позиционные параметры(стандартные), остальные идут именнованные
        data = my_file.read()
    if debug_mode:
        print(data)
    return data


data = read_txt_file('lesson_test.txt')
print(data)

data = read_txt_file()
######################################################################################################################

DEBUG_MODE = True  # переменная, пишеться с большой буквы, чтобы показать, что она относиться ко всему вашему файлу(глобальная)


def read_txt_file_as_str(filename: str) -> str:  # -> означает то что функция должна вернуть
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    return data


# делает так чтоб не все импортировалось, спомощью if __name__ == "__main__"
if __name__ == "__main__":  # __main__ путь к данному файлу, который запускает код.(если запустил этот код из этого файла, то сделаем вот эту часть(ниже))
    print(">>>>>>>>>>>>>", __name__)  # запус функции из которого
    data = read_txt_file_as_str('TEST.txt')
    print(">>>>>>>>>>>>>", data)
######################################################################################################################
# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os
from string import ascii_lowercase as alphabet
from random import shuffle


def create_dir(dirname):  # функция для создания папки
    # os.mkdir(dirname) # создает только одну папку, если такая же папка существует то программа ругается
    os.makedirs(dirname,
                exist_ok=True)  # True - создается для того, чтобы отключить проверку и не выводить ошибку при написание повторяющегося названия папки


def create_file(dirname, symbol):
    file_path = os.path.join(dirname, f"{symbol}.txt")  # путь к файлу
    with open(file_path, 'w') as txt_file:
        txt_file.write(alphabet.replace(symbol, symbol.upper()))


def create_files(dirname):
    for symbol in alphabet:
        create_file(dirname, symbol)


def do_tannos_click(dirname):  # в скобках не подставлять название существующей папки иначе не восстановить
    dir_list = os.listdir(dirname)  # создал список из нашей директории
    shuffle(dir_list)  # перемешал список, чтобы удалить разные файлы
    for filename in dir_list[::2]:  # делает срез половины списка чтобы его удалить по срезу [::2]
        filepath = os.path.join(dirname, filename)  #
        os.remove(filepath)  # удаляет файлы


dirname = "alphabet"
create_dir(dirname)
create_files(dirname)
do_tannos_click(dirname)
