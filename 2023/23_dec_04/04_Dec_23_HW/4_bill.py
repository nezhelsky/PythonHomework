in_cost = input("Введите стоимость покупки, $: ")
in_discount = input("Введите скидку, %: ")

cost = int(in_cost) 
discount = int(in_discount)

if discount > 100:
    print("Скидки больше 100% не существует!")
else:
    total = cost - (cost * discount / 100)
    message = "Стоимость товара со скидкой $%.2f" % (total)
    print(message)