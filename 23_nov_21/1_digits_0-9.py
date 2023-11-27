user_input = input("Введите число от 0 до 9: ")

if user_input != True and len(user_input) > 1: # проверяем, чтобы пользователь ввел только один символ
    print("Вы ввели не цифру от 0 до 9")
else:
    try:
        digit = int(user_input)
    except ValueError:
        print("Вы ввели не число")
    else:
        if digit == 0:
            print(")")
        elif digit == 1:
            print("!")
        elif digit == 2:
            print("@")
        elif digit == 3:
            print("#")
        elif digit == 4:
            print("$")
        elif digit == 5:
            print("%")
        elif digit == 6:
            print("^")
        elif digit == 7:
            print("&")
        elif digit == 8:
            print("*")
        elif digit == 9:
            print("(")

