# find the second largest element in an array in a single for loop


def snd_lrgst(l):
    _max = 0
    smax = 0
    for x in l:
        if x > _max:
            smax = _max
            _max = x  # x is letest highest value
        else:
            smax = x
    return _max, smax


print(snd_lrgst([2, 3, 4, 2, 8, 6, 10, 9, 12]))


# ------------------2nd process-----------------------------

def snd_lrgst(num):
    num.sort()
    return num[-2]


num = [2, 3, 4, 2, 8, 6, 10, 9, 12]
print(snd_lrgst(num))
