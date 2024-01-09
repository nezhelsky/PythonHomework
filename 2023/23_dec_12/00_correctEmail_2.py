email = input("Введите e-mail: ")
error = "Неверный адрес!"
chars_ok = True

for char in email:
    chars_ok &= (char.isalnum() or char in ".-_@")
    # chars_ok = chars_ok and (char.isalnum() or char in ".-_@")

email_parts = email.split('@')
parts_ok = len(email_parts) == 2
first_part_ok = bool(email_parts[0])
point_exist = "." in email_parts[1]
domain = email_parts[1].split(".")
domain_ok = len(domain[-1]) > 1

if chars_ok and parts_ok \
    and first_part_ok and point_exist \
    and domain_ok:
    print("Адрес верный")
else:
    print(error)
    


