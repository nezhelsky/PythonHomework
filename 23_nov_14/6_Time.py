print("Введите текущее время в формате 24h:")
hours = input("Часы: ")
minutes = input("Минуты: ")

h = int(hours)
m = int(minutes)

h = 23 - h
m = 60 - m
print("До конца дня осталось: меньше", h, "часов", m, "минут")