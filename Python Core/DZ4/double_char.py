# Ввод строки (string) и символа (char) который хотим удвоить
string = input('Введите текст (на латинице): ')
char = input('Введите символ который хотите удвоить: ')


doubled_char_string = string.replace(char, char * 2) # Удваиваемый символ char в string и записываем в doubled_char_string
print("Результат:", doubled_char_string) # Вывод doubled_char_string