array = ['Timur', 'Argyn', 'Sergey', 'Almat', 'Vyacheslav', 'Alexandr', 'Galymjan', 'Vitaly']

new_array = sorted(array, key=lambda a: len(a)) # Сортировка списка array по ключу "длина элемента"
print(new_array)

# def sum2(num1, num2):
    # return num1 + num2
lambda num1, num2: num1 + num2   # так можно записать функцию sum2 в виде лямбда-функции

# 1. map
# 2. filter
# 3. reduce

result = list(map(lambda x: x[-1], new_array))
print(result)

# result = []                  это можно записать как map выше
# for x in array:
#     result.append(x[-1])

userlist = ["2", "45", "-7", "4"]
numbers = list(map(int, userlist))
print(numbers)

