
user_input_1 = input("Введите первое число: ")
user_input_2 = input("Введите второе число: ")

try:
    n1 = float(user_input_1)
    n2 = float(user_input_2)
except ValueError:
    print("Вы ввели не число!")

oper = input("Введите действие: ")

if oper == "+":
    a = n1 + n2
    print("Результат:", a)
elif oper == "-":
    a = n1 - n2
    print("Результат:", a)
elif oper == "/":
    a = n1 / n2
    print("Результат:", a)
elif oper == "*":
    a = n1 * n2
    print("Результат:", a)
else:
    print("Действие введено не корректно!")