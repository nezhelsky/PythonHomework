user_in = input("Введите число: ")
n = int(user_in)

a = 0
b = 1

for i in range(n + 1):
    print(i, "--", a)
    c = a + b
    a = b
    b = c