user_input = input("Введите десятичное число: ")

digit = int(user_input)
binary = bin(digit)
octa = oct(digit)
hexa = hex(digit)

print("Двоичное значение:", binary[2:])
print("Восьмиричное значение:", octa[2:])
print("16-ричное значение:", hexa[2:])