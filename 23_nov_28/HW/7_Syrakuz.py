user_in = input("Введите число: ")
number = int(user_in)

iter = 0


while number > 1:
    if number % 2 != 0:
        number = (3 * number + 1)  # гугл говорит, что нечетное число не надо делить на 2
    else:
        number /= 2
    iter += 1
    print(int(number))
print("Значение «1» достигнуто за", iter, "итераций")
