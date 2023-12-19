n = 8

# for i in range(n):
#     print(i)

def print_range(num):
    if num > 0:
        i = print_range(num-1)
        print(i)
    return num

print_range(n)