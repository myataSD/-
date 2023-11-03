# Функция для разделения числа на  фицры и после жтого высчитывание суммы цифр
def num_amount(number):
    number_str = str(number)
    sum_digits = 0

    # Итерация по каждой цифре в числе и добавление её к сумме
    for digit in number_str:
        sum_digits += int(digit)
    return sum_digits 

# Ввод числа, получение результат, и его вывод.
num =  input('Введите число: ')
result = num_amount(num)
print(f'Сумма цифр числа {num}, равна: {result}')