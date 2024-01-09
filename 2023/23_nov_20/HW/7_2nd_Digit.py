a = input("Введите трехзначное целое число: ")

try:
    a = int(a)
except ValueError:
    print("Вы ввели не число")
else:
    a = a % 100 // 10
    print("Вторая цифра:", a)