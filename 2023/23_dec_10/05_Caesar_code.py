input_str = input("Введите сообщение: ")
input_key = input("Введите ключ: ")
key = int(input_key)

output_str = ""

for letter in input_str:
    if "а" <= letter.lower() <= "я" or "а" <= letter.lower() <= "z":
        code = ord(letter)
        new_code = code + key
        output_str += chr(new_code)
    else:
        output_str += letter

print(output_str)