user_input = ""
summ = 0
while user_input != 0:
    user_input = input("Введите число: ")
    user_input = int(user_input)
    summ += user_input

print(summ)