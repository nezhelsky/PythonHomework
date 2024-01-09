user_in = input("Введите числа через пробел: ")
user_list = user_in.split(' ')

numbers = []
try:
    for x in user_list:
        numbers += [int(x)]   # тут отличие от первого
except ValueError:
    print("У вас там не числа")
    exit()

print(numbers)

result = []
for x in numbers:
    if x <= 0:
        continue
    elif x > 1:
        for i in range(2, 1 + x//2):
            if x % i == 0:
                break
        else:
            result.append(x)
    else:
        result.append(x)

print(result)

