user_input = input("Введите число >50: ")

try:
    a = int(user_input)
except ValueError:
    print("Вы ввели не число")

counter = 0
if a < 50:
    print("Вы ввели число <50!")
    exit()
else:
    while a >= 50:
        a /= 2
        counter += 1
print("Результат:", a, "за", counter, "делений.")