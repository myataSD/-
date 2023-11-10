# Функция проверяющая вводную строку. (Явл ли он полиандромом)
def poliandrom(string):
    rev_string = ''.join(reversed(string)) # Создание копии строки на задом наперед
    if rev_string == string: # Сверка ориг строки и перевернутой копии, если они одинаковые вернуть True инече False
        return True
    else: 
        return False
# Ввод строки
inp_string = input()
# Вызов функции и присваивание результата 
poliandr_res = poliandrom(inp_string)
# Условие, если True: полиандром иначе "неполиандром"
if poliandr_res == True:
    print("Строка яваляется полиандромом!")
else:
     print("Строка неяваляется полиандромом!")