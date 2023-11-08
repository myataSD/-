import re
# Ввод текста и пустой список предложений
input_str = input()
final_sentences = []
# Разделения текста на предложения
sentences = re.split(r'[.!?]', input_str)
# Цикл для "заглавления" предложений(хз как его еще назвать)
for sentence in sentences:
    sentence = sentence.strip()
    # Проверка на пустое предложение
    if not sentence:
        continue
    # Заглавление первой буквы в предлодении
    sentence = sentence[0].upper() + sentence[1:]
    # Добавление в список предлодений
    final_sentences.append(sentence)
# Создание текста из списка
final_text = '. '.join(final_sentences)

# добавляем точку в конец
final_text = final_text  + '.'
# Вывод
print(final_text)
         