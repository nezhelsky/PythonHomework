
user_input = input("Введите цифру от 0 до 9: ")
# наш ввод должен удовлетворять двум условиям: 1. длина строки <2  2. ввод должен переводиться в int() без ошибки

if len(user_input) > 1: # проверяем ввод на длину
    print("Вы ввели что-то не то!")
else:
    try:
        x = int(user_input)
    except ValueError: # проверяем что, тот символ, который ввёл пользователь - это цифра
        print("Вы ввели не цифру!")
    else:
        if x == 0:    # ну и дальше выполнение условия
            print(")")
        elif x == 1:
            print("!")
        elif x == 2:
            print("@")
        elif x == 3:
            print("#")
        elif x == 4:
            print("$")
        elif x == 5:
            print("%")
        elif x == 6:
            print("^")
        elif x == 7:
            print("&")
        elif x == 8:
            print("*")
        elif x == 9:
            print(")")