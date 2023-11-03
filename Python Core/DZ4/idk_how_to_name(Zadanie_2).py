s = input('Введите строку: ')

if len(s) >= 15:
    result = str()
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    print("Результат:", result)
else:
    print("Введена строка с недостаточным количеством символов.")