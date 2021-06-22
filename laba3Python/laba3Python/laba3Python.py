import math
import random

znak = input("Введите арифметическое действие, либо 0 (рандомное число): ")

if znak == "+":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 + number2)

elif znak == "-":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 - number2)

elif znak == "/":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    if number2 == 0:
        print("На 0 делить нельзя")
    else:
        print(number1/number2)

elif znak == "*":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 * number2)

elif znak == "pow":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(pow(number1, number2))

elif znak == "module":
    number1 = float(input("Введите значение: "))
    print(abs(number1))

elif znak == "0":
    print(random.randint(0, 1000))

elif znak == "div":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    if number2 != 0:
        print("На 0 делить нельзя")
    else:
        print(number1//number2)

elif znak == "mod":
    number1 = float(input("Введите 1 значение: "))
    number2 = float(input("Введите 2 значение: "))
    print(number1 % number2)

elif znak == "f":
    number1 = int(input("Введите значение: "))
    print(math.factorial(number1))

elif znak == "arccos":
    number1 = float(input("Введите значение: "))
    number11 = number1*math.pi/180
    print(math.acos(number11))
