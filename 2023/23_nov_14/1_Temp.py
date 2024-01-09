t_min_str = input("Введите минимальное значение температуры: ")
t_max_str = input("Введите максимальное значение температуры: ")

t_min = int(t_min_str)
t_max = int(t_max_str)
temp_range = abs(t_max - t_min)
print("Перепад температуры: ", temp_range)