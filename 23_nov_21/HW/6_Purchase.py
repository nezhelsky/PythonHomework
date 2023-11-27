user_input = input("Введите стоимость товара: ")

try:
    cost = int(user_input)
except ValueError:
    print("Вы ввели не число!")
else:
    if cost < 300:
        total = 0.97 * cost
        print("Цена со скидкой:", total)
    elif 300 <= cost < 500:
        total = 0.95 * cost
        print("Цена со скидкой:", total)
    elif cost >= 500:
        total = 0.93 * cost
        print("Цена со скидкой:", total)