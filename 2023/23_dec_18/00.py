
user1 = input("Введите первое число: ")
user2 = input("Введите второе число: ")

try:
    num1 = float(user1)
    num2 = float(user2)
except ValueError:
    print("Вы ввели не число!")
    exit()


def get_sum(a, b):
    result = a + b
    return result

my_sum = get_sum(num1, num2)
print("Результат = %.2f" % my_sum)