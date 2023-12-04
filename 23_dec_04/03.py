user_input = input("Введите любое слово: ")
depth = len(user_input)
a = "*"

print(user_input[0] + a * (depth - 2) + user_input[-1])