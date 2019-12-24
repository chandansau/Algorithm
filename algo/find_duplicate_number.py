# How do you find the duplicate number on a given integer array


def find_duplicate(lst):
    b = []
    for i in lst:
        if lst.count(i) > 1:
            b.append(i)
    return b


lst = [5, 8, 9, 6, 4, 7, 1, 5, 9, 8]
print(find_duplicate(lst))

