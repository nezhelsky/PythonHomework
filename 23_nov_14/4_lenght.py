print("Введите координаты первой точки")
xa = input("Координата х: ")
ya = input("Координата y: ")

xa = int(xa)
ya = int(ya)

print("Введите координаты второй точки")
xb = input("Координата х: ")
yb = input("Координата y: ")

xb = int(xb)
yb = int(yb)
# Расстояние расчитываем по теореме Пифагора
# Тут не обязательно брать модуль разницы координат, т.к. дальше происходит возведение в квадрат
lenght = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
print("Расстояние меджу данными точками равно:", lenght)