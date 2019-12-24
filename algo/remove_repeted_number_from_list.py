# remove all repeted number from the list


def rm_repeted_number(lst):
    temp_lst = []
    for val in lst:
        if val not in temp_lst:
            temp_lst.append(val)
    return temp_lst


numbers = [1, 2, 2, 4, 4, 5]
org_val = rm_repeted_number(numbers)
print(org_val)


# --------------------- 2nd process ------------------

def rm_repeted_number(lst):
    return list(set(lst))


numbers = [1, 2, 2, 4, 4, 5]
org_val = rm_repeted_number(numbers)
print(org_val)
