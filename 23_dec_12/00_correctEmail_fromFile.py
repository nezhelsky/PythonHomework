filename = "23_dec_12\input.txt"

try:
    myfile = open(filename)
except FileNotFoundError:
    print("File not found!")
    exit()

text = myfile.read()
myfile.close()
# print(text, end="  -  ")


email_list = text.splitlines()

for email in email_list:
    print(email, end="  -  ")
    chars_ok = True
    for char in text:
        chars_ok &= (char.isalnum() or char in ".-_@")

    email_parts = text.split('@')
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
        print("Адрес неверный!")
        


