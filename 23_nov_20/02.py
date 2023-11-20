import math

user_data = input("Введите радиус: ")

try:
    num = float(user_data)
except ValueError:
    print("Вы ввели не число!")
else:
    square = math.pi * num ** 2
    print("Площадь круга:", square)