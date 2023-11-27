a = input("Введите a: ")
b = input("Введите b: ")

try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Вы ввели не число")
else:
    try:
        x = - (b / a)
    except ZeroDivisionError:
        print("Попытка деления на ноль. Значение 'а' не может равняться 0")
    else:
        print("Решение уравнения ax+b=0 для заданных a и b:", x)