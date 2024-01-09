user_input = input("Введите слово любой длины: ")
depth = len(user_input) // 2

print(user_input[:depth], user_input[depth:])