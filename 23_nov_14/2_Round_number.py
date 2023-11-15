a = input("Введите дробное число: ")
b = input("Введите количество знаков после запятой для округления:")

number = float(a)
digits = int(b)

round_number = round(number, digits)
print("Округленное значение:", round_number)