user_input = input("Введите число: ")
shift = input("Введите сдвиг: ")

number = int(user_input)
shift = int(shift)

if len(user_input) < shift:
    print("Сдвиг не должен быть длиннее числа!")
else:
    mult = 10 ** shift

    second_part_num = number // (10 ** (len(user_input) - shift))
    first_part_num = number % (10 ** (len(user_input) - shift))

    print(first_part_num * mult + second_part_num)