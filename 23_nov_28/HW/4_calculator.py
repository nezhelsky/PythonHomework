i = "1"

while i == "1":
    user_input_1 = input("Введите первое число: ")
    oper = input("Введите действие: ")
    user_input_2 = input("Введите второе число: ")

    try:
        n1 = float(user_input_1)
        n2 = float(user_input_2)
    except ValueError:
        print("Вы ввели не число!")
        
    if oper == "+":
        a = n1 + n2
        print("Результат:", a)
    elif oper == "-":
        a = n1 - n2
        print("Результат:", a)
    elif oper == "/":
        if n2 == 0:
            print("ДЕЛЕНИЕ НА НОЛЬ!")
        else:
            a = n1 / n2
        print("Результат:", a)
    elif oper == "*":
        a = n1 * n2
        print("Результат:", a)
    else:
        print("Действие введено не корректно!")
    
    i = input("Хотите продолжить? 1-Да, 0-нет: ")
