a = input("Введите данные продаж в этом месяце ($):")

try:
    a = int(a)
except ValueError:
    print("Вы ввели не число")
else:
    a = 250 + 0.1 * a
    print("В этом месяце вы получите: $", a)