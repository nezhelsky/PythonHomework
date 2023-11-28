user_in1 = input("Введите первое число диапазона: ")
user_in2 = input("Введите второе число диапазона: ")

try:
    user_in1 = int(user_in1)
    user_in2 = int(user_in2)
except ValueError:
    print("Вы ввели не число!")
    exit()

if user_in1 > user_in2:   # в этом условии сравниваем числа диапазона, чтобы определить какое число будет началом диапазона
    a = user_in2
    b = user_in1
    sum = user_in2
else:
    a = user_in1
    b = user_in2
    sum = user_in1

while a != b:
    a += 1
    sum += a

print("Сумма всех чисел диапазона =", sum)

