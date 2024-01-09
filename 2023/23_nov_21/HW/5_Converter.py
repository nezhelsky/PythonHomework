eur_curr = 0.9
uah_curr = 36
azn_curr = 1.7

user_input_usd = input("Введите сумму в $: ")
input_curr = input("Выберите валюту конвертации: 1-EUR, 2-UAH, 3-AZN: ")

try:
    usd = float(user_input_usd)
except ValueError:      # проверяем, чтобы веденные доллары оказались числом
    print("Вы ввели не число")
else:
    if input_curr == "1":
        a = round(usd * eur_curr, 2)
        print("$", usd, "= EUR", a)
    elif input_curr == "2":
        a = round(usd * uah_curr, 2)
        print("$", usd, "= UAH", a)
    elif input_curr == "3":
        a = round(usd * azn_curr, 2)
        print("$", usd, "= AZN", a)
#    elif  print("Не выбрана валюта для конвертации! Для выбора нажмите 1,2 или 3")