filename = "text.txt"
find_word = input("Введите заменяемое слово: ")
replace_word = input("Введите новое слово: ")

try:
    myfile = open(filename)
except FileNotFoundError:
    print("File not found!")
    exit()

text = myfile.read()
myfile.close()

# new_text = text.replace(find_word, replace_word)
new_text = text.replace(find_word.upper(), replace_word.upper())
new_text = new_text.replace(find_word.title(), replace_word.title())
new_text = new_text.replace(find_word.lower(), replace_word.lower())

print(new_text)

