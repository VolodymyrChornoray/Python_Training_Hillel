#######################################################
value = 24
new_value = value / 2 if value < 100 else - value
print(int(new_value))
#######################################################
value = 15
new_value = 1 if value < 100 else 0
print(int(new_value))
#######################################################
value = 255
new_value = True if value < 100 else False
print(int(new_value))
########################################################
my_str = "qwer"
if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)
########################################################
my_str = "qwer"
if len(my_str) < 5:
    print(my_str + my_str[::-1])
else:
    print(my_str)
########################################################
running = True
while running:
    input_case = input("Choose type of operation:\n1 +\n2 -\n3 *\n4 /\n: ")
    if input_case in "1,2,3,4":
        try:
            value_1 = float(input("Enter your first number:"))
            value_2 = float(input("Enter your second number:"))
            if input_case == "1":
                result = value_1 + value_2
                sign = '+'
            elif input_case == "2":
                result = value_1 - value_2
                sign = '-'
            elif input_case == "3":
                result = value_1 * value_2
                sign = '*'
            else:
                result = value_1 / value_2
                sign = '/'
            print(f'{value_1} {sign} {value_2} = {result}')
        except ZeroDivisionError:
            print("Can't divide by 0 !!!\nTry again")
        except ValueError:
            print("Wrong entry! \n Please type number!")
    else:
        print("Chosen undefined operation!\nTry again")
    question = input("Do you want to calculate more? \nType 'Y' or 'N': ")
    running = question.upper() != 'N'
print('End of operation')
