import math

user_input_psquare = input("Введите периметр квадрата: ")
user_input_pcircle = input("Введите длину окружности: ")

try:
    psquare = int(user_input_psquare)
    pcrcl = int(user_input_pcircle)
except ValueError:
    print("Вы ввели не число!")
else:
    if pcrcl / (2 * math.pi) <= psquare / 8:    # для выполнения условия радиус круга должен быть <= 1/8 периметра квадрата
        print("Круг с длиной окружности", pcrcl, "впишется в квадрат с периметром", psquare)
    else:
        print("Круг с длиной окружности", pcrcl, "не впишется в квадрат с периметром", psquare)