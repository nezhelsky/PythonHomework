
user_input_x = input("Input x: ")
user_input_y = input("Input y: ")

try:
    x = int(user_input_x)
    y = int(user_input_y)
except ValueError:
    print("Вы ввели не число!")
else:
    if x > 0 and y > 0:
        print("Точка находится в I четверти")
    elif x > 0 and y < 0:
        print("Точка находится в II четверти")
    elif x < 0 and y < 0:
        print("Точка находится в III четверти")
    elif x < 0 and y > 0:
        print("Точка находится в IV четверти")
    elif x == 0 and y > 0:
        print("Точка находится на оси X выше оси Y")
    elif x == 0 and y < 0:
        print("Точка находится на оси X ниже оси Y")
    elif x < 0 and y == 0:
        print("Точка находится на оси Y слева оси Х")
    elif x > 0 and y == 0:
        print("Точка находится на оси Y справа оси Х")
    else:
        print("Точка находится в центре оси координат")
