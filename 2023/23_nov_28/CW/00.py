for letter in "Python":
    if letter == 'o' or letter == "y":
        continue
    if letter == "n":
        break
    print("Текущая буква", letter)
else:
    print("Буквы кончились")