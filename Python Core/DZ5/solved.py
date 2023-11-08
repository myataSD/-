# Ввод фамилий
algebra = input().split()
geometric = input().split()
trigonometric = input().split()

# Нахождение пересечений
all_solvers = set(algebra) & set(geometric) & set(trigonometric)

# Если есть  учащиеся, решившие все 3 задачи, выввести их в алфавитном порядке, иначе, вывести, что 3 задачи никто не решил
if all_solvers:
    print('Вывод:'," ".join(sorted(all_solvers)))
else:
    print("Все три задачи никто не решил")