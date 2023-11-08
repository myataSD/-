# Ввод текстов
input_string1 = input()
input_string2 = input()

# Убирание пробелов из  текста
clean_text1 = input_string1.replace(" ", "").lower()
clean_text2 = input_string2.replace(" ", "").lower()

# Создание множеств :|
set1 = set(clean_text1)
set2 = set(clean_text2)

# Проверка на анаграмму
if set1 == set2:
    print("Эти строки являются анаграммами.")
else:
    print("Эти строки не являются анаграммами.")
