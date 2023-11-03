# Функция для разделения строки и добавления ее в список
def num_sep(string):
    string = string.split()
    r_list = [int(n_num) for n_num in string]
    return r_list

# Ввод строки, вызов функции num_add и ввод степени n
s = input('Введите строку: ')
num_list = num_sep(s)
n = int(input('Введите степень: '))

# Пустой список с результатами
res =[]

# Цикл for для нахождения значений значений в степени n из списка.
for i in range(len(num_list)):
    num = num_list[i]
    divided = num ** n
    res.append(divided)
# Вывод результата
print(res)