in_str_length = input("Введите длину строки: ")
first_symbol = input("Введите символ_1: ")
second_symbol = input("Введите символ_2: ")

str_length = int(in_str_length)
str = first_symbol + second_symbol

if len(first_symbol) > 1 or len(second_symbol) > 1:
    print("Вы ввели больше одного символа!")
else:
    if str_length % 2 != 0:
        mult = int((str_length - 1) / 2)
        print(str * mult + first_symbol)
    else:
        mult = int(str_length / 2)
        print(str * mult)