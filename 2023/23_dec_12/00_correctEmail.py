email = input("Введите e-mail: ")
error = "Неверный адрес!"

for char in email:
    if not (char.isalnum() or char in ".-_@"):
        print(error)
        exit()

email_parts = email.split('@')
if len(email_parts) != 2:
    print(error)
    exit()

if not email_parts[0]:
    print(error)
    exit()

if not "." in email_parts[1]:
    print(error)
    exit()

domain = email_parts[1].split(".")

if len(domain[-1]) <= 1:
    print(error)
    exit()

print("Адрес верный")
    


