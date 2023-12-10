user_in = input("Введите числа через пробел: ")
user_list = user_in.split(' ')

numbers = []
try:
    for x in user_list:
        numbers.append(int(x))
except ValueError:
    print("У вас там не числа")
    exit()

result = []

for x in numbers:
    if x:
        result += [x//abs(x)]
    else:
        result += [0]

print(result)