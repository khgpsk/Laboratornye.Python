import math
import random

do = input("Введите арифметическое действие, либо 0 (рандомное число): ")

if do == "+":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 + number2)

elif do == "-":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 - number2)

elif do == "/":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    if number2 == 0:
        print("На 0 делить нельзя")
    else:
        print(number1/number2)

elif do == "*":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 * number2)

elif do == "pow":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(pow(number1, number2))

elif do == "module":
    number1 = float(input("Введите значение: "))
    print(abs(number1))

elif do == "0":
    print(random.randint(0, 1000))

elif do == "div":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    if number2 != 0:
        print("На 0 делить нельзя")
    else:
        print(number1//number2)

elif do == "mod":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 % number2)

elif do == "f":
    number1 = int(input("Введите значение: "))
    print(math.factorial(number1))

elif do == "arccos":
    number1 = float(input("Введите значение: "))
    number11 = number1*math.pi/180
    print(math.acos(number11))