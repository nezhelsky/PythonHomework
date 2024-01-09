filename = "http.txt"

try:
    myfile = open(filename)
except FileNotFoundError:
    print("File not found!")
    exit()

text = myfile.read()
myfile.close()

protocol_part = text.split('//')
domen_name = text.split("/")

print("Протокол:", protocol_part[0])
print("Доменное имя:", domen_name[2])
print("Запрос:", domen_name[3])


