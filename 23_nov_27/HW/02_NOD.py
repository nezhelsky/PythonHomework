user_in1 = input("Введите первое число: ")
user_in2 = input("Введите второе число: ")

try:
    a = int(user_in1)
    b = int(user_in2)
except ValueError:
    print("Вы ввели не число!")
    exit()

c = ""
if a > b:   # в этом условии сравниваем числа, чтобы определить большее
    while c != 0:
        c = a % b
        a = b
        b = c
        c = a % b    # тут перед окончанием цикла проверяем С. Это какой-то колхоз, но он работает X(
    print("НОД двух чисел:", b)
else:
    while c != 0:
        c = b % a
        b = a
        a = c
        c = b % a
    print("НОД двух чисел:", a)