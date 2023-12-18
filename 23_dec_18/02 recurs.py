def get_sum_to(num):
    if num == 1:
        return 1
    return num + get_sum_to(num-1)


result = get_sum_to(4)
print("Сумма =", result)