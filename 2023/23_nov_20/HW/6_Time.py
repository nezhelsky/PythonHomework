print("Введите текущее время в формате 24h:")
hours = input("Часы: ")
minutes = input("Минуты: ")

try:
    h = int(hours)
    m = int(minutes)
except ValueError:
    print("Вы ввели не число")
else:
    h = 23 - h
    m = 60 - m
    print("До конца дня осталось: меньше", h, "часов", m, "минут")