import math

user_data1 = input("Введите число 1: ")
user_data2 = input("Введите число 2: ")

try:
    num1 = int(user_data1)
    num2 = int(user_data2)
except ValueError:
    print("Вы ввели не число!")
else:
    diff = num1 - num2
    try:
        result = math.sqrt(diff)
    except ValueError:
        print("Первое число должно быть больше!")
    else:
        print("Результат:", result)