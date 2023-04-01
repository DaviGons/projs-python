#imports
import math

#variables
number_1 = 0
number_2 = 0
result = 0
operation = 0
result_memory = []
option_1 = 0
option_2 = 0

#logic
print('''
Welcome to the Python3 Calculator!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Made by Davi Gonçalves Silva

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

while True:
    number_1 = int(input('First Number:  '))
    number_2 = int(input('Second Number: '))
    operation = int(input('''
    [1] = +
    [2] = -
    [3] = *
    [4] = /
    [5] = **
    [6] = SQRT (first number)
    [7] = ! (first number)
    [8] = Show Memory
    [0] = Quit Calculator

    '''))

    if operation == 1:
        result = number_1 + number_2
        print(result)
        option_1 = str(input("Wannna add to Memory Y/N: ")).strip().upper()
        if option_1 == "Y":
            result_memory.insert(1, result)

    elif operation == 2:
        result = number_1 - number_2
        print(result)
        option_1 = str(input("Wannna add to Memory Y/N: ")).strip().upper()
        if option_1 == "Y":
            result_memory.insert(1, result)

    elif operation == 3:
        result = number_1 * number_2
        print(result)
        option_1 = str(input("Wannna add to Memory Y/N: ")).strip().upper()
        if option_1 == "Y":
            result_memory.insert(1, result)

    elif operation == 4:
        result = number_1 / number_2
        print(result)
        option_1 = str(input("Wannna add to Memory Y/N: ")).strip().upper()
        if option_1 == "Y":
            result_memory.insert(1, result)

    elif operation == 5:
        result = number_1 ** number_2
        print(result)
        option_1 = str(input("Wannna add to Memory Y/N: ")).strip().upper()
        if option_1 == "Y":
            result_memory.insert(1, result)

    elif operation == 6:
        result = math.sqrt(number_1)
        print(result)
        option_1 = str(input("Wannna add to Memory Y/N: ")).strip().upper()
        if option_1 == "Y":
            result_memory.insert(1, result)

    elif operation == 7:
        result = math.factorial(number_1)
        print(result)
        option_1 = str(input("Wannna add to Memory Y/N: ")).strip().upper()
        if option_1 == "Y":
            result_memory.insert(1, result)

    elif operation == 8:
        print(result_memory)

    else:
        quit()