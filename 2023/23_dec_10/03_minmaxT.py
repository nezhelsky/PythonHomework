user_in = input("Введите числа через пробел: ")
user_list = user_in.split(' ')

numbers = []
try:
    for x in user_list:
        numbers += [int(x)]   # тут отличие от первого
except ValueError:
    print("У вас там не числа")
    exit()


result = []
for i in range(0, len(user_list),2):
    diff = numbers[i+1] - numbers[i]
    result.append(abs(diff))


print(result)