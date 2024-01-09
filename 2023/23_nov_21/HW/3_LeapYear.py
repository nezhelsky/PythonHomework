user_input = input("Введите год в формате YYYY: ")

if user_input != True and len(user_input) < 4: # проверяем, чтобы пользователь ввел не меньше 4 символов
    print("Вы ввели не год")
else:
    try:
        year = int(user_input)
    except ValueError:                 # проверяем, чтобы веденные данные оказались числом
        print("Вы ввели не число")
    else:
        if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0 and year >= 8:
            print("Год", year, "високосный")
        elif year < 8:
            print("Первыми високосными годами в Риме были 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9 годы до н.э., 8, 12 годы н.э. и в последующем каждый четвёртый год")
        else:
            print("Год", year, "не високосный")