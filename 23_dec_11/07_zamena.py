word = input("Введите фразу с цифрами: ")
diction = (
    ("1", "один"),
    ("2", "два"),
    ("3", "три"),
    ("4", "четыре"),
    ("5", "пять"),
    ("6", "шесть"),
    ("7", "семь"),
    ("8", "восемь"),
    ("9", "девять")
)


for i in diction:
    word = word.replace(i[0], i[1])

print(word)