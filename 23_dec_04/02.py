user_input = input("Введите любое число: ")
depth = len(user_input) // 2

a, b = int(user_input[:depth]), int(user_input[depth:])
print("Сумма двух чисел равна:", a + b)