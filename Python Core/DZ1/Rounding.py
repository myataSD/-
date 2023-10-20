#Ввод занчений
num = float(input("Введите число:"))
amount_of_symbols = int(input("Введите количество знаков после запятой: "))

#Округление
rounding  =  round(num, amount_of_symbols)

#Вывод
print(f"Округленное число: {rounding}")