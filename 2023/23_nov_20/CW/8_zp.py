default_sales = 0
user_in = input("Введите данные продаж в этом месяце ($):")

try:
    a = int(user_in)
except ValueError:
    sales = default_sales
    print("Вы получите только оклад!")

salary = 250 + 0.1 * sales
print("В этом месяце вы получите: $", salary)