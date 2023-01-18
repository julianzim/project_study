from functools import reduce

lst = [2, 3, 4, 5]
print(reduce(lambda x, y: x*y, lst))
