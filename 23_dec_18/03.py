def get_number_int(dig1, dig2, dig3):
    str1 = str(dig1)
    str2 = str(dig2)
    str3 = str(dig3)

    number = str1 + str2 + str3
    number = int(number)
    return number

result = get_number_int(3, 5, 2)
print(result)