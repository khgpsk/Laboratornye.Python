import math
import random

def plus(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def delenie(number1, number2):
    if number2 == 0:
        return print("На 0 делить нельзя!")
    else:
        number1/number2

def ymnowenie(number1, number2):
    return number1 * number2

def pow(number1, number2):
    return math.pow(number1, number2)

def module(number1):
    return abs(number1)

def rand(number1, number2):
    return random.uniform(number1, number2)

def factorial(number1):
    return math.factorial(number1)

def arccos(number1):
    return number1*math.pi/180

znak = input("Введите арифметическое действие, либо 0 (рандомное число): ")
while znak != "q":
    if znak == "+":
        print(plus(number1 = float(input("Введите 1 значение: ")),number2 = float(input("Введите 2 значение: "))))

    elif znak == "-":
        print(minus(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif znak == "/":
        print(div(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif znak == "*":
        print(multi(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif znak == "^":
        print(pow(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif znak == "module":
        print(module(number1=float(input("Введите значение: "))))

    elif znak == "0":
        print(random.randint(0, 1000))
        break
        
    elif znak == "f":
        print(factorial(number1=int(input("Введите  значение: "))))

    elif znak == "arccos":
        print(math.acos(arccos(number1=float(input("Введите  значение: ")))))
