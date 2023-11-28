user_in = input("Введите число: ")

num = int(user_in)

for i in range(1, num):
    if num % i == 0:
        print(i)