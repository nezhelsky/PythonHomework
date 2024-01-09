user_in = input("Введите слово: ")
# a = len(user_in)

# for i in range(2, a, 3):
#     print(user_in[i])

position = 1
for char in user_in:
    if position % 3 == 0:
        print(char)
    position += 1