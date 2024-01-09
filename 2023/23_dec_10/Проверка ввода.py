while numbers is None:
    user_in = input("Введите числа через пробел: ")
    user_list = user_in.split(' ')
    try:
        numbers = [int(x) for x in user_list]
    except ValueError:
        print("У вас там не число")