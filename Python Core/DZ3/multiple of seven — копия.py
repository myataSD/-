# Ввод числа и пустой список для ответов
n = int(input('Введите целое число: '))
multiple_list = []

# Проверка  кратности числе от 1 до n на 7
for i in range(n):
        if i % 7 == 0:
           multiple_list.append(i)

# Вывод чисел
print(f'Числа, кратные 7 в диапазоне от 0 до {n}: {multiple_list}')