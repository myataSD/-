# Функция нахождения факториала
def factorial_calc(num):
    ni = 1
    # Условие, если num = 0 то вернуть 1 в иином случаи выполнять цикл.
    if num == 0:
        return 1
    else:
        # Цикл, для нахождения факториала
        for i in range(num):
            ni =  ni * (i + 1)
            factorial = ni
        return factorial

# Воод числа, для нахождения факториала
n = int(input('Введите целое число: '))

# Проверка на отрицательное число
if n < 0:
    print('Факториал отрицательного числа не определяется!')
else:
    factroial_res = factorial_calc(n)
    print(f'Факториал числа {n}, равен: {factroial_res}')