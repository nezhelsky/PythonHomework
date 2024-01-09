array = ['Timur', 'Argyn', 'Sergey', 'Almat', 'Vyacheslav', 'Alexandr', 'Galymjan', 'Vitaly']

result = filter(lambda x: len(x) >= 8, array)

result = filter(lambda x: x[0] < "O", array)

print (list(result))
