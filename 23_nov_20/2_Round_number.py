a = input("Введите дробное число: ")
b = input("Введите количество знаков после запятой для округления:")

try:
    number = float(a)
    digits = int(b)
except ValueError:
    print("Вы ввели не число!")
else:
    round_number = round(number, digits)
    print("Округленное значение:", round_number)