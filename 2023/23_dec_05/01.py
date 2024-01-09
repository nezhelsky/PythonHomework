user_in = input("Введите 10 чисел: ").split(",")
while len(user_in) < 10:
    print("Вы ввели меньше 10 символов, введите данные заново")

if len(user_in) > 10:
    while len(user_in)>10:
        user_in.pop(10)

            # print(user_in)

    
numbers = []
numbers2 = []
for x in user_in:
    numbers.append(int(x))
    if int(x) % 2 ==0:
        numbers2.append(int(x))
print("Первый список:", *numbers)
print("Второй список:", *numbers2)










