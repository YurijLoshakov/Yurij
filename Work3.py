from math import factorial, acos
from random import randrange

print('''
Программа Калькулятор.
Выберите действие:
'+' - сложение
'-' - вычитание
'*' - умножение
'/' - деление
'**' - возведение в степень
'abs' - модуль числа
'random' - рандомное число
'factorial' - факториал числа
'acos' - арккосинус
'stop' - закончить работу программы
''')

def plus(digit, digit2):
    print(int(digit + digit2))
def minus(digit, digit2):
    print(int(digit - digit2))
def mult(digit, digit2):
    print(int(digit * digit2))
def division(digit, digit2):
    print(float(digit / digit2))
def exp(digit, digit2):
    print(int(digit ** digit2))

enter = input("Введите действие: ")

while(enter != "stop"):
    if(enter == "+"):
        plus(int(input("Первое число: ")), int(input("Второе число: ")))
    elif(enter == "-"):
        minus(int(input("Первое число: ")), int(input("Второе число: ")))
    elif (enter == "*"):
        mult(int(input("Первое число: ")), int(input("Второе число: ")))
    elif (enter == "/"):
        division(float(input("Первое число: ")), float(input("Второе число: ")))
    elif (enter == "**"):
        exp(int(input("Первое число: ")), int(input("Второе число: ")))
    elif (enter == "abs"):
        print(abs(int(input("Введите число: "))))
    elif (enter == "random"):
        print(randrange(int(input("Введите число: "))))
    elif (enter == "factorial"):
        print(factorial(int(input("Введите число: "))))
    elif (enter == "acos"):
        print(acos(int(input("Введите число от '-1' до '1': "))))
    enter = input("Введите действие: ")

