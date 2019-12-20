def rm_duplicate(lst):
    temp_lst = []
    for val in lst:
        if val not in temp_lst:
            temp_lst.append(val)
    return temp_lst


numbers = [1, 2, 2, 4, 4, 5]
org_val = rm_duplicate(numbers)
print(org_val)