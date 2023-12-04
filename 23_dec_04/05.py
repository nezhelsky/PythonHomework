year = input("Введите год: ")
month = input("Введите месяц: ")
date = input("Введите число: ")

year = int(year)
month = int(month)
date = int(date)

message = "%02d.%02d.%04d" % (date, month, year)
print(message)