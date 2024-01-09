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
        result += line.capitalize() + "\n"

print(result)