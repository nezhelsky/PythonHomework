def get_sum_to(num):
    total = 0
    for i in range(1, num+1):
        total += i
    return total


result = get_sum_to(6)
print("Сумма =", result)