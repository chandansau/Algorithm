# lenear search  complex city=  o(N)


def max_number(num):
    maxi = num[0]
    # find max from list
    for nu in num:
        if nu > maxi:
            maxi = nu
    return maxi


num = [10, 20, 300, 40, 600]
print(max_number(num))


# --------------------2nd process --------------------


def max_number(num):
    num.sort()
    return num[-1]


num = [10, 20, 300, 40, 600]
print(max_number(num))
