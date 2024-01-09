from functools import reduce
numbers = (5, 6, -8, 33, 5)


inverted = list(map(lambda x: -x, numbers))
evens = list(filter(lambda x: x % 2 == 0, inverted))
result = reduce(lambda acc, x: x * acc, evens)
print(inverted)
print(evens)
print(result)