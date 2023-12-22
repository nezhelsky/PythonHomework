def get_square(a, b=None):
    # y = x if y is None else y      вариант записи if - else
    if b is None:
        square = a*a
    else:
        square = a*b
    return square

result = get_square(3, 4)
print("Площадь прямоугольника =", result)

result = get_square(3)
print("Площадь квадрата =", result)