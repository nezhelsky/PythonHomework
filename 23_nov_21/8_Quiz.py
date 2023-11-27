# Какой цвет не относится к основным цветам радуги?
# Оранжевый  Фиолетовый   Розовый
score = 0
score_step = 2

print("Какой цвет получается при смешении синего и красного: 1-Коричневый  //  2-Фиолетовый  //  3-Голубой")
user_input = input("Ваш ответ: ")
if user_input in ("1", "2", "3"):
    if user_input == "2":
        score += score_step
    else:
        print("Неверный ввод!")

print("Какого моря не существует?")
user_input = input("1-Жёлтого  //  2-Синего  //  3-Белого: ")
if user_input in ("1", "2", "3"):
    if user_input == "2":
        score += score_step
else:
    print("Неверный ввод!")

print("Кольца какого цвета нет на олимпийском флаге?")
user_input = input("1-Голубого  //  2-Коричневого  //  3-Чёрного: ")
if user_input in ("1", "2", "3"):
    if user_input == "2":
        score += score_step
else:
    print("Неверный ввод!")

print("Ваш результат", score)