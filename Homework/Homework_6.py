########################### 1 ###########################
# У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [2, 20, 33, 223, 334, 338, 547, 756, 877, 9999, ]
for number in my_list:
    if number > 100:
        print(number)

########################### 2 ###########################
#  У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [25, 55, 78, 445, 547, 999, ]
my_result = []
for number in my_list:
    if number > 100:
        my_result.append(number)
print(my_result)

########################### 3 ###########################
# У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [20, 45, 78, ]
index = 2

if len(my_list) < index:
    my_list.append(0)
elif len(my_list) >= index:
    add = int(my_list[-1] + my_list[-2])
    my_list.append(add)
print(my_list)
