
user_input = input("Input age: ")

try:
    a = int(user_input)
except ValueError:
    print("Вы ввели не число!")
else:
    if 3 <= a <= 120:
        print("Правда")
    else:
        print("Вы врете!")  