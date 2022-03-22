# example of calculator with variate operation

input_case = input('Choose type of operation: \n 1 + add \n 2 - subtract \n 3 * multiply \n 4 / divide \n '
                   '5 % percentage \n 6 *2 squaring \n 7 (x)y exponentiation \n')

if input_case == '1':
    value_1 = input('Enter your first number:')
    value_2 = input('Enter your second number:')
    result = int(value_1) + int(value_2)
    print('Answer is:', result)
elif input_case == '2':
    value_1 = input('Enter your first number:')
    value_2 = input('Enter your second number:')
    result = int(value_1) - int(value_2)
    print('Answer is:', result)
elif input_case == '3':
    value_1 = input('Enter your first number:')
    value_2 = input('Enter your second number:')
    result = int(value_1) * int(value_2)
    print('Answer is:', result)
elif input_case == '4':
    value_1 = input('Enter your first number:')
    value_2 = input('Enter your second number:')
    result = int(value_1) / int(value_2)
    print('Answer is:', result)
elif input_case == '5':
    value_1 = input('Enter your number:')
    result = float(value_1) * 100
    print('Answer is:', int(result), '%')
elif input_case == '6':
    value_1 = input('Enter your number:')
    result = int(value_1) ** 2
    print('Answer is:', result)
elif input_case == '7':
    value_1 = input('Enter number x:')
    value_2 = input('Enter number y:')
    result = int(value_1) ** int(value_2)
    print('Answer is:', result)
else:
    result = 'Chosen undefined operation!'
    print(result)
print('End of calculation')
print('///////////////////')

# Below codes writen with exception to errors

input_case = input('Choose type of operation: \n 1 * multiply \n 2 / divide \n ')

try:
    if input_case == '1':
        value_1 = input('Enter your first number:')
        value_2 = input('Enter your second number:')
        result = float(value_1) * float(value_2)
        print('Answer is:', result)
    elif input_case == '2':
        value_1 = input('Enter your first number:')
        value_2 = input('Enter your second number:')
        result = float(value_1) / float(value_2)
        print('Answer is:', result)
    else:
        result = 'Chosen undefined operation!'
        print(result)
except ValueError:
    print("Wrong entry! \n Please type number!")
except ZeroDivisionError:
    print("Can't divide by 0 !!!")
print('End of operation')
