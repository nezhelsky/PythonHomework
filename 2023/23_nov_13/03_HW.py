miles = float(0.621371)
km_str = input("Введите расстяние (км): ")

km_fl = float(km_str)  # я сделал тип данных float для вводимого числа, чтобы конвертировать дробные значения 
km_2_miles = km_fl * miles

print("Расстояние в милях =", km_2_miles)