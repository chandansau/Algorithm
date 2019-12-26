
def quicksort(lst):
    if lst:  # if given list (or tuple) with one ordered item or more:
        pivot = lst[0]
        # below will be less than:
        below = [i for i in lst[1:] if i < pivot] 
        # above will be greater than or equal to:
        above = [i for i in lst[1:] if i >= pivot]
        return quicksort(below) + [pivot] + quicksort(above)
    else: 
        return lst  # empty list


lst = [5, 8, 9, 6, 4, 7, 1, 5, 9, 8]
print(quicksort(lst))


# --------------------------- 2nd process --------------

q = lambda x: x and q([i for i in x[1:]if i <= x[0]]) + [x[0]] + q([i for i in x[1:]if i > x[0]])
print(q(lst))
