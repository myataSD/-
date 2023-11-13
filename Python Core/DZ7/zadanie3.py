from functools import reduce

# Проверяет, какое из двух чисел больше, и возвращает наибольшее из них.
def a_or_b_is_max(a, b):
    return a if a > b else b

var_list = [1,4,102,5,3]

# применения a_or_b_is_max последовательно к элементам списка var_list и получения наибольшего элемента.
maximum = reduce(a_or_b_is_max, var_list)

print(maximum)