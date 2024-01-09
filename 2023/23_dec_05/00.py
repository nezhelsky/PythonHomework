user_data = input("Введите числа через запятую: ")
user_list = user_data.split(',')
print(user_list)

numbers = []
for x in user_list:
    numbers.append(int(x) + 10)


# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i]) + 10

print(numbers)