
user_data1 = input("Введите число 1: ")
user_data2 = input("Введите число 2: ")

try:
    num1 = float(user_data1)
    num2 = float(user_data2)
except ValueError:
    print("Вы ввели не число!")
else:
    try:
        a = num1 / num2
    except ZeroDivisionError:
        print("Второе число не должно быть равно нулю!")
    else:
        print("Деление чисел:", a)