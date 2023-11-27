user_input = input("Введите трехзначное число: ")

if user_input != True and len(user_input) != 3: # проверяем, чтобы пользователь ввел только три символа
    print("Вы ввели не трехзначное число")
else:
    try:
        number = int(user_input)
    except ValueError:
        print("Вы ввели не число")
    else:
        hundreds = number // 100            # Тут выдергиваем сотни, десятки и единицы
        decimals = number % 100 // 10
        digits = number % 100 % 10
        
        if hundreds == decimals or hundreds == digits or decimals == digits:
            print("В вашем числе есть одинаковые цифры")
        else:
            print("В вашем числе нет одинаковых цифр")
