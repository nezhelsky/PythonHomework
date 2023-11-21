a = input("Введите десятичное число: ")

try:
    digit = int(a)
except ValueError:
    print("Вы ввели не число!")
else:
    binary = bin(digit)
    octa = oct(digit)
    hexa = hex(digit)
    
    print("Двоичное значение:", binary[2:])
    print("Восьмиричное значение:", octa[2:])
    print("16-ричное значение:", hexa[2:])
