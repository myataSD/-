import pandas as pd

data = {'Имя':["Иван", "Мария", "Алексей", "Елена", 'Екатерина', 'Михаил', 'Анна'],
        'Фамилия':['Иванов', 'Смирнова', 'Петров', 'Сидорова', 'Иванова', 'Кузнецов', 'Петрова'],
        'Возраст':[25, 32, 41, 19, 28, 41, 24]
        }

DataF = pd.DataFrame(data)
print(DataF)

First3 = DataF.head(3)
print(First3)

Last3 = DataF.tail(3)
print(Last3)

DataF.to_csv(r'D:\output.csv')
