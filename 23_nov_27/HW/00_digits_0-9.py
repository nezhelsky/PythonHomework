user_input = input("Введите число от 0 до 9: ")

try:
    digit = int(user_input)
except ValueError:
    print("Вы ввели не число")

match digit:
    case 0:
        print(")")
    case 1:
        print("!")
    case 2:
        print("@")
    case 3:
        print("#")
    case 4:
        print("$")
    case 5:
        print("%")
    case 6:
        print("^")
    case 7:
        print("&")
    case 8:
        print("*")
    case 9:
        print("(")
    case _:
        print("Вы ввели неверное число!")

