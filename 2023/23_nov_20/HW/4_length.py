print("Введите координаты первой точки")
xa = input("Координата х: ")
ya = input("Координата y: ")

try:
    xa = int(xa)
    ya = int(ya)
except ValueError:
    print ("Введенное значение координат первой точки не является числом")
else:
    print("Введите координаты второй точки")
    xb = input("Координата х: ")
    yb = input("Координата y: ")
    try:
        xb = int(xb)
        yb = int(yb)
    except ValueError:
        print ("Введенное значение координат второй точки не является числом")
    else:
        length = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5    # теорема Пифагора
        print("Расстояние меджу данными точками равно:", length)