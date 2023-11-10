def maximux(num_amount, num_l):
    a = num_l[0]
    b = num_l[1]
    
    if num_amount == 2:
        if a > b:
            return a
        else:
            return b 
    elif num_amount == 3:
        res = num_l[0]
        
        for val in num_l[1:]:
            if val > res:
                res = val
        return res

num_amount = int(input())
num_list = []

if num_amount < 4:
    for i in range(num_amount):
        num = int(input())
        num_list.append(num)
        
        res = maximux(num_amount, num_list)
        print(res)
else:
    print("ERROR")
