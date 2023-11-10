n = int(input('Введите целое число: '))
ni = 1

if n < 0:
    print('Факториал отрицательного числа не определяется!')
else:
    if n == 0:
        res = 1
    else:
        # Цикл, для нахождения факториала
        for i in range(n):
            ni =  ni * (i + 1)
            factorial = ni
        res = factorial
    print(f'Факториал числа {n}, равен: {res}')