lyrics = """
i dont wAnna close me Eyes
i dont wanna FALL to Sleep
cos` i miss you baby
and i don`t Want to miss a THing
"""

lines = lyrics.split("\n")

result = ""
for line in lines:
    if line:   # если строка не пустаая
        pre_result = line.capitalize().center(36)
        result += pre_result + "\n"

count = result.count("n")

print(count)
print(result)