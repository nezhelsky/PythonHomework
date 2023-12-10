user_input = input("Введите любое слово: ")

"""
Шакальный способ
Работает только с кириллицей))
"""

if ord(user_input[0]) in range(1072, 1104): # проверка первой буквы на принадлежность к диапазону "а-я"
    unicode_char = ord(user_input[0])
    capital = chr(unicode_char - 32) # сдвинув позицию в таблице символов назад на 32, получим заглавную букву

    print(capital + user_input[1:])
else:
    print("Вы ввели не слово или слово с заглавной буквы")


#VN: лучше все явные константы, как 1072, 1104, 32, - вычислять в начале программы, чтобы меньше зависеть от кодировки