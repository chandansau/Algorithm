# TC = O(n)


def merge(a, b):
    """
    a and b are two sorted lists
    """
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        while i < len(a):
            c.append(a[i])
            i += 1
    if j<len(b):
        while j < len(b):
            c.append(b[j])
            j += 1
    print(c)


a = [3, 4, 5, 8, 9, 12]
b = [3, 5, 6]
merge(a, b)
