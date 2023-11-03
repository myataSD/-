# Ввод строки
s = input('Введите строку: ')

#Деление строки на элементы и создание списка
s = s.split()
n_list = [str(word) for word in s]

#Создание перевернутого  списка (rev_list)
rev_list = n_list[::-1]

# Вывод rev_list
print(rev_list)