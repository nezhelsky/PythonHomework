
user_input_h = input("Input hours: ")
user_input_m = input("Input minutes: ")
user_input_s = input("Input seconds: ")

try:
    h = int(user_input_h)
    m = int(user_input_m)
    s = int(user_input_s)
except ValueError:
    print("Вы ввели не число!")
else:
    if (0 <= h < 24) and (0 <= m < 60) and (0 <= s < 60):
        print("Данные введены верно")
    else:
        print("Данные введены неверно!")  