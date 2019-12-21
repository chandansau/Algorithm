# find unique pair inside list


def unique_pair(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(len(b))
    return b


a = [(5, 7), (3, 9), (3, 9), (2, 2), (2, 2)]
print(unique_pair(a))
