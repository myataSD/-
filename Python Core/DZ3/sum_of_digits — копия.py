# Ввод числа
num =  input('Введите число: ')
sum_digits = 0

num_str = str(num) # Преобразование числа в  строку

# Итерация по каждой цифре числа и добавление ее к сумма
for i in num_str:
    sum_digits += int(i)
# Вывод
print(f'Сумма цифр числа {num}, равна: {sum_digits}')