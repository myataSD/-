# Функция для извлечения текста из сбалансированных скобок
def extract_balanced_text(input_text):
    output_text = ""
    open_bracket = input_text.find('(')
    
    while open_bracket != -1:
        close_bracket = input_text.find(')', open_bracket)
        
        if close_bracket != -1:
            output_text += input_text[open_bracket + 1:close_bracket] + " "
            open_bracket = input_text.find('(', close_bracket + 1)
        else:
            break

    return output_text

# Ввод строки и вызов функции extract_balanced_text
string = input()
result = extract_balanced_text(string)

# Вывод result
print(result) 