number_str1 = input("Введите число_1: ")
number_str2 = input("Введите число_2: ")

number_int1, number_int2 = int(number_str1), int(number_str2)
number = (number_int1 + number_int2) / 2

print("Среднее арифметическое чисел:", number)