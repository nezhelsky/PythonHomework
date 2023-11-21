user_input_tmin = input("Введите минимальное значение температуры: ")
user_input_tmax = input("Введите максимальное значение температуры: ")

try:
    t_min = int(user_input_tmin)
    t_max = int(user_input_tmax)
except ValueError:
    print("Вы ввели не число!")
else:
    temp_range = abs(t_max - t_min)
    print("Перепад температуры:", temp_range)