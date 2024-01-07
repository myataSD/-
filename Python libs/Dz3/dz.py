import pandas as pd

data = pd.read_csv('data.csv', sep=';')

sel_1 = data[(data['Age'] > 30) & (data['Income'] < 30000)]
sel_2 = data[(data['Profession'] == 'Lawyer') & (data['Work Experience'] > 5)]

print(sel_1)
print(sel_2)