user_in = input("Введите номер дня недели: ")
try:
    day = int(user_in)
except ValueError:
    print("Вы ввели не число!")
    exit()

match day:
    case 1:
        day_name = "Понедельник"
    case 2:
        day_name = "Вторник"
    case 3:
        day_name = "Среда"
    case 4:
        day_name = "Четверг"
    case 5:
        day_name = "Пятница"
    case 6:
        day_name = "Суббота"
    case 7:
        day_name = "Воскресенье"
    case _:
        day_name = "Неизвестный день!"

print(day_name)