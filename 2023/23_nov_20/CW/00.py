a = input("Введите целое число: ")
try:
    a = int(a)
except ValueError:
    print("Вы ввели не число!")
else:
    result = a*a
    print(result)
finally:
    print("Конец")