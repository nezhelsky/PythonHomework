word = input("Введите слово: ")
width = len(word)
summ = 0

for i in range(width):
    code_of_symbol = ord(word[i])
    summ += code_of_symbol

print("Сумма кодов всех символов в этом слове:", summ)