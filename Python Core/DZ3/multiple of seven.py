# Функция для проверки  кратности числе от 1 до n на 7
def multiple_of_seven(num):
    multiple_list = []
    for i in range(num):
        if i % 7 == 0:
           multiple_list.append(i)
    return multiple_list
            
        

# Ввод числа и вызов функции multiple_of_seven
n = int(input('Введите целое число: '))
result = multiple_of_seven(n)

# Вывод чисел
print(f'Числа, кратные 7 в диапазоне от 0 до {n}: {result}')

