def reg(first, last, middle, age):
    res = f'{first.title()} {last.title()} {middle.title()} {age} г.р. зарегистрирован'
    return res


F_name = input()
L_name = input()
M_name = input()
age = input()

res = reg(F_name, L_name, M_name, age)
print(res)