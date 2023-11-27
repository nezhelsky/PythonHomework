count_input = 0   # счетчик введенных чисел
even_count = 0    # счетчик четных чисел
zero_number = 0   # счетчик нолей
positive_num = 0  # счетчик положительных чисел


while count_input < 10: # В этом цикле считаем положительные числа, нули и четные числа
    user_in = input("Введите число: ")
    a = int(user_in)
    count_input += 1
    
    if a > 0:
        positive_num += 1
    elif a == 0:
        zero_number += 1
    
    if a % 2 == 0:
        even_count += 1

print("Вы ввели:", even_count, "- четных чисел,", count_input - even_count, "- нечетных чисел,", zero_number, "- нолей,", positive_num, "- положительных и", count_input - zero_number - positive_num, "отрицательных чисел.")
        
