
# Ввод колличества городов
n = int(input())

# Список городов, список повторяущихся городов и кол. дубликатов (изначально равно 0)
c_list  = []
temp = []
dub = 0

# Цикл создания списка городов
for i in range(n):
    city = input()
    c_list.append(city)
# Цикл подсчета дубликатов
for i in c_list:
    if i not in temp:
        temp.append(i)
        dub = dub + 1

# Вывод колличества дубликатов
print(dub)

    


    