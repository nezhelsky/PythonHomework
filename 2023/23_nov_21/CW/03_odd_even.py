
user_input = input("Input number: ")

try:
    a = int(user_input)
except ValueError:
    print("Вы ввели не число!")
else:
    if a % 2 != 0:
        print("Нечетное число")
    else:
        print("Четное число")  