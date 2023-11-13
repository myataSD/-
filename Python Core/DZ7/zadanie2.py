
a = [26,9,13,19,38]

# Проверка на кратность на 19 или 13 и если True добавление в список res
res = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, a))

print(res)