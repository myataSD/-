def find_max(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        max_rest = find_max(num_list[1:])
        if num_list[0] > max_rest:
            return num_list[0]
        else:
            return max_rest
        

nums_list = [5, 2, 8, 12, 3]
maximum = find_max(nums_list)
print(maximum)
