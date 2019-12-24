# How are duplicates removed from a given array in Java? (solution)


def rm_duplicate(lst):
    b = []
    for i in lst:
        if lst.count(i) == 1:
            b.append(i)
    return b


lst = [1, 2, 2, 4, 4, 5]
print(rm_duplicate(lst))


