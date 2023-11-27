# Какой цвет не относится к основным цветам радуги?
# Оранжевый  Фиолетовый   Розовый
total = 0

print("Это небольшой квиз.")
print("Вам нужно ответить на 3 вопроса.")
print("За каждый правильный ответ вы получаите 2 балла.")

print("Какой цвет получается при смешении синего и красного?")
user_input = input("1-Коричневый  //  2-Фиолетовый  //  3-Голубой: ")
try:
    int(user_input)
    user_input != 1 or 2 or 3
except ValueError:
    print("Вы ввели не число или число отличное от 1, 2 или 3!")
else:
    if user_input == 2:
        total = total + 2
    else:
        total = total

print("Какого моря не существует?")
user_input = input("1-Жёлтого  //  2-Синего  //  3-Белого: ")
try:
    int(user_input)
    user_input != 1 or 2 or 3
except ValueError:
    print("Вы ввели не число или число отличное от 1, 2 или 3!")
else:
    if user_input == 2:
        total = total + 2
    else:
        total = total

print("Кольца какого цвета нет на олимпийском флаге?")
user_input = input("1-Голубого  //  2-Коричневого  //  3-Чёрного: ")
try:
    int(user_input)
    user_input != 1 or 2 or 3
except ValueError:
    print("Вы ввели не число или число отличное от 1, 2 или 3!")
else:
    if user_input == 2:
        total = total + 2
    else:
        total = total

print("Ваш результат", total)