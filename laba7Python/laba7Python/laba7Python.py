import math
import random

class Calculator:
    def plus(self, number1, number2):
        return number1 + number2

    def minus(self, number1, number2):
        return number1 - number2

    def div(self, number1, number2):
        if number2 == 0:
            print("На 0 делить нельзя!")
        else:
            return number1 / number2

    def multi(self, number1, number2):
        return number1 * number2

    def pow(self, number1, number2):
        return math.pow(number1, number2)

    def module(self, number1):
        return abs(number1)

    def rand(self, number1, number2):
        return random.uniform(number1, number2)

    def whole_div(self, number1, number2):
        if number2 == 0:
            print("На 0 делить нельзя!")
        else:
            return number1 / number2

    def mod(self, number1, number2):
        return number1 % number2

    def factorial(self, number1):
        return math.factorial(number1)

    def arccos(self, number1):
        return number1*math.pi/180

calc = Calculator()
do = input("Введите арифметическое действие, либо 0 (рандомное число): ")
while do != "q":
    if do == "+":
        print(calc.plus(number1 = float(input("Введите 1 значение: ")),number2 = float(input("Введите 2 значение: "))))

    elif do == "-":
        print(calc.minus(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif do == "/":
        print(calc.div(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif do == "*":
        print(calc.multi(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif do == "^":
        print(calc.pow(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif do == "module":
        print(calc.module(number1=float(input("Введите значение: "))))

    elif do == "0":
        print(calc.rand(number1=int(input("Введите наибольшее значение: ")), number2=int(input("Введите наименьшее значение: "))))

    elif do == "//":
        print(calc.whole_div(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif do == "%":
        print(calc.mod(number1=float(input("Введите 1 значение: ")), number2=float(input("Введите 2 значение: "))))

    elif do == "f":
        print(calc.factorial(number1=int(input("Введите  значение: "))))

    elif do == "acos":
        print(math.acos(calc.arccos(number1=float(input("Введите  значение: ")))))

    do = input("Введите оператор или введите q, что бы закончить: ")